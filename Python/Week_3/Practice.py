# n = int(input("Enter a number: "))
# i, fact = 1,1
# while i <= n:
#     fact *= i
#     print("factorial of",i,"is:",fact)
#     i += 1

# print(f"Factorial of {n} is: {fact}")



# n = input("Enter a number: ").strip()

# # Handle empty input
# if not n:
#     print("No. of digits: 0")
#     exit()

# # Handle negative numbers
# is_negative = n[0] == '-'
# if is_negative:
#     n = n[1:]

# # Remove leading zeros
# n = n.lstrip('0')

# # Handle the case where the number is zero
# if not n:
#     n = '0'
# count = len(n)

# print(f"No. of digits: {count}")


# Task 1:
# Take user inputs of name, age and favorite color and print the Output like given below - 
# Hello, John! You are 25 years old, and your favorite color is blue.
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: ")) 
fav_color = input("Enter Your Favorite color: ")
print(f"Hello, {name}! You are {age} years old, and your favorite color is {fav_color}.")


# Task 2: Number Formatting
# Write a program that prints the following information about a product using formatted output:

# Product name: "Laptop"
# Price: 999.99
# Discount: 5%

# The output should look like this:
# Product: Laptop
# Price: $999.99
# Discount: 5%

print("Product Name: Laptop","Price: $999.99","Discount: 5%", sep='\n')