#love calculator for logical statements


print("welcome to the love calculator")
name1 = input("what is your name? use your full name \n")
name2 = input("enter the full name of your crush \n")

#joins the names together to make operations easier
name_join = name1 + name2
lower_check = name_join.lower()

#adds each letter to a counter to get score
t = lower_check.count("t")
r = lower_check.count("r")
u = lower_check.count("u")
e = lower_check.count("e")

l = lower_check.count("l")
o = lower_check.count("o")
v = lower_check.count("v")
e = lower_check.count("e")

#add all numbers together to get score
true_total = t + r + u + e
love_total = l + o + v + e

#convert to concat
string_tl = str(true_total) + str(love_total)

#covert back to int for comparing
check_mark = int(string_tl)

#logic to give the score and if its good or bad!

if check_mark <= 10 or check_mark >= 90:
    print(f"Your score is {string_tl}, you go together like coke and mentos.")
elif check_mark >=40 and check_mark <= 50:
    print(f"Your score is {string_tl}, you are alright together.")
else:
    print(f"Your score is {string_tl}.")
