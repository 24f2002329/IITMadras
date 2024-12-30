# WEEK01_GRPA05

age = int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[0:2]),int(dob[3:5]),int(dob[6:]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = f"{day}/{month}/{year+5}" # str: fifth birthday formatted as day/month/year 

last_birthday = f"{day}/{month}/{year+age}" # str: last birthday formatted as day/month/year

tenth_month = f"{day}/{((((month+10)-1)%12)+1)}/{year+(((month+10)-1)//12)}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month,fifth_birthday,last_birthday, sep=", ")

weight = float(input()) # float: Read a number as float from stdin(Standard input)

weight_readable = f"{int(weight)} kg {round((weight-int(weight))*100)}0 grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)



# *The* Logic
# Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month, fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number) separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")

# Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.

# Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".

# Note: Finding the tenth_month will be a bit of challange. If you are stuck open the below hint.

# Hint for tenth_month
# Explanation

# When you're adding months to a date, you need to make sure that the month number doesn't go beyond 12, because there are only 12 months in a year.

# Starting from Zero:
# Think of months like positions on a number line that starts at zero instead of one (because modulo cycles from 0 to n-1). January is 0, February is 1, and so on.
# When you subtract 1 from a month, you're basically shifting it to this zero-based system. For example, if you start at month 10 (October), subtracting 1 gives you 9.
# Using Modulo:
# The modulo operation helps to wrap around when you go past December. So, 13 becomes 1 (January), 14 becomes 2 (February), etc.
# The modulo operation works naturally with zero-based numbers. For example, 24 % 12 = 0 means it wraps around to the starting point (January).
# Adding 1 Back:
# After using the modulo operation, you add 1 back to shift back to the regular month numbering system. This makes sure that months are in the range of 1 to 12.
# Example

# Let's say it's October (month 10) and you want to find the date 15 months later.

# Add the Months:
# 10 (October) + 15 months = 25.
# Convert to Zero-Based and Apply Modulo:
# Subtract 1: 25 - 1 = 24.
# Apply modulo 12: 24 % 12 = 0.
# This means it wraps around to the start of the year.
# Convert Back to One-Based:
# Add 1: 0 + 1 = 1.
# So, it’s January.
# Adjust the Year:
# Since you added enough months to go into the next year, you need to account for that.
# Calculate how many full years you’ve added: (25 - 1) // 12 = 2.
# So, if you started in 2022, adding 2 years brings you to 2024.
# Result

# 15 months from October 2022 is January 2024.

