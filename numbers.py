#-------------------------------------------NUMBERS----------------------------------------------

x = 1    # int
y = 2.8  # float
z = 3j   # complex
print(type(x))
print(type(y))
print(type(z))

x = 5
y = 1234567890
z = -96352741
print(type(x))
print(type(y))
print(type(z))

x = 1.23
y = 4.0
z = -56.78
k = 93e1
s = -87.7e198
print(type(x))
print(type(y))
print(type(z))
print(type(k))
print(type(s))

x = 2+8j
y = 9j
z = -4j
print(type(x))
print(type(y))
print(type(z))

x = 6    # int
y = 7.8  # float
z = 9j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))
