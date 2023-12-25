myfile = open('myfile.txt')

print(myfile.read())
# need to reset cursor to 0 to file containt see again
myfile.seek(0)
print(myfile.read())
myfile.seek(0)

contents = myfile.read()
print(contents)

myfile.seek(0)
print(myfile.readlines())

myfile.close()

# other way
with open('myfile.txt') as new_file:
    contents = new_file.read()
    print(contents)

with open ('mynewfile.txt', mode='r') as f:
    print(f.read())
    
with open ('mynewfile.txt', mode='a') as f:
    f.write('\nFour on forth D')
    
with open ('mynewfile.txt', mode='r') as f:
    print(f.read())

with open('createdbypy.txt', mode='w') as z:
    z.write('This file is created by py')
    
with open('createdbypy.txt', mode='r') as c:
        print(c.read())