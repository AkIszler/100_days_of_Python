import os
import time
import random
################SCOPE################

enemies = 1
bullets = random.randint(1,10+enemies)
def increaseEnemies():
    # this will print 2 because its inside the scope of the function
    enemies = 2
    print(f"enemies inside the function {enemies}")

#calls function
increaseEnemies()
#this will print 2 because its inside the scope of the function
#but below will print 2 because its the global scope of the program
print(f"enemies outside the function {enemies}")    

#data inside functions will stay set inside the function while global(outside functions) will retain
#thier global information unless changed.

#example of a function changing a global variable
def add_more(enemy, added):
    
    new_amount = enemy + added
    return new_amount

def enemy_killed(enemy, killed_enemy):
    enemy = enemy - killed_enemy
    return enemy

print(f"The {enemies} enemy has called for backup.\n")
added = int(input("how much backup did they call? \nthey can call up to 9 more people \n"))

os.system("clear") # used to clear temrminal to make the info easier to read


demo = add_more(enemies, added)

#this below is for fun
print("adding enemies...")
time.sleep(0.5)
print("adding....")
time.sleep(0.5)
print("ememies added...")
time.sleep(0.5)

print(f"you now have {demo} enemies")

killed = bullets
print(f"you have {bullets} bullets in your gun\n")
killed_ememies = enemy_killed(demo, killed)
print("killing ememies")
time.sleep(1)
print("...")
time.sleep(1)

remaining = demo - bullets

if killed_ememies == demo:
    print(f"you had {demo} enemies and you have {bullets} in your gun\nyou killed all of them")
elif killed <= demo:
    print(f"you had {demo} enemies and you have {bullets} in your gun\nyou killled all but {remaining} of them\nsorry you lose! ")
else:
    print(f"you have {bullets} in your gun, and only {demo} enemies\nso you had plenty of ammo and killed all of them")



# add_more takes the intial number in emenies (which is 1) and adds the "add enemy" input
# so if you were to make "added" 6 the function would add 6 enemies to 1 enemies and make 7
# with "add_more"  function you can change a global variable (enemies)
# and with enemy_killed you can change the global variable (enemies) 
