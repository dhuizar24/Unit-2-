#text Monster Game

#Map of dungeon
from operator import inv


dungeon = [ 
['prize', 'boss monster', 'sword', 'sword', 'stairs down'],
['magic stones', 'monster', 'stairs down', 'sword', 'stairs up'],
['empty', 'sword', 'stairs up', 'monster', 'empty']
]

#player info
inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]

game_over = False
#game loop
while game_over == False:
    #update location 
    location = dungeon[current_floor][current_room]

    
    if location == 'empty':
            print("You are in an empty room")
    elif location == 'sword': 
            print("You see sword.")
    elif location == 'stairs up':
        print("You see some stairs leading up")
    elif location == 'stairs down':
        print("You see some stairs leading down")
    elif location == 'monster':
        print("You see a scary monster")
    elif location == 'magic stones': 
            print("You see magic stones")
    elif location == 'boss monster':
            print("You found the boss monster.")
    else: 
        print("You found the prize!")

        #player choices
    player_choices= input("What would you like to do?) (left, right, up, down, grab, fight)")
    print(player_choices)

    if player_choices == 'right':
        current_room += 1
        if current_room == 6:
            print("You can't go any further in that direction.")
            current_room = 5

    elif player_choices == 'left':
        current_room -= 1 
        if current_room == -1:
            print("You can't go any further in that direction.")
            current_room = 0 
    
    elif player_choices == 'down':
        if location == 'stairs down':
            current_floor += 1
        if current_floor == 3:
            print("You can't go any further in that direction")
            current_floor = 2
        else: 
            print("There are no stairs down")
    
    
    elif player_choices == 'up':
        if location == 'stairs up':
            current_floor -= 1
        if current_floor == -1:
            print("You can't go any further in that direction")
            current_floor == 0 
        else: 
            print("There are no stairs up")

    elif player_choices == 'grab':
        if location == 'sword' or location == 'magic stones':
            inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'monster' or location == 'boss monster':
            print("Good luck grabbing a monster")
            
        else:
            print("Nothing to grab")
        
       
     
    
    elif player_choices == 'inventory': 
        print("You have:")
        print(' '.join(inventory)) #joins every item from list with a space
    
    elif player_choices == 'fight':
        pass 

    if location == 'monster':
        if 'sword' in inventory: 
            print("Monster has been slayed")
            dungeon[current_floor][current_room] = 'empty'
            inventory.remove('sword')
            
        else: 
            print("You need a sword to fight the monster")
            game_over = True
    elif location == 'boss monster':

        if 'sword' in inventory and 'magic stones' in inventory:
            print('Victory Achieved')
            inventory.remove('sword')
            inventory.remove('magic stones')
            dungeon[current_floor][current_room] = 'empty'
    
        else:
            print("You need a sword and magic stones to fight the monster")
            game_over = True
    
# determine win/loss
if game_over == True:
    print("You died")
else:
    print("Award achieved")


    
