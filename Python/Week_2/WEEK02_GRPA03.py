
# Week 2 Graded Programming Assignment 3 - "Very Good!!!"
# The Question is as follows:
'''
GrPA 3 - Basic conditional patterns - GRADED
This problem gives you exposure to different use cases of if ... elif and else conditional structues.

Part 1 - Only if

Part 2 - if ... else

Part 3 - if ... elif

Template Code(Click to Expand)
# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if ... :
    ...

# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if ...:
    ...
else:
    ...

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block

# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if ...
elif ...:
        ...
elif ...:
    ...
else:
    ...

is_time_valid = ... # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = ...

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here
'''



# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "12 AM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if "ing" in new_word:
    new_word = new_word.replace("ing","")

# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here
if continuous_tense:
    new_word = new_word + "ing"
# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age >= 18:
    age_group = "Adult"
else:
    age_group = "Child"

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block
if age_group == "Adult":
    if is_member:
        applicant_type = "Adult Member"
    else:
        applicant_type = "Adult Non-member"
else:
    if is_member:
        applicant_type = "Child Member"
    else:
        applicant_type = "Child Non-member"

# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if color_code == "R":
    color = "red"
elif color_code == "G":
    color = "green"
elif color_code == "B":
    color = "blue"
else:
    color = "black"

is_time_valid = True if int(time.replace(" PM","").replace(" AM","")) in [1,2,3,4,5,6,7,8,9,10,11,12] else False # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = int(time.replace("AM",""))%12 if "AM" in time else 12 + (int(time.replace("PM",""))%12)

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here
if is_time_valid:
    if time_in_hrs >= 6 and time_in_hrs < 12:
        time_of_day = "Morning"
    elif time_in_hrs >= 12 and time_in_hrs < 18:
        time_of_day = "Afternoon"
    elif time_in_hrs >= 18 and time_in_hrs < 24:
        time_of_day = "Evening"
    elif time_in_hrs < 6:
        time_of_day = "Night"
else:
    time_of_day = "Invalid"

# # print all varaibles
# print(new_word)
# print(age_group)
# print(color)
# print(is_time_valid)
# print(time_in_hrs)
# print(time_of_day)
