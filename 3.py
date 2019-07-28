#%%
print("#This is not a comment because it's inside quotes.")


#%%
2+2

#%%
50-5*6

#%%
(50-5*6)/4

#%%
8/5

#%%
17/3
#%%
17//3


#%%
17%3

#%%
5*3+2


#%%
5**2

#%%
2**7

#%%
width=20
height=5*9
width*height

#%%
n

#%%
4*3.75-1

#%%
tax=12.5/100
price=100.50
price*tax
#%%
price+_

#%%
round(_,2)

#%%
'spam eggs'

#%%
"doesn't"

#%%
'doesn\'t'

#%%
'"Yes," they said.'

#%%
'"Isn\'t," they said.'

#%%
"\"Yes,|" they said.""

#%%
"\"Yes,\" they said."

#%%
'"Isn\'t they said.'

#%%
'"Isn\'t" they said.'

#%%
'"Isn\'t, they said.'

#%%
print('"Isn\'t," they said.')

#%%
s = 'First line. \nSecond line.' # \n means newline

#%%
s

#%%
print(s)

#%%
print('C:\some\name')

#%%
print(r'C:\some\name')

#%%
print("""\
    Usage:thingy[OPTIONS]
    -h              Display this usage message
    -H hostname         Hostname to connect to
    """)

#%%
3 * 'un' + 'ium'

#%%
'Py' 'thon'

#%%
text = ('Put several strings within parentheses'
    'to have them joined together.')
text

#%%
prefix = 'Py'
prefix 'thon # can't concatenate a variable and a string literal

#%%
prefix + 'thon'

#%%
prefix = 'Py'
prefix + 'thon'

#%%
word = 'Python'
word[0]
word[5]

#%%
word[-1]

#%%
word[-2]

#%%
word[:2]

#%%
word[0:3]

#%%
word[42]

#%%
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

#%%
word[0] = 'J'

#%%
'J' + word[1:]

#%%
word[:2] + 'py'

#%%
s = ' supercalifragilisticexpialidocious'
len(s)

#%%
str.format('python')

#%%
str.format(111222)

#%%
String Methods

#%%
squares = [1,4,9,16,25]
squares

#%%
squares[0]

#%%
squares + [36,49,64,81,100]

#%%
cubes = [1,8,27,65,125]
4**3

#%%
cubes[3]=64
cubes

#%%
cubes.append(216)

#%%
cubes[:]

#%%
letters = ['a' , 'b' , 'c'. 'd', 'e', 'f', 'g']
letters

#%%
letters = ['a' , 'b' , 'c'. 'd', 'e', 'f', 'g']
letters

#%%
letters = ['a' , 'b' , 'c', 'd', 'e', 'f', 'g']
letters

#%%
letters[2:5] = ['C', 'D', 'E']

#%%
letters

#%%
letters[2:5] = []

#%%
letters

#%%
len(letters)

#%%
# Fibonacci series:
# the sum of two defines the next
a,b =0,1

#%%
while a<10:
    print(a)
    a,b = b,a+b

#%%
i = 256*256
print('The value of i is', i)


#%%
a,b = 0,1
while a < 1000:
    print(a, end=',')
    a,b =b,a+b

#%%
