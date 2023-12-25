#strings are ordered sequences
print('hello')
print("world")
print("Hello I am string")
print("i'm going to run")
print("Hello \n World")
print("Hello \t World")

# checking string length
print(len('hello'))

# indexing
# h  e  l  l  o
# 0  1  2  3  4
# 0 -4 -3 -2 -1

mystring = 'hello world'
print(mystring)
print(mystring[0])
print(mystring[8])
print(mystring[9])
print(mystring[-1])
print(mystring[-2])

# Slicing
# [start:stop:step]
mystring = 'abcdefghijk'
print(mystring[:])
print(mystring[2])
print(mystring[2:])
print(mystring[:3])
print(mystring[3:6])
print(mystring[1:3])
print(mystring[3:9])

# step size
# print(mystring[start:stop:stepsize])
print(mystring[::])
print(mystring[::2])
print(mystring[::3])

print(mystring[2:9:3])
print(mystring[1:10:2])

# reverse strig
print(mystring[::-1])

# String properties and Methods
# Immutability

name = "Sam"
# name[0] = "p" This will give error

print(name)
last_letters = name[1:]
print(last_letters)
# Strig concatination
print('P'+last_letters)

x = 'Hello World'
print(x + " It is beautiful outside")

letter = 'z'
print(letter*10)

print(2+4)
print('2'+'4')

# String methods dont forget parenthesis
x = 'Hello World'
print(x.upper())
print(x.lower())
print(x.split())

x = 'Hi this is a string'
print(x.split())
print(x.split('i'))


# String formating for printing
print('This is a string {}'.format('Inserted'))

print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {0} {0} {0}'.format('fox','brown','quick'))


print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
print('The {f} {f} {f}'.format(f='fox',b='brown',q='quick'))

# Float formatinng "{value:width.precision f}"
result = 1000/777
print(result)

print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:10.5f}".format(r=result))

# fStrings
name = "jose"
print(f'Hello, his name is {name}')

name = "Sam"
age = 3
print(f'{name} is {age} years old.')