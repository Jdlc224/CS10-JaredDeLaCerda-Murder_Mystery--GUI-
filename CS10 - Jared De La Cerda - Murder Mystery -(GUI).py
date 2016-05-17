# -*- coding: utf-8 -*-
import sys
import pickle
import time

#NAme : Reggae Raphael

node = None
inventory = []
dog = 0


class Room:
    def __init__(self,name, north, east, south, west, up, down, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.description = description
    
    def move(self,direction):
        global node
        node = globals()[getattr(self,direction)]

Intro = Room('Intro',None,None,None,None,None,None,'')
Bedroom = Room('Bedroom',None, None,None,'Hallway',None,None,'You awake to the smoke of a fire. The fire is quickly spreading over the house, you must get out.To the west is the hallway.')
Hallway = Room('Hallway','Bathroom','Window',None,'Stairway',None,None,'You are in the hallway.To the north is your bathroom,west is a stairway, and to the east is a window.')
Window = Room('Window',None,None,None,'Hallway',None,'Outside_D','Your standing in front of a opened window and when you look out you notice it\'s not that far of a drop.Type "down" to go out the window.')
Outside_D = Room('Outside_D',None,None,None,None,None,None,'You Died')
Bathroom = Room('Bathroom',None,None,'Hallway',None,None,None,'You are standing in your bathroom. There is something shimmering in the toilet water. Type "pick up" to pick up the item.')
Stairway = Room('Stairway',None,'Hallway',None,None,None,'Front_Room','You\'re standing at the stairs. You could see the front door from up here, you are so close to getting out.Type "down" to go down the stairs.')#? New Map Part
Front_Room = Room('Front_Room',None,None,None,None,None,None,'')

Cemetary = Room('Cemetary','Cathedral',None,None,None,None,None,'As you get close to the light you see it\'s coming from a small cathedral and see the speck of light through the boarded up window. To the north is the door')
Cathedral = Room('Cathedral','Inside',None,'Coffin',None,None,None,'As you get close to the light you see it\'s coming from a small cathedral and see the speck of light through the boarded up window. To the north is the door')
Coffin = Room('Coffin',None,None,None,None,None,None,'')
Inside = Room('Inside','Alter',None,None,'Side_Room',None,None,'You walk inside. You notice the candles lit by the window. You see some more light coming from a room to your left, but you also hear a faint sound coming from a room ahead of you.')
Alter = Room('Alter',None,'Basement','Inside',None,None,None,'You are standing at an alter. There\'s a door to the east of you.')
#Basement_Door = Room('Basement_Door',None,None,'Alter',None,None,None,'You go down to the basement. It\'s empty.')
Basement = Room('Basement',None,None,'Alter',None,None,None,'You open the door and go down stairs into a dark basement.Looks empty.')
Side_Room = Room('Side_Room',None,'Stairs',None,'Closet_Door',None,None,'You walk into the room and see two doors west and east of you.')
Closet_Door = Room('Closet_Door',None,None,'Stairs',None,None,None,'You try opening the door multiple times but it won\'t budge.Maybe you can try and use that key you have. Type "use" to try the key.')
Closet = Room('Closet',None,None,'Side_Room',None,None,None,'Just a closet. Everything looks to be like it has not been touched for years. There\'s a pice of paper the floor that has something written on it. Type "read" to see what it says.')
Stairs = Room('Stairs',None,'Inside','Side_Room',None,None,'Storage_Room','Behind the door are stairs that lead down to another room.Type "down" to go down.')
Storage_Room = Room('Storage_Room','Table',None,'Side_Room',None,None,None,'You go down the stairs into a storage room. It\'s dimly lit by some candles. You see something on a table on the other side of the room in front of you.')
Table = Room('Table',None,'Light','Storage_Room',None,None,None,'You approach the table. There are candles surrounding the edges of the table and you notice there is a picture in the middle. Before you can get a good look at it you hear something to the left of you and see a light start flickering.')
Light = Room('Light',None,None,None,None,None,None,'')


Cityburg = Room('Cityburg',None,None,None,None,None,None,'')

Bus_Stop = Room('Bus_Stop',None,'AG_Street',None,None,None,None,'Your standing at the bus stop, to the east you see a building.')
#Grocery_Store = Room('Grocery_Store',None,None,'Bus_Stop',None,None,None,'')
AG_Street = Room('AG_Street','Old_Store','HN_Street','Bus_Stop',None,None,None,'You walk down AG Street and to the north of you is an old store. To the east is HN Street')
Old_Store = Room('Old_Store',None,None,'AG_Street',None,None,None,'Its an abandoned store.')
HN_Street = Room('HN_Street',None,None,'AG_Street','Park_Entrance',None,None,'To the west is a park and south is AG Street.')
Park_Entrance = Room('Park_Entrance','Park',None,'HN_Street',None,None,None,'To the north of you is the entrance of the park.')
#OU_Street = Room('OU_Street','Main_Street',None,None,None,None,None,'')
#VZ_Street = Room('VZ_Street',None,None,'OU_Street',None,None,None,'')
#Main_Street = Room('Main_Street','Park','Abandoned_Factory',None,'Water_Street',None,None,'')
#Water_Street = Room('Water_Street',None,None,None,None,None,None,'')
Park = Room('Park',None,None,None,'Shack',None,None,'Your standing by the entrance of the park. All of a sudden the gates close behind you. To the west you notice a strange figure going inside a shack.')
Shack = Room('Shack','Mystery_Door',None,None,None,None,None,'Your standing in an empty room, in front of you is a hallway with a door at the end.')
Mystery_Door = Room('Mystery_Door',None,None,'Shack',None,None,None,'You approach the door but its locked with a keypad. You must enter the 6 digit password to open the door. Guess the code to continue. ')
#Abandoned_Factory = Room('Abandoned_Factory',None,None,None,None,None,None,'')


Aregs_Aquatic_Aerobic_Arena = Room('Aregs_Aquatic_Aerobic_Arena',None,None,None,None,None,None,'')
Bobs_Bar = Room('Bobs_Bar',None,None,None,None,None,None,'')
Crispy_Chickens_Club = Room('Crispy_Chickens_Club',None,None,None,None,None,None,'')
Davids_Delicious_Doughnuts = Room('Davids_Doughnuts',None,None,None,None,None,None,'')
Erics_Everything_Emporium = Room('Erics_Everything_Emporium',None,None,None,None,None,None,'')
Franks_Flapjacks = Room('Franks_Flapjacks',None,None,None,None,None,None,'')
Geralds_Garage = Room('Geralds_Garage',None,None,None,None,None,None,'')
Hanks_Homemade_Hoagies = Room('Hanks_Homemade_Hoagies',None,None,None,None,None,None,'')
IceCubes_Icecream = Room('IceCubes_Icecream',None,None,None,None,None,None,'')
Jareds_Jewelry = Room('Jareds_Jewelry',None,None,None,None,None,None,'')
Kristens_Kabobs = Room('Kristens_Kabobs',None,None,None,None,None,None,'')
Luigis_Lemonade = Room('Luigis_Lemonade',None,None,None,None,None,None,'')
Micheals_Milkshakes = Room('Micheals_Milkshakes',None,None,None,None,None,None,'')
Nu_Noodles = Room('Nu_Noodles',None,None,None,None,None,None,'')
Olafs_Opera = Room('Olafs_Opera',None,None,None,None,None,None,'')
Patricks_Pub = Room('Patricks_Pu b',None,None,None,None,None,None,'')
Rickys_Ratatouille = Room('Rickys_Ratatouille',None,None,None,None,None,None,'')
Sallys_Supermarket = Room('Sallys_Supermarket',None,None,None,None,None,None,'')
Valeries_Vineyard = Room('Valeries_Vineyard',None,None,None,None,None,None,'')
Wallys_Workshop = Room('Wallys_Workshop',None,None,None,None,None,None,'')
Xaviers_Xylophones = Room('Xaviers_Xylophones',None,None,None,None,None,None,'')
Zacks_Zoo = Room('Zacks_Zoo',None,None,None,None,None,None,'')

node = Intro



if node == Intro:
        print 'Your name is Reggae Raphael. You grew up in the city of'"\x1B[3mCityville\x1B[23m"'.You had a wife and son,until tragically one day while they were driving your wife lost control of her car and swerved off a bridge and then landed in the water.'
        print 'You used to be a detective before you decided to retire early to pursue your other passions. One being that you always loved Reggae music since you were \x1B[3m17\x1B[23m and you also wanted to be a DJ, hence the name your friends gave you. So you moved to Cityburg and opened a club, which has been pretty successful.'
        #print "\x1B[3mHello World\x1B[23m"
        #print("\x1b[31m\"This text is in red,cool!\"\x1b[0m")
        #"red"
        node = Bedroom
        time.sleep(3)

#Save Function
def save():
    global name, player#<-Examples)
    with open('savegame.day', 'ab') as f:
        pickle.dump([node],f, protocol=2)
                #Example ^^^
    print "Game successfully saved"
    
#Load Function
def load():
    global name, player
    with open('savegame.day', 'rb') as f:
        name,player, = pickle.load(f)
    print "Game successfully loaded"
    
    


#-------------------------------------------------------------------------------

def display_choices(node):
    print "\nYour Choices: "
    for i,p in enumerate(node["Choices"]):
        print '\t%d: "%s"' % (i, p[2])#1

def player_says(text, destination):
    global dialogue_node
    print "You say: '%s'" % text
    dialogue_node = destination


Javier = {
    "Start" : {
        "Dialogue" : "H..He...Hello? Someone there?",
        "Choices" : [
            (player_says,"","No"),
            (player_says,"","Yes"),
            (player_says,"","Hello?"),
            ]
        },
    
    "Hello" : {
        "Dialogue" : "Can you help me, my hands are chained to the wall. Maybe you could find something to get me free.",
        "Choices" : [
        (player_says,"","Ok"),
        (player_says,"","What happened?"),
        (player_says,"","Sucks for you."),
        ]
    },
        
    "Yes" : {
        "Dialogue" : "Can you help me, my hands are chained to the wall. Maybe you could find something to get me free.",
        "Choices" : [
        (player_says,"","Ok"),
        (player_says,"","What happened?"),
        (player_says,"","Sucks for you."),
        ]
    },
    
    "What happened?" : {
        "Dialogue" : "I was just doing my job and prepping a new grave when all of sudden I was hit in the back of the head.",
        "Choices" : [
        (player_says,"","So your a cemetary caretaker"),
        (player_says,"","Well I guess I\"ll keep looking."),
        ]
    },
    
    "So your a cemetary caretaker" : {
        "Dialogue" : "Yup",
        },
}    
    
#-------------------------------------------------------------------------------

def play():
    if dog > 0:
        node = 'Cementary'


while True:
    print 
    print 'Room:' + node.name
    print
    print 'Description:' + node.description
    
    movement = ['north','east','south','west','up','down']
    command = raw_input('>').strip().lower()
    
    if command == 'inventory':
        print inventory
    
    if command == 'map':
        print '''
                                  
                                _______  
                               |       |
                               |       |             ____________
                               |_______|            |            |
                                  |                 |  Warehouse |
                       ___________|____________     |____________|   
                       |                      |            |
                       |                      |        ____|__
                       |           _______    |        |     |
                       |  _____   |Factory|   |        |Docks|
_______________________|_|Store|  |       |___|________|     |
          |            | |_____|  |       |   |        |     |
    ______|_____       |          |_______|   |        |_____|
    |          |       |                      |
    | Bus Stop |       |                   ___|____
    |__________|       |__________________|        |
                                          | Park   |
                                          |________|


        '''
        
    if node == Park:
        if command == 'park map':
            print '''
            hi this is the park map.
            '''
    
    if command in ['itwasmeallalong']:
        print 'You win! Congratulations!'
        print '''
                     ¶¶¶¶¶¶¶¶¶¶¶¶ 
                 ¶¶              ¶¶ 
   ¶¶¶¶¶        ¶¶                ¶¶ 
   ¶     ¶     ¶¶      ¶¶    ¶¶     ¶¶ 
    ¶     ¶    ¶¶       ¶¶    ¶¶      ¶¶ 
     ¶    ¶   ¶¶        ¶¶    ¶¶      ¶¶ r
      ¶   ¶   ¶                         ¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶                         ¶¶ 
   ¶            ¶    ¶¶            ¶¶    ¶¶ 
  ¶¶            ¶    ¶¶            ¶¶    ¶¶ 
 ¶¶   ¶¶¶¶¶¶¶¶¶¶¶      ¶¶        ¶¶     ¶¶ 
 ¶               ¶       ¶¶¶¶¶¶¶       ¶¶ 
 ¶¶              ¶                    ¶¶ 
  ¶   ¶¶¶¶¶¶¶¶¶¶¶¶                   ¶¶ 
  ¶¶           ¶  ¶¶                ¶¶ 
  ¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶            ¶¶
                  ¶¶¶¶¶¶¶¶¶¶¶
                  PS: Han Solo dies, by his son Ben Solo. 
                  Dumbledore dies.
                  Master Jariya dies.
                  The Matrix is just a computer program.
                  :)    
    '''
        sys.exit(0)

    if command in ['q', 'exit', 'quit']:
        print 'You beat yourself to death'
        print '''
\x1b[31m                            ,--.   \x1b[0m
\x1b[31m                           {    }  \x1b[0m
\x1b[31m                           K,   }  \x1b[0m
\x1b[31m                          /  ~Y`   \x1b[0m
\x1b[31m                     ,   /   /     \x1b[0m
\x1b[31m                    {_'-K.__/      \x1b[0m
\x1b[31m                      `/-.__L._    \x1b[0m
\x1b[31m                      /  ' /`\_}   \x1b[0m
\x1b[31m                     /  ' /        \x1b[0m
\x1b[31m             ____   /  ' /         \x1b[0m
\x1b[31m      ,-'~~~~    ~~/  ' /_         \x1b[0m
\x1b[31m    ,'             ``~~~  ',       \x1b[0m
\x1b[31m   (                        Y      \x1b[0m
\x1b[31m  {                         I      \x1b[0m
\x1b[31m {      -                    `,    \x1b[0m
\x1b[31m |       ',                   )    \x1b[0m
\x1b[31m |        |   ,..__      __. Y     \x1b[0m
\x1b[31m |    .,_./  Y ' / ^Y   J   )|     \x1b[0m
\x1b[31m \           |' /   |   |   ||     \x1b[0m
\x1b[31m  \          L_/    . _ (_,.'(     \x1b[0m
\x1b[31m   \,   ,      ^^""' / |      )    \x1b[0m
\x1b[31m     \_  \          /,L]     /     \x1b[0m
\x1b[31m       '-_~-,       ` `   ./`      \x1b[0m
\x1b[31m          `'{_            )        \x1b[0m
\x1b[31m              ^^\..___,.--`        \x1b[0m
      '''
        sys.exit(0)
    elif command in ["save"]:
        save()
    elif command in ["load"]:
        load()
    
    if command in movement:
        try:
            node.move(command)
        except:
            print 'You can\'t go that way.'

    if node == Basement:
        time.sleep(1)
        #print 'Man in corner: H..He..Hello?'
        #print 'Is someone there?'
            
    if node == Closet_Door:
        if command == 'use':
            node = Closet
    
    if node == Mystery_Door:
        if command == '196917':
            time.sleep(2)
            print '-------------------------------------------------------'
            print 
            print 'The door unlocks. You slowly open the door and all you see in the dark room are to glowing pair of eyes standing at the end of room. They slowly approach you...getting closer..and...closer.'
            print 
            print 'Part 2....Fin'
            print 'To Be Continued...'
            print 
            print '-------------------------------------------------------'
            sys.exit(0)
            

                
    if node == Shack:
        if command == 'south':
            print 'The door seems to be jammed and won\'t open.'
            
    if node == Closet:
        note = '''
             ______________
            |              |
            |              |
            |              |
            |              |
            |     1969     |
            |              |
            |              |
            |              |
            |______________|
        '''
        if command == 'read':
            print '''
             ______________
            |              |
            |              |
            |              |
            |              |
            |     1969     |
            |              |
            |              |
            |              |
            |______________|
            '''
            #print 'Type "add" to put in inventory.'
            #if command == 'add':
            #    inventory.append('note')
    
    if node == Bathroom:
        k = 0
        if k == 1:
            print 'You already picked it up.'
        else:
            if command == 'pick up':
                print 'You picked up a key. May need it later'
                inventory.append('key')
                k = k + 1            
                print inventory
            
            
        
        
    if node == Front_Room:
            print
            print 'You go down the stairs as fast as you can.\
    As you\'re going towards the door your hit on the back of your head.\
    You fall to the floor and start losing conscious.\
    Before you lose conscious you see a blurry figure standing above you.'
            print
            dog + 1
            break
            #node = Cemetary
    

        
    if node == Outside_D:
        print node.name
        print 
        print 'You jumped and were impaled by a old rusty fence pole.'
        print node.description
        print '''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
        '''
        sys.exit(0)
    
    
    if node == Cemetary:
            print node.name
            print '-------------------------------------------------------'
            print
            print 
            print 'You awake in a coffin in a cemetary, when you get up you notice a shovel in a pile of dirt. It\'s a foggy night and you can mostly just see trees that surround you. As you look around you can see light coming from somewhere in front of you.'
            print
            print 
            print '-------------------------------------------------------'
    
            
    if node == Coffin:
            print node.name
            print
            print 'You tried to retrace your steps and as your walking you trip on a root and hit your head on a gravestone'
            print 'You died.'
            sys.exit(0)

    if node == Light:
            #time.sleep(4)
            print node.name
            print '-------------------------------------------------------'
            print 
            print 'You start walking towards the light. The light flickers and you see a man in black standing and staring at you with something in his hand. The light flickers again and he\'s gone. You look around to see where he could have gone and don\'t see anything.'
            print 
            print 'Part 1....Fin'
            print 
            print '-------------------------------------------------------'
            time.sleep(4)
            node = Cityburg
            
    if node == Cityburg:
            time.sleep(6)
            print node.name
            print 'Part 2'
            print '-------------------------------------------------------'
            print
            print '\x1B[3mGary The Bus Driver:\x1B[23m Look who\'s finally awake.'
            time.sleep(2)
            print 'You: Ww..ww..what?'
            time.sleep(2)
            print 'You: Where am I?'
            time.sleep(2)
            print '\x1B[3mGary:\x1B[23m Uhh on a bus, not very observant are you?'
            time.sleep(2)
            print 'You: How did I get here?'
            time.sleep(2)
            print '\x1B[3mGary:\x1B[23m Don\'t know, you were here when I got here.'
            time.sleep(2)
            print '\x1B[3mGary:\x1B[23m Tried waking you but you wouldn\'t budge.'
            time.sleep(2)
            print 'You: Didn\'t bother getting help? I could have been dead!'
            time.sleep(2)
            print '\x1B[3mGary:\x1B[23m Well, believe it or not you aren\'t the first person who was passed out on my bus.'
            time.sleep(2)
            print 'You: Where are we heading?'
            time.sleep(2)
            print '\x1B[3mGary:\x1B[23m Citysburg! The best smallest city there is.'
            time.sleep(2)
            print 'You: Citysburg? Never heard of it.'
            time.sleep(2)
            print '\x1B[3mGary:\x1B[23m Well, i\'m making my first stop so it\'s probably best if you get off.'
            time.sleep(2)
            print 'You: Ok.'
            time.sleep(1)
            print 'Well here\'s your stop.'
            node = Bus_Stop
            
            print
            print '-------------------------------------------------------'
#print "\x1B[3mHello World\x1B[23m"       


time_start = time.time()
seconds = 0
minutes = 0
Clock = True

while Clock:
    try:
        sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start) - minutes * 60
        if seconds >= 60:
            minutes += 1
            seconds = 0
    except KeyboardInterrupt, e:
        break
    if seconds == 11:
        Clock = False

if Clock == False:
    print 'To Continue playing the game press "c" to exit demo press "q"'

play()