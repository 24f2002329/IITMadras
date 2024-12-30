# Practice Assignment Week 1 Question No: 1,2,3

# The Questions Of PA 1

# # print(1 2 3 4 5)
# print("a + 'b' + c + '' + d")
# print('1 2 3 4 5') # there is a space between consecutive numbers

# Practice Assignment Week 1 Question No: 4
# Feedback:
# The division operation will always produce a float value irrespective of the operands involved. For example, in the expression a / b, even if a and b are integers such that a is divisible by b, the result will still be a float. Try out the following in your interpreter:

# print(10 / 5) # Output = 2.0
# For any arithmetic operation, even if one of the operands is float, the resulting value is a float. For example, try out the following in your interpreter:

# print(10 // 5) # Output = 2
# print(10.0 // 5) # Output = 2.0
# print(10 // 5.0) # Output = 2.0


# Practice Assignment Week 1 Question No: 5
# word = "hello"
# # new_word = word[0] + word[-1]
# new_word = word[0] + word[len(word)-1]
# print(new_word)

# Practice Assignment Week 1 Question No: 6

# x = int(input())
# y = int(input())
# z = int(input())
# avg = (x + y + z) / 3
# print(avg)
# Note: The Quotient is always a floating point number.

# Practice Assignment Week 1 Question No: 7
# w1 = input()
# w2 = input()
# print(w1 + w2) # concatenation of two strings gives Output = 1020
# print(int(w1) + int(w2)) # addition of two strings gives Output = 30
# w1 = int(input())
# w2 = int(input())
# print(w1 + w2) # addition of two integers gives Output = 30


# Practice Assignment Week 1 Question No: 8
# print(2**3**0) # Output = 2 Python paran
# and the python paranthesizes the code as (2**(3**0)) = 2**1 = 2







# Imp Questions!


# GA Q-4
# Q - 2 points E_1 and E_2 are Boolean values. Consider the following expression.
# 1 E_3 = not (E_1 or E_2) 
# 2 E_4 = (not E_1) and (not E_2) 3 print(E_3 == E_4)
# What can you say about the value printed by the code given above?

# It is True if and only if both E_1 and E_2 have the same value.
# It is False if and only if both E_1 and E_2 have the same value.
# It is always True.
# It is always False.

# Soln:

# Let's analyze the given expressions step-by-step:

# E_3 = not (E_1 or E_2)

# This expression uses the or operator and then negates the result.
# According to De Morgan's laws, not (E_1 or E_2) is equivalent to (not E_1) and (not E_2).
# E_4 = (not E_1) and (not E_2)

# This expression directly applies De Morgan's law.
# print(E_3 == E_4)

# This prints whether E_3 is equal to E_4.
# Since E_3 and E_4 are equivalent due to De Morgan's laws, the expression E_3 == E_4 will always be True regardless of the values of E_1 and E_2.

# Therefore, the value printed by the code is always True.

# The correct answer is: it is always True.


# GA Q-5
# E is a boolean variable. Consider the following sequence of expressions:

# 1 not E 2 not not E 3 not not not E 4 not not not not E 5 . 6 . 7 .

# This pattern keeps repeating for a thousand lines. If line number 500 evaluates to False, what is the value of E?

# True

# False

# Cannot be determined

# Soln:
# Let's analyze the given sequence of expressions:
# Given the sequence:

# not E
# not not E
# not not not E
# not not not not E
# ...
# We need to determine the value of E if line number 500 evaluates to False.

# Explanation:
# Odd-numbered lines apply not an odd number of times.
# Even-numbered lines apply not an even number of times.
# If line number 500 evaluates to False, it means:

# Line 500 is an even-numbered line.
# Applying not an even number of times results in the original value of E.
# Thus, if line 500 evaluates to False, E must be False.

# Illustration with Code:
# # Example to illustrate the pattern
# E = False

# # Line 1: not E
# line_1 = not E
# print(f"Line 1: {line_1}")  # Output: True

# # Line 2: not not E
# line_2 = not not E
# print(f"Line 2: {line_2}")  # Output: False

# # Line 3: not not not E
# line_3 = not not not E
# print(f"Line 3: {line_3}")  # Output: True

# # Line 4: not not not not E
# line_4 = not not not not E
# print(f"Line 4: {line_4}")  # Output: False

# # Line 500: not applied 500 times (even number)
# line_500 = E
# print(f"Line 500: {line_500}")  # Output: False


# Conclusion:
# If line number 500 evaluates to False, the value of E must be False.

# The correct answer is: False.


# # GA Q-6,7
# # Common Data for questions (6) and (7)

# # Consider the following string:

# word = '138412345678901938'

# # For what values of a and b does the following expression evaluate to True? Assume that both a and b are positive integers.

# word[a : b] == '123456789'

# # Enter the value of a. (NAT)
# # Ans = 4 # 4th index is 1

# # Enter the value of b.
# # Ans = 13 # since 2nd argument is exclusive so 13-1 = 12th index is 9


# GA Q-8

# We need to write a program that performs this task: accept two names (strings) as input. Print True if the first name comes before the second in alphabetical order, and False otherwise. Sample test cases:

# Input	         Output
# sachin, rohit	  False
# saina, sindh    True
# For example, sachin comes after rohit, so the expected output is False. Assume that all names consist of just one word and will be entered in lower case during the time of input. Select all correct implementations of this program.

# Soln:
# Let's analyze the given problem statement:
# We need to write a program that accepts two names as input and prints True if the first name comes before the second in alphabetical order, and False otherwise.
# The names will be entered in lowercase.
# We can compare the names directly using the less than operator (<) to check the alphabetical order.
# Let's consider the given test cases:
# Test case 1: sachin, rohit
# The name sachin comes before rohit in alphabetical order.
# The expected output is False.
# Test case 2: saina, sindh
# The name saina comes before sindh in alphabetical order.
# The expected output is True.
# Implementation:
# We can implement the program as follows:

# # Accept two names as input
# name1 = input()
# name2 = input()
# print(name1 < name2)  # Check if name1 comes before name2 in alphabetical order

# The program compares the two names directly using the less than operator (<) to check the alphabetical order.
# If name1 comes before name2, it prints True; otherwise, it prints False.


# A detailed explaination of the code is given below:

# Code Explanation:
# # Accept two names as input
# name1 = input()
# name2 = input()
# print(name1 < name2)  # Check if name1 comes before name2 in alphabetical order

# Why Use < Instead of > ? 
# Alphabetical Order Check:

# The < operator checks if name1 comes before name2 in alphabetical order.
# For example, if name1 is "sachin" and name2 is "rohit", the expression name1 < name2 evaluates to False because "sachin" does not come before "rohit" alphabetically.
# Desired Output:

# The goal is to determine if name1 should appear before name2 in a sorted list.
# Using < directly aligns with this goal. If name1 is alphabetically less than name2, it means name1 should come first.
# Using >:

# If you used the > operator, it would check if name1 comes after name2 in alphabetical order.
# This would reverse the logic. For example, name1 > name2 would be True if "sachin" comes after "rohit", which is not what we want to check.
# Example
# Let's consider the provided test cases:

# Test Case 1: name1 = "sachin", name2 = "rohit"

# name1 < name2 evaluates to False because "sachin" does not come before "rohit".
# name1 > name2 would evaluate to True, but this is not the check we need.
# Test Case 2: name1 = "saina", name2 = "sindh"

# name1 < name2 evaluates to True because "saina" comes before "sindh".
# name1 > name2 would evaluate to False, which is not useful for our purpose.
# Conclusion
# Using the < operator directly checks if the first name should come before the second name in alphabetical order, which is the intended functionality. Using > would invert this logic and not provide the correct result for the given problem.

# print(input() < input())

# name1 = input()
# name2 = input()
# result = name1 < name2
# print(result)

# GA Q-9

# x = 2 ** 5
# x1 = x // 2
# x2 = x1 // 2
# x3 = x2 // 2
# x4 = x3 // 2
# x5 = x4 // 2
# print(x1 + x2 + x3 + x4 + x5)

# Code Explanation:
# Certainly! Let's break down the code step by step:

# ### Code Explanation

# 1. **Exponentiation**:
#     ```python
#     x = 2 ** 5
#     ```
#     - `2 ** 5` means 2 raised to the power of 5.
#     - This results in [`x`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A248%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") being `32` because \(2^5 = 32\).

# 2. **Integer Division**:
#     ```python
#     x1 = x // 2
#     ```
#     - [`x // 2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A248%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") performs integer division of [`x`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A248%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") by 2.
#     - Since [`x`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A248%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") is `32`, [`x1`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A249%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") becomes `16`.

# 3. **Subsequent Integer Divisions**:
#     ```python
#     x2 = x1 // 2
#     x3 = x2 // 2
#     x4 = x3 // 2
#     x5 = x4 // 2
#     ```
#     - Each line performs integer division of the previous result by 2.
#     - [`x2 = 16 // 2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A250%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") results in `8`.
#     - [`x3 = 8 // 2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A251%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") results in `4`.
#     - [`x4 = 4 // 2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A252%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") results in [`2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A248%2C%22character%22%3A4%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition").
#     - [`x5 = 2 // 2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A253%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") results in `1`.

# 4. **Summation and Output**:
#     ```python
#     print(x1 + x2 + x3 + x4 + x5)
#     ```
#     - This line sums up all the variables [`x1`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A249%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition"), [`x2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A250%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition"), [`x3`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A251%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition"), [`x4`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A252%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition"), and [`x5`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A253%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition").
#     - The sum is `16 + 8 + 4 + 2 + 1`, which equals `31`.
#     - The [`print`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fdevendra%2FPython%20IITM%2FWeek%201%2FPA_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A254%2C%22character%22%3A0%7D%7D%5D%2C%224fba1ca3-a13d-4182-ab9c-268d4db17b38%22%5D "Go to definition") function outputs `31` to the console.

# ### Summary
# The code calculates the sum of a series of integer divisions starting from \(2^5\) and repeatedly dividing by 2. The final result printed is `31`.

# ### Potential Improvements
# - **Readability**: Using a loop or list comprehension could make the code more concise and easier to maintain.
# - **Scalability**: If the number of divisions changes, a loop would be more flexible.

# Here's an example using a loop:

# ```python
# x = 2 ** 5
# result = 0
# for _ in range(5):
#     x //= 2
#     result += x
# print(result)
# ```

# This code achieves the same result but is more scalable and easier to understand.




