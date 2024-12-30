'''
A bit of wisdom 📖

Iterable - Something that can be used in a for loop.
Collection - Datatypes that hold many values like list, set, tuple and dict.
All iterables are not collections. Eg. str and range are iterables but not collections.
All collections are iterables.
Only ordered collections are indexable and slicable
Only Mutable collections can be modified
Hasing is a method used in collections like set to check whether an element is present or not quickly, and in dict to retrive the value for the given key quickly. There are only certain datatypes that can be hashed. For example


Data Type	Iterable	Collection	Indexable/
Sliciable	Ordered	Mutable	Uses Hashing
str	✅	❌	✅	✅	❌	❌
range	✅	❌	❌	✅	❌	❌
list	✅	✅	✅	✅	✅	❌
tuple	✅	✅	✅	✅	❌	❌
set	✅	✅	❌	❌	✅	✅
dict	✅	✅	❌	❌	✅	✅
(on keys)

built-in functions - some functions like sum, min, max, sorted, reversed will help in doing some basic tasks.
Any iterable can be converted into a list or a tuple
Any iterable of hashable data types can be converted into a set

Learning objectives

NOTE In this exercise we will not be using dict as they will be introduced in next week.

Empty collections
Singleton Collections
True-ness and False-ness in collections
Inbuilt functions for collections
Indexing and Slicing
Membership checks
Concatenation

Instructions on how to solve (Click to expand)
NOTE: In this type of questions you should not take input or print anything unless your are explicitly asked to. Assign the result of the required computation to the correct variable name as it will be evaluated for type and value by the evaluator.

The input variables will be assigned by the evaluator based on the test cases.

The grey part before the white part (if any) in the code is the prefix code. The grey part after the white part (if any) is the suffix code which are not editable. Usually they will be the part of code but in this type of questions it will be removed by the evaluator.

The Three dots (...) called as Ellipsis in python are like placeholders, replace them with your answer.

The inputs on the code blocks are just sample inputs they won't be evaluated in the actual testcases.

Each testcase will have its own set of testcases defined as variables. The check function in the testcases is in the hidden evaluation code that checks the value and type of the variable.

'''


# The values of the below variables will be changed by the evaluator
int_iterable = range(1,10,3)
string_iterable = ["Apple","Orange", "Banana"]
some_value = 4
some_collection = [1,2,3] # list | set | tuple 

some_iterable = (1,2,3)
another_iterable = {"apple", "banana", "cherry"} # can be any iterable
yet_another_iterable = range(1,10)

# <nofor>
# <eoi>

empty_list = [] 
empty_set = set() # be carefull here you might end up creating something called as an empty dict 
empty_tuple = tuple() 

singleton_list = [1] # list: A list with only one element
singleton_set = {1} # set: A set with only one element
singleton_tuple = (1,) # tuple: A tuple with only one element

a_falsy_list = [] # list: a list but when passed to bool function should return False.
a_falsy_set = set() # set: a list but when passed to bool function should return False.
a_truthy_tuple = (1,) # tuple: a tuple but when passed to bool function should return True.

int_iterable_min = min(int_iterable) # int: find the minimum of int_iterable. Hint: use min function
int_iterable_max = max(int_iterable) # int: find the maximum of int_iterable. Hint: use max function
int_iterable_sum = sum(int_iterable) # int: you know what to do
int_iterable_len = len(int_iterable) # int: really... you need hint?
int_iterable_sorted = sorted(int_iterable) # list: the int_iterable sorted in ascending order
int_iterable_sorted_desc = sorted(int_iterable, reverse=True) # list: the int_iterable sorted in desc order

if  : # some iterables are not reversible why?
    int_iterable_reversed = list(reversed(int_iterable)) # list: the int_iterable reversed use the reversed function
else: # in that case sort it in ascending order and reverse it
    int_iterable_reversed = list(reversed(sorted(int_iterable)))

if ...: # some collections are not indexable why?
    third_last_element = ... # the third last element of `some_collection`
else: # in that case set third_last_element to None
    third_last_element = ... 

if ...: # some collections are not slicable
    odd_index_elements = ... # type(some_collection): the elements at odd indices of `some_collection` 
else: # in that case set odd_index_elements to None
    odd_index_elements = ... 

is_some_value_in_some_collection = ... # bool: True if `some_value` is present in `some_collection`

if ...: # some collections are not ordered
    is_some_value_in_even_indices = ... # bool: True if `some_value` is present in even indices of `some_collection`
else: # in that case set is_some_value_in_even_indices to None
    is_some_value_in_even_indices = ...

all_iterables = ... # list: concatenate `some_iterable`, `another_iterable` and `yet_another_iterable` into a list.

if ... : # some iterables are not ordered
    all_concat = ... # str: concatenate all the strings in string_iterable with '-' in between
else: # in that case sort them and concatenate
    all_concat = ...




