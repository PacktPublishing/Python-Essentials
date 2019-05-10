#!/usr/bin/env python3
"""Python Essentials

Chapter 15, Script 2
"""
import cmd

class Conversion(cmd.Cmd):
    prompt="Known temp: F x or C x> "
    def do_C(self, arg):
        """C x, converts Celsius temperature x to Fahrenheit."""
        try:
            c= float(arg)
            f= c*9/5+32
            print("C={c:.0f}°, F={f:.0f}°".format_map(locals()))
        except ValueError as ex:
            print( "'{0}' is not a valid number".format(arg) )
    def do_F(self, arg):
        """F x, converts Fahrenheit temperature x to Celsius."""
        try:
            f= float(arg)
            c= (f-32)*5/9
            print("C={c:.0f}°, F={f:.0f}°".format_map(locals()))
        except ValueError as ex:
            print( "'{0}' is not a valid number".format(arg) )
    def do_EOF(self, arg):
        """Enter ^D (or ^Z on Windows) to exit."""
        return True

if __name__ == "__main__":
    Conversion().cmdloop()