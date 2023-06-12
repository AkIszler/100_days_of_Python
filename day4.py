import random 


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = len(names)

picked_number = random.randint(0, x -1)

who_pays = names[picked_number]

total_bill = float(input("what is your total bill? \n$"))
total_people = x - 1
tip_amount = int(input("how much you want to tip? \n"))

tipped_bill = float(((tip_amount / 100)) + 1) * total_bill

print(f"{who_pays} foots the bill")
print(f"they will pay ${tipped_bill}")

