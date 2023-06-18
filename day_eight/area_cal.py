#a can of paint can cover 5 square feet of area
# calulates the total amoount of cans of paint youd need to paint
import math

def area_of_paint(x_axis, y_axis, can_cover):
    area_of_paint = x_axis * y_axis 
    can_amount = can_cover 
    number_of_cans = math.ceil(area_of_paint / can_cover) 
    
    return number_of_cans
     

height = int(input("how tall is your wall in feet?:\n"))
width = int(input("what is the length of your wall?: \n"))
can_cover = int(input("how much can a single can cover?: \n"))

paint_needed = area_of_paint(height, width, can_cover)

print(f"you will need at least {paint_needed} to safely cover the wall")


