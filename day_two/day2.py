#tip calculation program
#used to learn f strings, math and input manipulation

print("welcome to the Tip calculation program")
total_bill = float(input("what is your total bill? \n$"))
total_people = int(input("how many people are eating? \n"))
tip_amount = int(input("how much you want to tip? \n"))

tipped_bill = float(((tip_amount / 100)) + 1) * total_bill
share_amount = round(tipped_bill / total_people, 2)
#testing math
#print(share_amount)

print(f"It looks like each person owes ${share_amount} if the bill is ${total_bill} and the tip it {tip_amount}%")
print(f"your total bill with tip is ${tipped_bill} in case you wanted to know!")