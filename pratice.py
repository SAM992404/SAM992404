'''veg_items = {
      "tomato" : 120,
      "orange" :  80,
      "apple"  :  70
}
user_item = input("enter an item: ").lower()

if user_item in veg_items:
    price = veg_items[user_item]
    print(f"The price of {veg_items} is ${price:}")
else:
   print(f" Sorry,{user_item} is not available.")'''



'''total=0
for num in range(1,101):
  total += num

  print("the sum of all num from 1 to 100 is:", total)'''


'''import math


radius= float(input("area of circle:"))
area = math.pi * (radius ** 2)
print(f"the area of circle with radius {radius} is {area:.2f}")'''

          
'''import math  
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is {area:.2f}")'''

'''input_string ="HELLO,SAMHITHA !"
lowercase_string= input_string.lower()
uppercase_string= input_string.upper()
print("original string:",input_string)
print("lowercase:",lowercase_string)
print("uppercase:",uppercase_string)'''


'''n = int(input("Enter the value of n: "))
even_number = 2
for i in range(n):
    print(even_number, end=" ")  
    even_number += 2  
print()'''


'''base=float(input("enter the base of the triangle: "))
height=float(input("enter the height of the triangle: "))
area=0.5 * base * height
print(f"the area of triangle with base{base} and height is {height}")'''





def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

my_list = [1, 2, 3, 4, 5, 6]
result = filter_even_numbers(my_list)
print(result)



