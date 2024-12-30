# # To Calculate the factors of a number

# n = int(input())
# i = 1
# while (i <= n):
#     if (n % i == 0):
#         print(i)
#     i = i + 1



# # My code for fibonacci series
# n = int(input())
# f_prev = 1
# f_curr = 1
# for i in range(n):
#     if i<2:
#         print(f"F_{i+1}: 1")
#         continue
#     fibonacci = f_prev + f_curr
#     print(f"F_{i+1}: {fibonacci}")
#     f_prev = f_curr
#     f_curr = fibonacci
#     i += 1


# # If we need F_n only:
# n = int(input())
# f_prev = 1
# f_curr = 1
# for i in range(n):
#     if i<2:
#         fibonacci_n = 1
#         continue
#     fibonacci_n = f_prev + f_curr
#     f_prev = f_curr
#     f_curr = fibonacci_n
#     i += 1
# print(f"F_{n}: {fibonacci_n}")

count = 0
for x in range(100):
    for y in range(100):
        if x != y:
            count += 1
            print(f'{x},{y}')
print(count)

# Alt Code:
x, y = 0, 0
while x < 100:
    y = 0
    while y < 100:
        if x != y:
            print(f'{x},{y}')
        y += 1
    x += 1