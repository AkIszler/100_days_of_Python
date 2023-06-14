
#this is how I did it by myself without the prompt
total = 0
for i in range(0,101):
    if i % 2 == 0:
        total += i
print(total)        

#how its taught by the bootcamp. both are valid, but who did it better I wonder...
even_sum = 0
for number in range(2, 101, 2):
  # print(number)
  even_sum += number
print(even_sum)     

