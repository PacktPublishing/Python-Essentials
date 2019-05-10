#!/usr/bin/env python3
"""A little score-keeper app.

This shows **very** fixed interactions.

Based (partially) on this list of old Solaris commands:

ckdate(1)
ckgid(1)
ckint(1)
ckitem(1)
ckkeywd(1)
ckpath(1)
ckrange(1)
ckstr(1)
cksum(1)
cktime(1)
ckuid(1)
ckyorn(1)
"""
import shelve
from contextlib import closing
import datetime
import cmd
import os
import code

class Quit(Exception):
    pass

def ckyorn( prompt, help="Enter y or n", quit=True, default=None, valid=lambda x: x[:1] in ('y','n') ):
    choices= 'y,n,?'
    if quit:
        choices += ',q'
    prompt= "{0} [{1}] ⎆ ".format(prompt, choices)
    txt= input( prompt ).lower()
    while not valid(txt):
        if default is not None and len(txt) == 0:
            return default
        elif txt == '?':
            print( help )
        elif quit and txt == 'q':
            raise Quit
        else:
            print( "Input not {0}".format(choices) )
        txt= input( prompt ).lower()
    return txt[:1]

def ckstr( prompt, help="Enter a value", quit=True, default=None, valid=lambda x: x ):
    choices= '?'
    if quit:
        choices += ',q'
    prompt= "{0} [{1}] ⎆ ".format(prompt, choices)
    txt= input( prompt )
    while not valid(txt):
        if default is not None and len(txt) == 0:
            return default
        if txt == '?':
            print( help )
        elif quit and txt == 'q':
            raise Quit
        else:
            print( "Input not {0}".format(choices) )
        txt= input( prompt )
    return txt

def tryint( value ):
    try:
        int(value)
        return True
    except ValueError:
        pass

def ckint( prompt, base=10, help="Enter an integer value", quit=True, default=None, valid=tryint ):
    choices= '?'
    if quit:
        choices += ',q'
    prompt = "{0} [{1}] ⎆ ".format(prompt, choices)
    txt= input(prompt)
    while not valid(txt):
        if default is not None and len(txt) == 0:
            return default
        if txt == '?':
            print( help )
        elif quit and txt == 'q':
            raise Quit
        else:
            print( "Input not {0}".format(choices) )
        txt= input( prompt )
    return int(txt)

def ckitem( prompt, items, help="Enter one of the allowed items", quit=True, default=None, valid=None ):
    if not valid:
        valid = lambda x: x in items
    choices= ",".join(items) + ",?"
    if quit:
        choices += ',q'
    prompt = "{0} [{1}] ⎆ ".format(prompt, choices)
    txt= input(prompt)
    while not valid(txt):
        if default is not None and len(txt) == 0:
            return default
        if txt == '?':
            print( help )
        elif quit and txt == 'q':
            raise Quit
        else:
            print( "Input not {0}".format(choices) )
        txt= input( prompt )
    return txt

def get_players():
    names = []
    print( "Enter the players" )
    name = ckstr( "Player's Name", default="" )
    while name:
        names.append(name)
        print( "Players:", names )
        name = ckstr( "Player's Name", default="" )
    return names

def setup( database ):
    game = database.get('game',"")
    if game != "":
        print( "Game:", game )
        same_game= ckyorn( "Continuing same game?", default="y" )
    else:
        print( "No game history, starting fresh" )
        same_game= "n"

    if same_game == 'n':
        for k in database.keys():
            del database[k]
        game = ckstr( "What game?" )
        database['game']= game

    names = database.get('players',[])
    if names:
        print( "Players:", names )
        same_names = ckyorn( "Continuing with these players?", default="y" )
    else:
        same_names = 'n'
    if same_names == 'n':
        names = get_players()
        database['players']= names

    limit = database.get('limit',None)
    if limit:
        print( "Play to {0}".format(limit) )
        same_limit = ckyorn( "Continue with this limit?", default="y" )
    else:
        same_limit = 'n'
    if same_limit == 'n':
        limit = ckint( "Play to score of" )
        database['limit']= limit

    database.sync()

def show_history( database ):
    played= 0
    for k in sorted(database.keys()):
        if k.startswith('game:'):
            _, game_txt = k.split(":")
            played= int(game_txt)
            print( played, database[k] )
    return played

def score_game( database, game ):
    players= database['players']
    totals= dict( (p,0) for p in players )
    r = 1
    while max(totals.values()) < database['limit']:
        print( "Points for round {0}".format(r) )
        scores= {}
        while set(scores.keys()) != set(players):
            player= ckitem( "Player", players )
            score= ckint( "Score for {0}".format(player) )
            scores[player]= score
        for k in players:
            totals[k] += scores[k]
        print( totals )
        print()
        r += 1
    winner= max( totals.items(), key=lambda x:x[1] )
    print( "Winner", winner )
    record = {
        'game': game,
        'date': datetime.datetime.now(),
        'score': totals,
        'winner': winner,
    }
    database['game:{0}'.format(game)] = record
    database.sync()
    print()

def prompted_interaction(database):
    setup( database )
    played= show_history(database)
    print()
    try:
        game = played+1
        go= ''
        while go != 'q':
            go= ckitem( "s-start game {0}, h-history".format(game), ["s","h"] )
            if go == 'h':
                show_history(database)
            elif go == 's':
                score_game(database, game)
                game += 1
    except Quit:
        pass
    print( "Done" )

def get_history( database ):
    for k in sorted(database.keys()):
        if k.startswith('game:'):
            _, game_txt = k.split(":")
            played= int(game_txt)
            yield played, database[k]

if __name__ == "__main__":

    with closing(shelve.open("scores")) as database:
        prompted_interaction( database )
