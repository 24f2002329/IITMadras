# WEEK01_GRPA01

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = 5
b = 6
price, discount_percent = 80, 5.75
total_mins = 470
# <eoi>

output1 = int(a+b) # int: sum of a and b
output2 = int(2*(a+b)) # int: twice the sum of a and b
output3 = int(abs(a-b)) # int: absolute difference between a and b
output4 = int(abs((a+b)-(a*b)))  # int: absolute difference between sum and product of a and b

# Find discounted price given price and discount_percent
# input variables : price: int, discount_percent: float
discounted_price = price - (price * (discount_percent / 100)) # float

# Round the discounted_price
rounded_discounted_price = int(discounted_price) # int

# Find hrs and mins given the total_mins
# input variables : total_mins
hrs = int(total_mins//60) # int: hint: think about floor division operator
mins = int(total_mins%60) # int


print(output1, output2, output3, output4, discounted_price, rounded_discounted_price, hrs, mins, sep=', ')
