# # Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
# from os import link


with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while ...: # the terminal condition
        ... # add n to the total
        ... # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while ...: # repeat forever since we are breaking inside
        line = input()
        if ...: # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = ... # convert to ints
        ... # accumulate the total price
    print(total_price)

# Filtering - Selecting based on a criterion
# only_ed_or_ing: Continuously read strings from standard input until you encounter the word "STOP" (case insensitive and not included in the output).
# Print only those strings that end with "ed" or "ing" (case insensitive).
# reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output).
# Print only those integers for which the sum of the number and its reverse is a palindrome.

elif task == "only_ed_or_ing":
    while True:
        string = input()
        if string.lower() == "stop":
            break
        if string.lower().endswith("ed") or string.lower().endswith("ing"):
            print(string)

elif task == "reverse_sum_palindrome":
    stored = []
    while True:
        num = input()
        if int(num) == -1:
            break
        sum_of_num = int(num) + int(num[::-1])
        if sum_of_num == int(str(sum_of_num)[::-1]):
            stored.append(num)
    i = 0
    while i<len(stored):
        print(stored[i])
        i += 1
# Mapping - Applying the same operation to different items
# double_string: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.
# odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output).
#  Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.


elif task == "double_string":
    while True:
        string = input()
        if string == "":
            break
        print(string*2)

elif task == "odd_char":
    s = ""
    while True:
        string = input()
        s += "".join(string[1::2]) + " "
        if string.endswith("."):
            s = s.strip()
            break
    print(s)

# Filter and Map - Applying an operation to selected items
# only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. 
# Print the square of each number only if it is even.

elif task == "only_even_squares":
    while True:
        num = input()
        if num == "NAN":
            break
        if int(num) % 2 == 0:
            print(int(num)**2)     

# Filter and Accumulate - Accumulating a result with selected items
# only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. 
# Create a string by prepending only the odd lines (starting from 1) with a newline character in between, 
# and print the result which will be the odd lines in reverse order.

elif task == "only_odd_lines":
    s = ""
    while True:
        string = input()
        if string == "END":
            break
        s += string + "\n"
    s = s.strip().split("\n")
    i = 0
    s_final = []
    while i<len(s):
        s_final.append(s[i])
        i += 2
    j = 1
    while j <= len(s_final):
        print(s_final[-j])
        j += 1