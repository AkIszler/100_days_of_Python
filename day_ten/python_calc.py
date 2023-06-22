import time

print("################################")
print("")
print("############Py-Calc#############")
print("")
print("################################")
keepGoing = True
while keepGoing == True:
    def add_numb(x , y ):
        answer = x + y 
        return answer

    def sub_numb(x , y):
        answer = x - y
        return answer

    def mul_numb(x , y):
        answer = x * y
        return answer

    def div_numb(x , y):
        answer = x / y
        return answer

    whatToDo = input("what you would like to do? +,-,/-* \n")

    num1 = int(input("pick your first number \n"))
    num2 = int(input("pick your second number \n"))

    print("hum, your answer is....")
    time.sleep(1)
    if whatToDo == "+":
        print(add_numb(num1, num2))
    elif whatToDo == "-":
        print(sub_numb(num1, num2))
    elif whatToDo == "*":
        print(round(mul_numb(num1, num2),2))
    elif whatToDo == "/":
        print(round(div_numb(num1, num2),2))
    else:
        print("Thats not a valid input")                      

    time.sleep(1.5)
    goAgain = input("Do you want to go again? y/n \n")

    if goAgain == "n":
        break
    else:
        keepGoing = True