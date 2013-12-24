import inventory
from npc import *

# This file contains all the stages of the game

# Base class for all the stages
class Stage(object):
    
    def enter(self):
        print "Initializing stage... "
        return next_stage
    

# Derived actual stages used in the game
class Stage1(Stage):

    def enter(self):
        print """ 
        You are standing on the street that has 6 houses on it.
        The street looks empty and you are alone here. 
        """
        print "You can go forward, backward, or to one of the houses. "
        print "Forward, back, first house, second house? "
        action = raw_input("> ") 
        if "first" in action:
            return 'house1'
        elif "forward" in action:
            return 'street_sector2'
        elif "second" in action:
            return 'house2'
        elif "back" in action:
            print "You mysteriously ended up at the end of the street"
            return 'street_sector3'
        else:  
          print "Input is not readable" 
          return 'street_sector1' 
            
class Stage2(Stage):

    def enter(self):
        print "You are on the street between houses three and four."
        print "Forward, three, four, back: "
        print "Where do you want to go?"
        action = raw_input("> ")
        if "forward" in action:            
            print "You are moving forward. " 
            return 'street_sector3'
        elif "three" in action: 
            print "You are moving towards house three"
            return 'house3'
        elif "four" in action: 
            print "You are moving towards house four" 
            return 'house4'
        elif "back" in action:
            print "You decided to come back "
            return 'street_sector1'
        else: 
            print "Hm...what? " 

class Stage3(Stage):

    def enter(self):
        print 
        """ You are standing on the street between houses five and 
        and six.
        """
        print "Where would you like to go? "
        print "Forward, back, fifth house, sixth house: "
        action = raw_input("> ")
        if "fifth" in action:
            return 'house5'
        elif "forward" in action:
            print "You mystiriously ended up in the beginning of the street"
            return 'street_sector1'
        elif "sixth" in action:
            return 'house6'
        elif "back" in action:
            return 'street_sector2'
        else:  
          print "Input is not readable" 
          return 'street_sector3' 
          
# Stage four is ommited 


# This is house 1
class Stage5(Stage):
    """
    You are standing in the house that looks like a medieval european
    place. There is an old lady sitting in the middle of it.
    """
    def enter(self):
        print "You are in the house 1"
        print "What would you like to do? " 
        print "Exit, look around, talk: "
        action = raw_input("> ") 
        if action == "exit":
            print "You left the house"
            return 'street_sector1'
        elif "look" in action:
            print Stage5.__doc__
            return 'house1'
        elif action == "talk":
            old_lady = House1NPC()
            outcome = old_lady.talk()
            return outcome
        else:
            print "Hmm..what?"
            return 'house1'

# This is house 2                        
class Stage6(Stage):
    """
    You are in a house that looks like it is done in a very modern 
    style. All the decor and furnishings are incredibly well designed
    looks like a person who owns it has a refined sense of taste.

    There is a pretty young woman sitting in a cozy chair next to 
    the window. She has a distant look in her eyes. 
    """
    def enter(self):
        if inventory.horse != None and inventory.cat == None:
            print "You are in the house 2 now" 
            print "What would you like to do? " 
            print "Exit, look around, talk: "
            action = raw_input("> ") 
            if action == "exit":
                print "You left the house 2"
                return 'street_sector1'
            elif "look" in action:
                print Stage6.__doc__
                return 'house2'
            elif action == "talk": 
                lady = House2NPC()
                outcome = lady.talk()
                return outcome
            else:
                print "Can't recognize input"
                return 'house2' 
        else:
            print """
            You can't get in.It is either too late or too early 
            for you to take this path...  
            """
            return 'street_sector1' 

# This is house 3
class Stage7(Stage):
    """
    This house is designed in traditional Japanese style. Everything 
    you see breathes with history and all the objects are placed in 
    order. There is very little furniture in this place and the furnniture
    that is present is samall and not taking much space saving it for the 
    owner. 

    There is a samurai sitting in traditional clothes on some sort of a 
    pillow in the middle of the room. 
    """

    def enter(self):
        if inventory.cat != None and inventory.fence == None:
             print "You are in the house 3"
             print "What would you like to do? " 
             print "Exit, look around, talk: "
             action = raw_input("> ") 
             if action == "exit":
                 print "You left the house"
                 return 'street_sector2'
             elif "look" in action:
                 print Stage7.__doc__
                 return 'house3'
             elif action == "talk":
                 samurai = House3NPC()
                 outcome = samurai.talk()
                 return outcome
             else:
                 print "Hmm..what?"
                 return 'house3'
        else:
            print """
            You can't get in.It is either too late or too early 
            for you to take this path...  
            """
            return 'street_sector2' 

# This is house 4
class Stage8(Stage):
    """
    This house is a mess. It is a representation of chaos. Literally. 
    There are heaps of books all over it. A lot of them are open on 
    random pages somewhere close to the middle. Some of them face up, 
    some - face down. Plenty of computer motherboards with custom details
    attached to them are hanging on the walls. A lot of dust. You can 
    see that a lot of these books are dedicated to informational 
    technology. 

    You notice a guy sitting in front of the computer behind the shelf. 
    You come closer. His hair is gray and he is typing some sort of code
    on the screen. 
    """
            
    def enter(self):
        if inventory.fence != None and inventory.house == None:
            print "You are in the house 4"
            print "What would you like to do? " 
            print "Exit, look around, talk: "
            action = raw_input("> ") 
            if action == "exit":
                print "You left the house"
                return 'street_sector2'
            elif "look" in action:
                print Stage8.__doc__
                return 'house4'
            elif action == "talk":
                dennis = House4NPC()
                outcome = dennis.talk()
                return outcome
            else:
                print "Hmm..what?"
                return 'house4'
        else:
            print """
            You can't get in.It is either too late or too early 
            for you to take this path...  
            """
            return 'street_sector2'

# This is house 5
class Stage9(Stage):
    """
    This house looks like a shrine. It is designed in eastern style
    and has very little things in it. Those things that there are 
    in a very particular order that creates plenty of space. 

    You can see a guy who looks like a Buddah standing in the middle of 
    the house. Or maybe he just looks so. 
    """
            
    def enter(self):
        if inventory.house != None and inventory.ocean == None:
            print "You are in the house 5"
            print "What would you like to do? " 
            print "Exit, look around, talk: "
            action = raw_input("> ") 
            if action == "exit":
                print "You left the house"
                return 'street_sector3'
            elif "look" in action:
                print Stage9.__doc__
                return 'house5'
            elif action == "talk":
                buddah = House5NPC()
                outcome = buddah.talk()
                return outcome
            else:
                print "Hmm..what?"
                return 'house5'
        else:
            print """
            You can't get in.It is either too late or too early 
            for you to take this path...  
            """
            return 'street_sector3'

# This is house 6
class Stage10(Stage):
    """
    This house looks like a typical midwest or eastcoast crappy american 
    house. Walls that made out of shitty cheap material that does not 
    isolate from any noize or temperature. Quite a bit of space inside.
    The furniture is either from ikea or a thrift store. All the regular
    shit that you hate so much seems to be here. 

    The only unusual thing is that there is a humaz-sized zebra sitting 
    on the couch reading the newspapper. Zebra has glasses on and looks
    quite intelligent.
    """
            
    def enter(self):
        if inventory.ocean != None:
            print "You are in the house 6"
            print "What would you like to do? " 
            print "Exit, look around, talk: "
            action = raw_input("> ") 
            if action == "exit":
                print "You left the house"
                return 'street_sector3'
            elif "look" in action:
                print Stage10.__doc__
                return 'house6'
            elif action == "talk":
                zebra = House6NPC()
                outcome = zebra.talk()
                return outcome
            else:
                print "Hmm..what?"
                return 'house6'
        else:
            print """
            You can't get in.It is either too late or too early 
            for you to take this path...  
            """
            return 'street_sector3'
