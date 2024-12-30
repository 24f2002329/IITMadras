
# Week 2 Graded Programming Assignment 4
# The Question
'''
Problem Type: Standard Output - Standard Output

You are tasked with creating a multi-purpose application that performs various operations based on user input. 
The application should take the operation name from the input and execute the corresponding task.

The operations your application should support are as follows:

Odd number checker: Check whether the input number is odd.
Name: odd_num_check
Inputs: number:int
Output: "yes" if the number is odd, "no" otherwise.
Perfect square checker: Check whether the input number is a perfect square.
Name: perfect_square_check
Inputs: number:int
Output: "yes" if the number is a perfect square, "no" otherwise.
Vowel checker: Check if a string has a vowel in it.
Name: vowel_check
Inputs: text:str
Output: "yes" if the string contains a vowel, "no" otherwise.
Divisibility checker: Check if a number is divisible by 2 or 3.
Name: divisibility_check
Inputs: number:int
Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.
Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
Name: palindrominator
Inputs: text:str
Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)
Simple interest calculator with inputs with a higher interest rate if long term.
Name: simple_interest
Inputs: principal_amount:int, n_years:int (number of years)
Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
If the operation name is not any of the above print "Invalid Operation".

Problem Type: Standard Input - Standard Output

Instructions on how to solve (Click to expand)
NOTE: In this type of questions you have to read input from standard input(stdin) using input function in an appropriate manner and print the output in the appropriate format using print function.

The Three dots (...) called as Ellipsis in python are like placeholders, replace them with your answer.

Each testcase will have the standard input and expected output your program should read the standard input and print the result to the standard output matching the expected output.
'''



import math as m
Operation_name = input()

if Operation_name == "odd_num_check":
    number = int(input())
    if number % 2 != 0:
        print("yes")
    else:
        print("no")
elif Operation_name == "perfect_square_check":
    number = int(input())
    if m.sqrt(number) == int(m.sqrt(number)):
        print("yes")
    else:
        print("no")
elif Operation_name == "vowel_check":
    text = input()
    if 'a' in text or 'e' in text or 'i' in text or 'o' in text or 'u' in text or 'A' in text or 'E' in text or 'I' in text or 'O' in text or 'U' in text:
        print("yes")
    else:
        print("no")
elif Operation_name == "divisibility_check":
    number = int(input())
    if number % 2 == 0 and number % 3 == 0:
        print("divisible by 2 and 3")
    elif number % 3 == 0:
        print("divisible by 3")
    elif number % 2 == 0:
        print("divisible by 2")
    else:
        print("not divisible by 2 and 3")
elif Operation_name == "palindrominator":
    text = input()
    print(text[0:len(text)-1] + text[::-1])
elif Operation_name == "simple_interest":
    principal_amount = int(input())
    n_years = int(input())
    if n_years < 10:
        print(round(principal_amount*0.05*n_years))
    else:
        print(round(principal_amount*0.08*n_years))
else:
    print("Invalid Operation")
    
