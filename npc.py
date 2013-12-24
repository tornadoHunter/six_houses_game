from sys import exit
# All the variables are going to come from inventory. Horse, ocean, etc...
import inventory
class Npc(object):
    "This is a base class for all the npcs in the game" 

    def talk(self):
        print "I am talking to you, human"
   
class House1NPC(Npc):

    def talk(self):
        print "Are you ready to hear my question? " 
        answer = raw_input("(y/n)> ") 
        if answer == "y" or answer == "Y":
            print """
            Alright! 

            You see an open field out there in nature. There is 
            a horse on that field. How does it look like? Describe it. 
            Is it white and beautiful? Dark maybe? Do you hate horses 
            at all? You can tell me if you do, no problem with that, 
            but in order for you to benefit you should be honest. 
            You should describe what you imagination says in detail.  
            """
            inventory.horse = raw_input("> ")
            print "Perfect! Go on to the second house and be patient \
                   you will soon find the ansers. "
            return 'street_sector1' 
        else: 
            print "Alright, doesn't look like you want to talk yet." 
            return 'house1' 

class House2NPC(Npc):

    def talk(self):
        print """
        Oh! She seemed to be a bit surprised by seeing you. 
        But after a moment she smiles and says: \"Ready for the next
        question? \" 
        """
        answer = raw_input("(y/n)> ") 
        if answer == "y" or answer == "Y": 
            print """
            Good! 

            After the field where you encountered the horse on you went on
            down the unpaved road towards the forest. A cat crosses 
            the road right in front of you. 

            What are you going to do? Catch it? Chase it? Leave it 
            alone? Describe in as many details as your imagination 
            suggests, so your journey might have a better result.
            And don't worry - this secret dies with me. 
            """
            inventory.cat = raw_input("> ") 
            print "Alright. Your answer is accepted. Go on to the \
                   next house to continue your journey. " 
            return 'street_sector1'
        else: 
            print "Hmm..you are confusing me with your wording..." 
            return 'house2' 

class House3NPC(Npc):

    def talk(self): 
        print """
        The samurai gets awakened from his meditation by you. For a 
        moment, you are afraid that he will get angry and cut you 
        down with a sword, but his face looks like a mountain 
        spring. Cold and steady. 

        It the very same fashion as his face is he asked you semi-quietly:
        \"Would you like to take the next step to Zen? \"
        """
        answer = raw_input("(y/n)> ") 
        if answer == "y" or answer == "Y": 
            print """
            Wakarimashta!

            You enter the forest and walk in there for a while. Finally, 
            you stumble upon some sort of a house that you really cannot 
            see behnd an annoying fence. 

            Describe me this fence. Is it made of steel? Wood? Are you 
            andgry about it? You need to go through this fence. How will 
            you go about it? Try to find an entrance? If there is no 
            obvious way to enter what will you do? Break the fence jump 
            over it or something else? Use your imagination. 
            """
            inventory.fence = raw_input("> ") 
            print "Your answer is accepted! Go on to the next house with \
                   your quest. " 
            return 'street_sector2' 
        else: 
            print "You don't really want to talk. Come back next time. " 
            return 'house3' 

class House4NPC(Npc): 

    def talk(self): 
        print """
        The guy turns around and looks at you. He doesn't look surprised
        at all. His face looks extremely familiar to you, but you cannot 
        really tell where you've seen it. 

        He smiles and asks in a soft manner: \"Wanna do some hacking? \"
        """
        answer = raw_input("(y/n)> ") 
        if answer == "y" or answer == "Y": 
            print """
            Perfect! 

            ...So you finaly reached the house through the fence. 
            It looks abandoned, but to what extent? How bad does it 
            look? Or how good? Is it big? Small? 

            Describe house in as much detail as possible. 
            """
            inventory.house = raw_input("> ") 
            print "I'll remember your answer. Go further in your journey \
                   now! " 
            return 'street_sector2'
        else: 
            print "Come back when you really want to talk. " 
            return 'house4' 

class House5NPC(Npc): 

    def talk(self): 
        print """
        You come closer to talk and notice that the guy is actually 
        smoking a sigar. He turns around to you and frowns. 

        He says with the same look: \"Want something? \" 
        You keep staring at the huge sigar in his mouth. 
        He gives a brief look to it and smiles decadently. 
        \"Don't pay attention at little things like that! I actually 
        like sigars! Haaa! 
        
        So...man...quit breaking my balls and tell me you want to 
        hear the rest of the story so I can end my existence in this 
        virtual reality. 
        """
        answer = raw_input("(y/n)> ") 
        if answer == "y" or answer == "Y": 
            print """
            Nice! 

            After examination of the house you decided to go back 
            on the road and continue your trip.

            You went for quite a long time when you finally exited 
            the forest and started to walk through the field. 
            Suddenly the road has ended and you could see that 
            there is an ubrupt end of the landscape. It turns into 
            an oceanshore. 

            You standing above this ocean. What does it look like? 
            Describe waht your imagination tells you in as much
            detail as possible, so your journey would have a 
            better outcome. 
            """
            inventory.ocean = raw_input("> ") 
            print "Ok! You can finally go for your result to the last \
                   house! "
            return 'street_sector3'
        else: 
            print "You don't really wanna talk. Do you? " 
            return 'house4' 

class House6NPC(Npc): 

    def talk(self): 
        print """
        Zebra puts the newspaper on the table and looks you directly in 
        the eyes. It's quite morbid to feel its look but you stay still. 

        Then Zebra smiles and says in a frindly manner: \" You probably
        wanna know what this all is about? Ha? No wonder...\"
        """
        answer = raw_input("(y/n)> ") 
        if answer == "y" or answer == "Y": 
            print """
            Well... I guess you deserve to know. 

            /For testing my poorly written game ; ) / 
            Now, just don't take seriously all I am gonna tell you. 
            Not because I am a zebra, but because...
            It might be true, or might not be. Always remember 
            that this is just a game. Just like life itself.

            Still remember your first description? That was a horse 
            that you saw. Horse represents what you think of the 
            opposite gender. And you said ...             

            %s 

            Now, the second thing we talked about was a cat. 
            Whatever you might think, but cat symbolizes your 
            relationships with parents. You said about it ...

            %s

            The next one was the fence. Well...the fence is the law 
            and how you interact with it. Don't worry if you broke 
            one in the game - its just a virtual one. If you jumped 
            over it it means you kinda don't feel like breaking it, 
            but still can sometimes be on the edge. Just as a reminder 
            what you said was ...

            %s 

            The abandoned house behind the fence, remember? 
            You said about it that it looks like ...

            %s

            Well...this is how you think family should be. If it is 
            small - there are few family members. If it is decayed and
            burned you might be opposed to haveing a family. If it is 
            a nice place in your descripton - you might be ready to 
            start your own family. 

            And finally the ocean. Whatever you think about the ocean
            is how you might view love and sexuality. So if it is 
            a calm and quiet ocean - you like stability and permanence 
            if your feelings. If it is stormy - you are probablay of 
            a type who always chases sharpness and adrenaline in 
            relationships. You said...

            %s

            Make your conclusions

            And always remember: you are your only judge. 
            No one can tell you who you are, but you. 

            The end.
            """ % (inventory.horse, inventory.cat, inventory.fence,
                   inventory.house, inventory.ocean) 
            exit(1)
        else: 
            print "Well...then you should go elsewhere..." 
            return 'house6' 

