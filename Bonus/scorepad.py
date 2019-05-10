#!/usr/bin/env python3
"""A little console-based scorepad app.

This uses cmd to provide much more flexible interaction.

Leverages the venerable ckyorn idea.

Uses a database access wrapper.
"""
import shelve
from contextlib import closing
import datetime
import cmd
import os
import code
import json
import csv
import sys
import readline

class ScoreDatabase:
    """An access wrapper around a scores database instance.

    Provides some attribute-like properties for a game database.
    """
    def __init__( self, name ):
        self.name= name
        self.db= shelve.open(name)
        self.filename= name+'.db'
    def close( self ):
        self.db.close()
        self.db= None
        self.fiename= None
        self.name= None
    @property
    def is_new(self):
        'game' not in self.db
    @property
    def modified(self):
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.filename))
    @property
    def game(self):
        return self.db['game']
    @game.setter
    def game(self, name):
        self.db['game']= name
    def validate_players( self, name_list ):
        for name in name_list:
            try:
                int(name)
                return "{0} isn't a valid player name".format(name)
            except ValueError:
                pass # good!
    @property
    def players(self):
        return self.db['players']
    @players.setter
    def players(self, name_list):
        self.db['players']= name_list
    @property
    def limit( self ):
        return self.db['limit']
    @limit.setter
    def limit( self, value ):
        self.db['limit']= value

    def history_iter( self ):
        for k in sorted(self.db.keys()):
            if k.startswith('game:'):
                _, game_txt = k.split(":")
                played= int(game_txt)
                yield played, self.db[k]
    def add_history( self, game, record ):
        """Expected keys are game, date, score, winner."""
        self.db['game:{0}'.format(game)]= record

    def export_csv( self ):
        wtr= csv.writer( sys.stdout )
        wtr.writerow( ['game', self.game] )
        wtr.writerow( ['players', self.players] )
        wtr.writerow( ['limit', self.limit] )
        keys = set()
        for g, row in self.history_iter():
            for k in row.keys():
                keys.add(k)
        header= list(keys)
        wtr.writerow(header)
        for g, row in self.history_iter():
            wtr.writerow( [row.get(k,None) for k in header] )
    def export_json(self):
        doc = {
            'game': self.game,
            'players': self.players,
            'limit': self.limit,
            'history': dict( (g, r) for g, r in self.history_iter() ),
        }
        print( json.dumps(doc, default=self.json_default, indent=2) )

    @staticmethod
    def json_default( obj ):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S")
        raise TypeError

class Quit(Exception):
    pass

def ckyorn( prompt, help="Enter y or n", quit=True, default=None,
           valid=lambda x: x[:1] in ('y','n') ):
    """Check for input being y or n. Will handle ? to provide help, also.
    If quit=True, can raise a Quit exception.
    """
    choices= 'y,n,?'
    if quit:
        choices += ',q'
    prompt= "{0} [{1}]: ".format(prompt, choices)
    txt= input( prompt ).lower()
    while not valid(txt):
        if default is not None and len(txt) == 0:
            return default
        elif quit and txt == 'q':
            raise Quit
        elif txt == '?':
            print( help )
        else:
            print( "Input is not one of {0}".format(choices) )
        txt= input( prompt ).lower()
    return txt[:1]

class Scorepad_Open( cmd.Cmd ):
    """Scorepad Commands with an open database."""
    prompt = 'scorepad: '

    def __init__( self, db, *args, **kw ):
        self.db= db
        self.quit= None
        self.in_game= None
        self.totals= None
        if db.is_new:
            self.intro= "Working with {0}\n".format(self.db.name)
        else:
            self.intro= "Working with {0} database, '{1}' from {2:%A, %b %d %H:%M}\n".format(
                self.db.name, self.db.game, self.db.modified)
        super().__init__( *args, **kw )

    def done_mssg( self, txt ):
        n = len(list(self.db.history_iter()))
        print( "{0}. Saved {1} games.\n".format(txt, n) )

    def do_EOF( self, args ):
        self.done_mssg("Done")
        self.quit= True
        return True
    def do_quit( self, args ):
        """Done playing."""
        self.done_mssg("Done")
        self.quit= True
        return True
    do_bye= do_quit
    def do_close( self, args ):
        """Close this file."""
        self.done_mssg("Closing database")
        self.quit= False
        return True

    def do_game( self, args ):
        """Get the game heading or show the game."""
        if args:
            if self.in_game:
                print( "Abandon the current game before changing the name.\n" )
                return
            print( "Setting game to {0}.\n".format(args) )
            self.db.game= args
        else:
            print( "Game is {0}.\n".format(self.db.game) )

    def do_players( self, args ):
        """Set the names of the players. Use " " between names; keep them short."""
        if args:
            # TODO: Or... provide a default score for the new player.
            if self.in_game:
                print( "Abandon the current game before changing players.\n" )
                return
            names = args.split()
            errors= self.db.validate_players(names)
            if errors:
                print( errors )
                return
            confirm = ckyorn("Set players to {0}?".format(names), quit=False)
            if confirm == 'y':
                print( "Setting players to {0}.\n".format(args) )
                self.db.players= args
        else:
            print( "Players are {0}.\n".format(self.db.players) )

    def do_limit( self, args ):
        """Set the score limit."""
        if args:
            try:
                limit= int(limit)
                confirm= ckyorn("Set the limit to {0}?".format(limit), quit=False)
                if confirm == "y":
                    print( "Setting limit to {0}.\n".format(limit) )
                    self.db.limit= limit
            except ValueError as e:
                print( "Sorry, '{0}' isn't a valid number.".format(args) )
        else:
            print( "Limit is {0}.\n".format(self.db.limit) )

    def do_history( self, args ):
        """Show the history"""
        for game, result in self.db.history_iter():
            print( game, result )
        print()

    def do_startgame( self, args ):
        """Start a new game."""
        played, _ = list(self.db.history_iter())[-1]
        confirm = ckyorn( "Start game {0}".format(played+1), quit=False )
        if confirm == "y":
            self.in_game= played+1
            self.totals = dict( (p,0) for p in self.db.players )
            self.prompt = "game {0}: ".format(self.in_game)
    do_newgame= do_startgame

    def do_endgame( self, args ):
        """Abandon a game without a final score."""
        if self.in_game:
            print( self.totals )
            confirm = ckyorn( "Abandoning game {0}".format(self.in_game), quit=False )
            if confirm == "y":
                self.in_game= None
                self.totals = None
                self.prompt = "score: "
    do_abandon= do_endgame

    def do_add( self, args ):
        """Add points to a given player.

        Use either "add player score" or "add score player"."""
        if not self.in_game:
            print( "You need to start a game, first." )
            return
        try:
            # Parse the args: (Player,score) or (score,Player)
            w0, w1 = args.split()
            try:
                points= int(w0)
                name= w1
            except ValueError:
                points= int(w1)
                name= w0
            # Update game score
            self.totals[name] += points
            print( "{0}\n".format(self.totals) )
            # End of game?
            player, score = max( self.totals.items(), key=lambda x:x[1] )
            if score >= self.db.limit:
                print( "{0} is the winner!".format(player) )
                confirm = ckyorn( "Done? Save it?", quit=False,
                                 help="Some games allow one final round." )
                if confirm == "n":
                    return
                record = {
                    'game': self.in_game,
                    'date': datetime.datetime.now(),
                    'score': self.totals,
                    'winner': (player, score),
                }
                print( "{0}\n".format(record) )
                self.db.add_history( self.in_game, record )
                # Reset state
                self.in_game= None
                self.totals = None
                self.prompt = "score: "
        except ValueError as e:
            print( "Sorry, '{0}' isn't a valid 'player number.' input".format(args) )
        except KeyError as e:
            print( "Sorry, '{0}' doesn't have a valid player name.".format(args) )

    def do_score( self, args ):
        """Show the scores."""
        if self.totals:
            print( self.totals )
            print()
        else:
            self.do_history( args )
    def emptyline( self ):
        self.do_score("")

    def do_export(self,args):
        """Export in then given format. Choices are json and csv. The default is json."""
        if args == "csv":
            self.db.export_csv()
        else:
            self.db.export_json()

    def do_shell( self, args ):
        locals = { 'db': self.db }
        console= code.InteractiveConsole(locals)
        # May not be a good idea; no clean exit.
        # console.interact("db is the open database")
        # Better approach is to use our own prompt allowing a cleaner exit
        print( "\ndb is the open ScoreDatabase object. Use exit to return to scorepad.\n" )
        line= input( ">>> " )
        while line != 'exit':
            while console.push(line):
                line= input( "... " )
            line= input( ">>> " )

class Scorepad( cmd.Cmd ):
    """Scorepad commands with no database."""
    intro = 'Welcome to the console scorepad. Type help or ? to list commands.\n'
    prompt = 'scorepad: '
    default_db= "scores"

    def do_open( self, args ):
        """open file

        Open a score file and start keeping score."""
        if len(args) == 0: args= self.default_db
        print( "open '{0}'".format(args) )
        with closing( ScoreDatabase(args) ) as database:
            so= Scorepad_Open( database )
            so.cmdloop()
        return so.quit # Exit all the way? Or just close the DB?
    def do_EOF( self, args ):
        """Control-D will quit"""
        return True
    def do_quit( self, args ):
        """Finish up."""
        print( "Done.\n" )
        return True # force postcmd to stop the loop.
    do_bye= do_quit

    def do_export( self, args ):
        """export filename format

        Opens a database, exports in the given format.
        Default format is json. csv can also be specified.
        """
        words = args.split()
        if len(words) == 1:
            name= words[0]
            format= "json"
        elif len(words) == 2:
            name, format = words
        else:
            print( "'{0}' isn't a valid filename (and optional format.)".format(args) )
            return
        if format in ("json", "csv"):
            with closing( ScoreDatabase(name) ) as database:
                if database.is_new:
                    print( "That's an empty database" )
                    return
                if format == "json":
                    database.export_json()
                elif format == "csv":
                    database.export_csv()
        else:
            print( "'{0}' doesn't have a valid format: it must be json or csv.".format(args) )

if __name__ == "__main__":
    s= Scorepad()
    s.cmdloop()