# # heterogeneous - multi line
# def get_student_details():
#     '''
#     Get the student details over multiple lines

#     Input format:

#     name
#     age
#     rollno

#     Return: name:str, age:int, rollno:int
#     '''
#     name = input()
#     age = int(input())
#     rollno = int(input())

#     return name, age, rollno

# # heterogeneous - single line 
# def get_student_details_same_line():
#     '''
#     Get the student details from the same line

#     Input format:(separated by space)

#     name age rollno

#     Return: name:str, age:int, rollno:int
#     '''
#     x = input()
#     l = s.split(" ")
#     name = l[0]
#     age = int(l[1])
#     rollno = int(l[2])
#     return name, age, rollno

# # homogeneous - single line
# def get_comma_separated_integers():
#     '''
#     Get a list of comma separated integers from input

#     Return: numbers:list[int]
#     '''
#     x = input()
#     numbers = x.split(",")
#     numbers = [int(num) for num in numbers]

#     return numbers

# # homogeneous - multi-line - definite
# def get_n_float_numbers():
#     '''
#     Get n float numbers with one number in each line 
#     and the first line has n.

#     Input Format:
#     n
#     num1
#     num2
#     ...
#     numn

#     Return: nums:list[float]
#     '''
#     n = int(input())
#     nums = list()
#     while n != 0:
#         x = float(input())
#         nums.append(x)
#         n -= 1

#     return nums

# # homogeneous - multi-line - indefinite
# def get_nums_until_end():
#     '''
#     Get float numbers with one number in each line 
#     until the input is "end"(case insensitive)

#     Input Format:
#     num1
#     num2
#     ...
#     numx
#     End

#     Return: nums:list[float]
#     '''
#     nums = []
#     while True:
#         n = input()
#         if n == "end":
#             break
#         nums.append(float(n))

#     return nums

# # hybrid - single line
# def get_batsman_runs():
#     '''
#     Get batsman name, number and runs as a list

#     Input format: (separated by space)
#     name no run1 run2 run3 ...

#     Return: name:str, no:int, runs:list[int]
#     '''
#     x = input()
#     lst = x.split(" ")
#     name = lst[0]
#     no = int(lst[1])
#     runs = []
#     for i in range(2,len(lst)):
#         runs.append(int(lst[i]))

#     return name, no, runs

# # key value 
# def get_course_scores():
#     '''
#     Get course name and scores of the over multiple lines where 
#     course name and scores are separated by a hypen in each line.
#     First line corresponds to the number or entries.

#     Input format:
#     2
#     course1-score1
#     course2-score2

#     Return: dict[str,int] - with course name as key and score as value
#     '''
#     n = int(input())
#     string = ""
#     for i in range(n):
#         string += input() + "-"
#     course_list = string.split("-")
#     course_list.pop()
#     course_scores = {}
#     for i in range(0,len(course_list),2):
#         course_scores[course_list[i]] = int(course_list[i+1])

#     return course_scores

# # dict with list as values
# def get_all_batsman_runs():
#     '''
#     Given the batsman name and the comma separated runs 
#     where both are seperted by a hypen in multiple lines, 
#     create a dictionary with batsman name and list of runs as value.
#     The number of lines is given in the first line

#     Input format:
#     3
#     batsman1-1,2,1,4,6,2,2,1
#     batsman2-2,2,6,4,1
#     batsman3-6,1,2,4,4,2

#     Return: dict[str,list[int]] - with batsman name as key and list of runs as values
#     '''
#     n = int(input())
#     input_string = ""
#     for i in range(n):
#         input_string += input()+"-"
#     l = input_string.split("-")
#     l.pop()
#     batsman_runs = {}
#     for i in range(0,len(l),2):
#         batsman_runs[l[i]] = l[i+1].split(",")
#         for j in range(len(batsman_runs[l[i]])):
#             batsman_runs[l[i]][j] = int(batsman_runs[l[i]][j])

#     return batsman_runs

# # csv - list of dicts
# def get_student_marks():
#     '''
#     Given the student rollno, city, age,
#     course1_marks, course2_marks and course3_marks 
#     as comma separated values over multiple lines,
#     create a list of dict with the above attributes as keys 
#     and the corresponding value as values.
#     The number of lines is given in the first line

#     Input Format:
#     n
#     1,citya,23,86,69,86
#     2,cityb,19,78,65,89
#     ...
#     n,cityx,35,89,57,76

#     Return: 
#     student_data - list[dict]: where each dict would be 

#     {'rollno':int, 'city':str,'age':int, 
#     'course1':int, 'course2':int, 'course3':int}
#     '''
#     n = int(input())
#     data = []
#     student_data = []
#     for x in range(n):
#         _input = input()
#         data.append(_input)
#     for i in range(len(data)):
#         data[i] = data[i].split(",")
#         student_dict = {}
#         for j in range(len(data[i])):
#             student_dict["rollno"] = int(data[i][0])
#             student_dict["city"] = data[i][1]
#             student_dict["age"] = int(data[i][2])
#             student_dict["course1"] = int(data[i][3])
#             student_dict["course2"] = int(data[i][4])
#             student_dict["course3"] = int(data[i][5])
#         student_data.append(student_dict)

#     return student_data

# # list of dicts
# def get_student_data_over_multiple_lines():
#     '''
#     Given each attribute as described above in given over multiple lines 
#     and multiple entries are given create a dictionary as described above.

#     Input format:
#     n
#     1
#     citya
#     23
#     86
#     69
#     86
#     2
#     cityb
#     19
#     78
#     65
#     89
#     ...
#     n
#     cityx
#     35
#     89
#     57
#     76
#     '''
#     n = int(input())
#     data = []
#     student_data = []
#     for x in range(6*n):
#         _input = input()
#         data.append(_input)
#     for i in range(n):
#         student_dict = {}
#         for j in range(len(data[i])):
#             student_dict["rollno"] = int(data[0])
#             student_dict["city"] = data[1]
#             student_dict["age"] = int(data[2])
#             student_dict["course1"] = int(data[3])
#             student_dict["course2"] = int(data[4])
#             student_dict["course3"] = int(data[5])
#         student_data.append(student_dict)

#     return student_data

# # this will read the function name from the input.
# func = eval(input()) 

# # this will read the actual output that is required which is the second line
# expected_output = eval(input())

# # The remaining of the input should be read by your function
# actual_output = func()

# if expected_output != actual_output:
#     print("Your output doesn't match the expected output.")
# print(actual_output)



# An Algoritm for Matrix Multiplication:
# Let us define a matrix called "A"

# A = []
# B = []

# a1 = [1,2,3]
# a2 = [4,5,6]
# a3 = [7,8,9]

# b1 = [1,2,1]
# b2 = [6,2,3]
# b3 = [4,2,1]

# A.append(a1)
# A.append(a2)
# A.append(a3)

# B.append(b1)
# B.append(b2)
# B.append(b3)

# C = [[0,0,0],[0,0,0],[0,0,0]]
# dim = 3
# for i  in range(dim):
#     for j in range(dim):
#         for k in range(dim):
#             C[i][j] = A[i][k] * B[k][j]

# print(C)



"""


Implement all the given functions that are used to solve the below problems.

Follow the path

You are given a matrix of size m x n consisting of ones (1) and zeros (0). 
There is a single continuous path formed with ones that starts 
from the rightmost cell in the last row (m-th row) with 
one and ends at leftmost cell in the first row with one in it.
The path does not branch, and there is only one such path.
Your task is to traverse along the path and print the
coordinates of the path from start to end as tuples over multiple lines.
 The path can move vertically and horizontally.

Input

matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
Output

(4,1)
(4,0)
(3,0)
(2,0)
(2,1)
(2,2)
(2,3)
(1,3)
(0,3)
(0,2)
Alternate the path Same setup, but while going in that path, flip every ones in the even position in the path to 2. Modify the matrix inplace.

Output

[
    [0, 0, 2, 1],
    [0, 0, 0, 2],
    [2, 1, 2, 1],
    [1, 0, 0, 0],
    [2, 1, 0, 0]
]
Count the path Same setup, but instead of flipping put the count of the step in the path. Modify the matrix inplace.

Output

[
    [0, 0, 10, 9],
    [0, 0, 0, 8],
    [4, 5, 6, 7],
    [3, 0, 0, 0],
    [2, 1, 0, 0]
]
Mirror the path horizontally Same setup, but also add a path that is the horizontal mirror of the original path in the same matrix.

Input

[
  [0,1,0,0,0],
  [0,1,1,1,0],
  [0,0,0,1,0],
  [0,0,0,1,1]
]
Output

[
  [0,1,0,1,0],
  [0,1,1,1,0],
  [0,1,0,1,0],
  [1,1,0,1,1]
]
Mirror the path vertically Same setup, but also add a path that is the vertical mirror of the original path in the same matrix.

Input

[
  [0,1,0,0,0],
  [0,1,1,1,0],
  [0,0,0,1,0],
  [0,0,0,1,1]
]
Output

[
  [0,1,0,1,1],
  [0,1,1,1,0],
  [0,1,1,1,0],
  [0,1,0,1,1]
]

"""

# Template Code-

def index_of_first_occurance(row:list,elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    # for element in row:
    #     if element == 1:
    #         first_index = row.index(element)
    if 1 in row:
        first_index = row.index(1)
    return first_index
            

def index_of_last_occurance(row:list,elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    for i in range((len(row)-1),-1,-1):
        if row[i] == 1:
            last_index = i
            break
    return last_index

def is_valid_coordinate(x:int,y:int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''
    

def valid_adjacent_coordinates(x:int,y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
      (x1,y1)
      for x1,y1 in ... # all the possible adjacent coordinates
      if is_valid_coordinate(x1,y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''
    ...

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1,0
    y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)
    ...

def print_path(M):
    path = get_path_coordinates(M)
    ...

def alternate_path(M):
    path = get_path_coordinates(M)
    ...

def count_path(M):
    path = get_path_coordinates(M)
    ...

def mirror_horizontally(M):
    path = get_path_coordinates(M)
    ...

def mirror_vertically(M):
    path = get_path_coordinates(M)
    ...


















# Iterators and Generators in Python

# Some Problems from ChatGPT

# 1
'''

Here's a problem for you to solve that involves using **iterators,
 generators, `map()`, `reduce()`, `lambda`, `enumerate()`, and `zip()`**
   in a single program:

### Problem Statement:
You have two lists:
- `products`: a list of product names (e.g., `
['Laptop', 'Mouse', 'Keyboard', 'Monitor']`)
- `prices`: a list of corresponding prices (e.g., `[1000, 20, 50, 300]`)

**Your tasks**:
1. Create a **generator** that yields tuples containing 
   `(index, (product, price))` using `enumerate()` and `zip()`.
2. Use a **`map()` function with a `lambda`** to format the output as 
  strings: `"<index>: <product> costs $<price>"`.
3. Use **`reduce()`** to create a single string that combines all formatted
   strings, separated by newline characters.
4. Implement an **iterator class** to iterate over each formatted string.
5. Finally, iterate through the formatted strings using the custom iterator
    and print them one by one.

**Example Input**:
```python
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
prices = [1000, 20, 50, 300]
```

**Expected Output**:
```
1: Laptop costs $1000
2: Mouse costs $20
3: Keyboard costs $50
4: Monitor costs $300
```
'''
products = ["Laptop","Mouse","Keyboard","Monitor"]
prices = [80000,400,1200,7000]


from functools import reduce
# Create a **generator** that yields tuples containing `(index, (product, price))` using `enumerate()` and `zip()`.

def my_generator(products, prices):
    for index, (product,price) in enumerate(zip(products,prices),start=1):
        yield index, (product,price)

formatted_strings = map(lambda x: f"{x[0]}: {x[1][0]} costs Rs.{x[1][1]}",
                        my_generator(products,prices))

combined_string = reduce(lambda x,y: x + "\n" + y, formatted_strings)

print(combined_string)

# .............................................

# mapping
def is_greater_than_5(numbers:list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''

    return list(map(lambda x: x>5, numbers))

# filtering
def filter_less_than_5(numbers:list)->list:
    '''Given an list of numbers, return a list of numbers that are less than 5'''

    return list(filter(lambda x: x<5, numbers))

# aggregation with filtering
def sum_of_two_digit_numbers(numbers:list):
    '''Given a list of numbers find the sum of all two_digit_numbers.
    '''

    return sum(filter(lambda x: len(str(x))==2, numbers))

# aggregation with mapping
def is_all_has_a(words:list)->bool:
    '''Given a list of words check if all words has the letter a(case insensitive) in it.
    '''

    return all(map(lambda x: 'a' in x.lower(), words))

# enumerate
def print_with_numbering(items): 
    '''
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    '''

    for i, value in enumerate(items,1):
        print(f"{i}. {value}")

# zip
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    '''

    for country, capital in zip(countries, capitals):
        print(f"{country} - {capital}")

# key value list to dict
def make_dict(keys, values):
    '''Create a dict with keys and values'''

    return dict(zip(keys,values))

# enumerate with filtering and map
def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of the big words(length greater than 5).
    '''

    return list(map(
      lambda x: x[0], # taking only the indices
      filter(lambda y: len(y[1])>5, enumerate(words)) # filtering with size
    ))

# zip with mapping and aggregation
def decode_rle(chars:str, repeats:list)->str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times. 

    Note rle refers to Run-length encoding
    '''

    return "".join(map(lambda x: x[0]*x[1], zip(chars, repeats)))






def merge(D1, D2, priority):
    """
    Merge two dicts

    Arguments: 
        - D1: first dictionary
        - D2: second dictionary
        - priority: string
    Returns: D; merged dictionary
    """
    D = {}
    if priority == "first":
        D.update(D2)
        D.update(D1)
    else:
        D.update(D1)
        D.update(D2)
    return D








