#these lessons were done on a different website, so this is just some practice code

def dosomething():
    print("I did something")
    
keep_going = False
while keep_going == False:    
    something = input("do you want to do something? \n")

    if something == 'y':
        dosomething()
    elif something == 'n':
        print("okay byyyyye")
        keep_going = True   
    else:
        print("that didnt seem to mean anything... bye now")
        
        
def find_z(x, y):        
    z = (x - y) * 2
    z % 2 == z + 1
    print(f"z would be {z}")
def add_number(x,y):
    answer = x + y
    print(f"the answer is {answer}")
    
    
x_choice = int(input("give me a number \n"))
y_choice = int(input("give me another number \n"))

add_number(x_choice,y_choice)
    
find_z(x_choice,y_choice)            