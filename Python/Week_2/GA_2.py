'''
Consider the following snippet of code. Assume that L is a positive integer that has already been defined at this stage.

# L is a positive integer that has already been defined at this stage
word = input()
space = ' ' # there is a single space
if len(word) < L:
    word = 'short' + space + word
elif L <= len(word) < 2 * L:
    word = 'medium' + space + word
else:
    word = 'long' + space + word
print(word)

The code is run twice, with two different input words. Each input word is a string that consists only of letters without any spaces in them.

Output-1
short good

Output-2
long goodnessme

With just this data given to you, what is the value of L? (NAT)
'''

# Answer



num = input()
first, middle, last = int(num[0]), int(num[1]), int(num[2])
if first + last == middle:
    print('sandwich')
else:
    print('plain')