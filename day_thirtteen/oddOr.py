## in this excerise I need to take the code provided, fix it and make it loopable
#----------------------------------------------------------------
#code provided in comment
# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
#----------------------------------------------------------------  
import time #for fake loading delay, not needed



while True: #using generic boolean to start looping
    #code provided
    number = float(input("Which number do you want to check?\n")) # set to float incase user wants to use one, no output
    #of number is needed on the console so not need to keep it and int or round() the number 
    #fixed if statement with "==" so it will work correctly
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

    while True: #nested loop to allow the user to keep using the first loop iteration, uses break statement to close
        #the loop, and the exit() function to end the program on quit.
        going_check = input("Do you want to keep checking? (y/n): \n") #this is to see if user wants to keep checking
        lcheck = going_check.lower()

        if lcheck == "y":   #lcheck is to force a lowercase char to prevent confusion.
            break
        elif lcheck == "n":
            print("thank you for using the program")
            time.sleep(1) # uses the sleep function to simulate the closing of the program.
            exit()    #kills program to end both loops and allows the user to leave
        else:
            print("thats an invalid selection, please try again") # this along with the loops will allow the user to keep going
            # in case they accidentally use a non "y / n" selection, if invalid charaters used, it will reask the user for a 
            # valid selection


#KEYNOTE: 
# This lesson section was mostly about how to debug programs, and it was mostly theory So i used this broken code
# as a chance to make a more useable solution.         