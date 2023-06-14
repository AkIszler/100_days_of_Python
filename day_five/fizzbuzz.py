#this is just a fizz buzz program

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 3 == 0:
        print("Buzz")
    else:
        print(i)        
        
        
        
