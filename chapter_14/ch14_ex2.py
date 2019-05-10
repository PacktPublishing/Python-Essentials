#!/usr/bin/env python3
"""Python Essentials

Chapter 14, Example Set 2
"""
import logging
import logging.config
from Chapter_13.ch13_ex3 import Logged

logger= logging.getLogger(__name__)

class Demonstration(metaclass=Logged):
    def __init__(self, arg1, arg2):
        self.arg1= arg1
        self.arg2= arg2
        self.logger.info("Created {arg1}, {arg2}".format_map(self.__dict__) )
    def __del__(self):
        self.logger.info("Removed {arg1}, {arg2}".format_map(self.__dict__) )

config = {
    'version': 1,
    'handlers': {
        'console': {
            'class' : 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {
        'level': 'DEBUG',
        'handler': ['console'],
    }
}

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)
    #logging.config.dictConfig(config)
    x= Demonstration("Object 1", 3.14)
    x= Demonstration("Object 2", 2.718)
    x= 22
    logging.getLogger('Demonstration').setLevel(logging.DEBUG)
    logging.shutdown()

    with open('app.log') as data:
        print( data.read() )