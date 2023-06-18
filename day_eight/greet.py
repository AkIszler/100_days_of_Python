# base idea of a function using inputs to get data
#def greeting(): 
#    print("hello welcome")
#    name_of = input("What is your name? \n")
#    area_of = input("where do you live? \n")
#    print(f"greetings {name_of}, how is the weather in {area_of}")

#greeting()    

#a function using preset data or info into the fucntion from someone else in the program
name = input("Name of user: ")
area = input("Area of user: ")

def greeting_more(name_of: str, area_of: str) -> None:
    print(f"greetings {name_of}")
    print(f"how is the weather in {area_of}, {name_of}?")

    
greeting_more(name,area)    

#functions like greeting_more is better because it can use data from outside the function scope to do what the 
#funtion is designed for 