import random 
import time

def random_seed(seed):
    seed = random.randint(1000000, 9999999)
    print('generating random seed...')
    time.sleep(1)
    print("please wait...")
    time.sleep(3)
    
def player_name():
    running = True
    while running == True:
        player = input("what is your players name? \n")
        print(f"you choice {player}")
        is_good = input("is this correct y/n \n")
        is_good = is_good.lower()
        if is_good == 'y':
            print("okay perfect")
            break
        elif is_good == 'n':
            running = True
        else:
            print("not a valid input")
            running = True    
    return player
seed = 0

def player_race():
    races_list = ["orc", "elf", "human", "seakin", "goblin", "halflings"]
    print("pick a player race")
    
    for race in races_list:
        print(f"{race}")
    
    race_pick = input("pick a player race from the list above: ")
    
        
    
    

#random_seed(seed)
player = player_name()
player_race()
