# Week 1 Python Concepts

# Print Function and Input Function
print("Welcome to the Week 1 Python Revision Code!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Type Conversion (input returns string, converting to int)
print(f"Hello, {name}! You are {age} years old.")  # String Concatenation and f-string for formatted output

# Datatypes: String, Integer, Floating Point, Boolean, Lists
pi = 3.14159  # Floating point number
is_adult = age >= 18  # Boolean with comparison operator
numbers_list = [1, 2, 3, 4.5, "Five", True]  # List with different data types (int, float, string, boolean)

# Type Conversion
age_str = str(age)  # Converting integer to string
pi_int = int(pi)  # Converting float to integer (truncates decimal)
is_adult_str = str(is_adult)  # Converting boolean to string

# Arithmetic Operators
sum_numbers = 10 + 5  # Addition
difference = 10 - 5  # Subtraction
product = 10 * 5  # Multiplication
quotient = 10 / 3  # Division (float result)
integer_division = 10 // 3  # Floor division (integer result)
modulus = 10 % 3  # Modulus (remainder)
power = 2 ** 3  # Exponentiation (power)

# Logical Operators and Boolean expressions
is_teenager = age >= 13 and age <= 19  # AND operator for logical comparison
is_senior = age >= 60 or age < 0  # OR operator (impossible age)
not_senior = not is_senior  # NOT operator

# Comparison Operators
is_equal = age == 18  # Equal to
is_not_equal = age != 18  # Not equal to
is_greater = age > 18  # Greater than
is_less = age < 18  # Less than

# Strings: Indexing, Slicing, Concatenation, len(), Replication, Comparison
welcome_message = "Hello, " + name + "!"  # Concatenation
first_letter = name[0]  # String indexing (first character)
last_letter = name[-1]  # Negative indexing (last character)
substring = name[1:4]  # Slicing (characters from index 1 to 3)
repeated_message = "Python " * 3  # Replication (repeat string)
name_length = len(name)  # Length of the string
is_same_name = name == "John Doe"  # String comparison

# Working with Lists: Indexing, Slicing, len(), Concatenation, Replication
first_item = numbers_list[0]  # Accessing first item in the list
last_item = numbers_list[-1]  # Accessing last item in the list
list_slice = numbers_list[1:4]  # Slicing a list (index 1 to 3)
extended_list = numbers_list + ["Six", 7.5]  # Concatenating lists
replicated_list = numbers_list * 2  # Replicating a list
list_length = len(numbers_list)  # Length of the list

# Type Checking
is_integer = isinstance(age, int)  # Checking if the variable is of type integer
is_float = isinstance(pi, float)  # Checking if pi is a float
is_string = isinstance(name, str)  # Checking if name is a string
is_list = isinstance(numbers_list, list)  # Checking if numbers_list is a list

# Final summary output with all the concepts
print("\nSummary of Concepts Covered:")
print(f"Name: {name}, Age: {age_str}, Adult: {is_adult_str}")
print(f"Arithmetic Results: Sum={sum_numbers}, Difference={difference}, Product={product}, Quotient={quotient:.2f}")
print(f"Logical Results: Teenager={is_teenager}, Senior={is_senior}, Not Senior={not_senior}")
print(f"Comparison Results: Equal to 18={is_equal}, Not Equal to 18={is_not_equal}, Greater than 18={is_greater}")
print(f"String Details: First Letter={first_letter}, Last Letter={last_letter}, Substring={substring}")
print(f"List Details: First Item={first_item}, Last Item={last_item}, Sliced List={list_slice}")
print(f"List Length: {list_length}, Concatenated List: {extended_list}, Replicated List: {replicated_list}")

# Checking data types
print(f"\nType Checks: Is Integer={is_integer}, Is Float={is_float}, Is String={is_string}, Is List={is_list}")




# -----------------------------------------------------------------------------



# Advanced Python Week 1 Revision Code

# Print Function, Input, Type Conversion
print("Advanced Week 1 Python Revision!")
name = input("Enter your full name: ")
age = int(input("Enter your age: "))  # Type Conversion

# Datatypes: String, Integer, Floating Point, Boolean, Lists
salary = float(input("Enter your monthly salary (in USD): "))  # Floating point
is_employed = age >= 18 and salary > 0  # Boolean expression
hobbies = ["Reading", "Coding", "Music", "Travelling", True]  # List with mixed data types

# Advanced Type Conversion and Operations
# Type Conversions with error handling
try:
    bonus_percentage = float(input("Enter your bonus percentage: "))  # May input non-numeric
    total_salary = salary + salary * (bonus_percentage / 100)  # Bonus calculation
except ValueError:
    print("Invalid percentage! Setting bonus percentage to 0.")
    bonus_percentage = 0.0
    total_salary = salary

# Advanced Arithmetic and Operators
# Demonstrating combined operators (+=, -=, *=, /=, **=)
total_salary += 200  # Add bonus to salary (demonstrates += operator)
total_salary **= 1.02  # Simulate a raise by a power factor (advanced exponentiation)

# Logical Operators in Complex Expressions
is_rich = total_salary > 5000 or is_employed and age >= 30
is_young_but_rich = not is_rich and age < 30

# Advanced Slicing: String Slicing (Reverse, Step, etc.)
full_name_length = len(name)
middle_name = name[1:full_name_length-1]  # Slicing out first and last letters
reversed_name = name[::-1]  # Reverse slicing using negative step
every_second_letter = name[::2]  # Advanced slicing with step
first_two_letters = name[:2]  # Simple slicing (first two letters)
last_two_letters = name[-2:]  # Slicing last two characters

# Lists: Advanced Slicing, Nesting
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, [10, 11, 12]]  # Nested list
nested_list_slice = numbers[6:10]  # Slice to get part of list [6, 7, 8, 9]
deep_nested_slice = numbers[10][1:3]  # Slicing inside nested list [11, 12]
reversed_numbers = numbers[::-1]  # Reverse slicing the entire list
every_third_number = numbers[::3]  # Get every third number

# Advanced String Operations
capitalized_name = name.capitalize()  # Capitalize first letter
swapped_case = name.swapcase()  # Swap case of all characters
is_name_alpha = name.isalpha()  # Check if name is alphabetic
contains_space = " " in name  # Check if there's a space in the name

# String Comparison (Case-insensitive)
if name.lower() == "john doe".lower():
    print("Name matches John Doe.")

# Working with Lists: Advanced Operations
extended_hobbies = hobbies + ["Hiking", "Swimming"]  # Concatenation of lists
replicated_hobbies = hobbies * 2  # Replicate list elements
hobby_exists = "Coding" in hobbies  # Check membership in list
filtered_hobbies = [hobby for hobby in hobbies if isinstance(hobby, str)]  # List comprehension to filter strings

# More Advanced Arithmetic and Comparison
ratio = salary / 30  # Assume monthly salary is split over 30 days
threshold = 100
complex_comparison = salary > threshold and total_salary > 1.5 * salary or not is_rich

# Final summary of advanced operations
print("\nSummary of Advanced Concepts:")
print(f"Name: {name} (Capitalized: {capitalized_name}, Reversed: {reversed_name})")
print(f"String Operations: Middle Name={middle_name}, Every Second Letter={every_second_letter}")
print(f"Advanced Slicing: First Two Letters={first_two_letters}, Last Two Letters={last_two_letters}")
print(f"Numbers List Slice={nested_list_slice}, Deep Nested Slice={deep_nested_slice}")
print(f"Reversed Numbers={reversed_numbers}, Every Third Number={every_third_number}")
print(f"Hobbies Filtered: {filtered_hobbies}, Bonus Salary: {total_salary:.2f}")
print(f"Complex Logical Expression Results: Rich={is_rich}, Young but Rich={is_young_but_rich}")

# Logical Expression Based on Salary and Age
if salary > 3000:
    print("You have a high salary!")
elif salary > 1000 and age < 25:
    print("You are doing well for your age!")
else:
    print("Keep growing your career!")

# Type Checking
is_int = isinstance(age, int)
is_float = isinstance(salary, float)
is_string = isinstance(name, str)

# Output type checking results
print(f"\nType Check Results: Age (int)={is_int}, Salary (float)={is_float}, Name (str)={is_string}")


# ------------------------------------------------------------------------




# Python Week 1: Comprehensive Program

# Scenario: A small payroll and employee management system
print("Welcome to the Employee Management System")

# Input employee details
name = input("Enter employee's full name: ")
age = int(input("Enter employee's age: "))
basic_salary = float(input("Enter employee's basic salary (in USD): "))

# Additional Info
designation = input("Enter the employee's designation: ")
working_days = int(input("Enter the number of working days in the month: "))

# Calculations
# Calculate monthly bonus and deductions based on salary
bonus_percentage = 10 if basic_salary > 2000 else 5  # Conditional logic
bonus_amount = basic_salary * (bonus_percentage / 100)  # Bonus calculation
tax_deduction = basic_salary * 0.15 if basic_salary > 2500 else basic_salary * 0.05  # Tax deduction logic
total_salary = basic_salary + bonus_amount - tax_deduction

# Advanced operators
total_salary += 100  # Additional incentive for high performers
total_salary **= 1.01  # Small annual raise in performance evaluation

# Logical checks and conditions based on age and salary
is_adult = age >= 18
is_senior = age > 60
eligible_for_retirement = is_senior and total_salary > 3000

# Advanced string slicing and manipulation
first_name = name.split()[0]  # Extract first name
reversed_name = name[::-1]  # Reverse employee's full name
is_valid_name = name.isalpha()  # Name must be alphabetical

# Advanced list operations: Employee skills and performance tracking
skills = ["Python", "Teamwork", "Project Management"]
additional_skills = ["Communication", "Leadership"]
all_skills = skills + additional_skills  # Concatenation of skills
skills_training = ["Python Training", "Leadership Course"] * 2  # Replicating skills training twice

# Slicing the skills
top_skills = all_skills[:3]  # First three skills
reversed_skills = all_skills[::-1]  # Reverse the list of skills
every_second_skill = all_skills[::2]  # Every second skill

# Displaying the employee summary
print(f"\nEmployee Summary for {name}:")
print(f"First Name: {first_name}")
print(f"Reversed Name: {reversed_name}")
print(f"Designation: {designation}")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"Bonus Percentage: {bonus_percentage}%")
print(f"Bonus Amount: ${bonus_amount:.2f}")
print(f"Tax Deduction: ${tax_deduction:.2f}")
print(f"Total Salary after deductions and incentives: ${total_salary:.2f}")
print(f"Eligible for Retirement: {eligible_for_retirement}")

# Final skills output
print(f"\nEmployee's Skills: {all_skills}")
print(f"Top 3 Skills: {top_skills}")
print(f"Reversed Skills: {reversed_skills}")
print(f"Every Second Skill: {every_second_skill}")

# Checking valid age and name conditions
if is_adult:
    print(f"{first_name} is an adult.")
if eligible_for_retirement:
    print(f"{first_name} is eligible for retirement benefits.")
if not is_valid_name:
    print("Invalid name format detected (should contain alphabets only).")

# Final Type Checks (Advanced)
is_name_string = isinstance(name, str)
is_age_integer = isinstance(age, int)
is_salary_float = isinstance(basic_salary, float)

print(f"\nType Check Results: Name is String={is_name_string}, Age is Integer={is_age_integer}, Salary is Float={is_salary_float}")

# Handling and filtering skills using list comprehension
filtered_skills = [skill for skill in all_skills if isinstance(skill, str) and len(skill) > 6]  # Filtering longer skills
print(f"Filtered Skills (more than 6 characters): {filtered_skills}")

# Advanced Logical Expression
is_high_earner = total_salary > 5000 and len(skills) >= 3
print(f"Is {first_name} a high earner with excellent skills? {is_high_earner}")





