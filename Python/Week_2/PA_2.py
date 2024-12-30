# # # a,b,c are three random distinct integers
# # a = 10
# # b = 20
# # c = 30
# # x, y, z = a, b, c
# # x = y = z
# # print(x==y==z)
# # print(x==y==z==c)
# # print(x==y==z==a)
# # print(x==y==z==b)


# x = 7.658
# print(int(x))
# print(int(-x))



# # Block 1
# flag = True
# if flag == True:
#     print('works')

# # Block 2
# flag = True
# if flag:
#     print('works')

# # Are the two blocks equivalent?
# # Yes, Then How?
# # Yes, because the value of flag is True in both the blocks. The first block checks if the value of flag is True, and the second block checks if the value of flag is True. Both the blocks are equivalent.

# a,b,c,d = input()
# print(a)
# print(b)
# print(c)
# print(d)




# # Consider the following code-block. E_1, E_2 and E_3 are all Boolean variables that have already been defined. x is a variable that has NOT been defined before.

# '''
# Added Empty Variables to make the code run without any error.
# '''
# E_1 = ... 
# E_2 = ...
# E_3 = ...

# if E_1:
#     x = 1
# if E_2:
#     x = 2
# if E_3:
#     x = 3
# print(x)


# # Q - When will this code throw an error?
# # Ans - When all three Boolean variables are False.


# # Q - If the code throws an error, in which line will it occur? Enter an integer between 1 and 7, both endpoints included.
# # Ans - 7


# # Caeser Cipher

# alpha = "abcdefghijklmnopqrstuvwxyz"
# name = "Devendra"
# name = name.lower()
# hash = ""
# i,k = 0,1
# while i < len(name):
#     hash = hash + alpha[(alpha.index(name[i])+k) % 26]
#     i = i + 1
# print(hash)




