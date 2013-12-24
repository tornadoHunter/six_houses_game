#!/usr/bin/env python2 

from stages import * 
from inventory import * 

        
class Engine(object):

    def __init__(self, global_map):
        self.world = global_map
       
    def play(self):
    
        current_location = 'street_sector1'
         
        while True:
            print "\n"
            print "-" * 10
            next_location = self.world.next_stage(current_location)
            current_location = next_location.enter()

           
class Map(object):

    stages = {
        'street_sector1': Stage1(),
        'street_sector2': Stage2(),
        'street_sector3': Stage3(),
        'house1': Stage5(),
        'house2': Stage6(),
        'house3': Stage7(),
        'house4': Stage8(),
        'house5': Stage9(),
        'house6': Stage10(),
    }
    
    def __init__(self):
        print "Initializing the global map..."

    def next_stage(self, stage_name):
        return Map.stages.get(stage_name)
           
print """ 
Well the game is a project which I might finish or might not. 
Basically there are six houses on the street which you are on. 
You need to talk to six people in there. And give them your answer. 
Go in order, so you will have a better result at the end. 

"""
wmap = Map()
game = Engine(wmap)
game.play()
