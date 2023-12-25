#Dictionnaries syntax {'key1':'value1','key2':'value2'}
# Not able to sort
# Object retreaved by key name

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key1'])

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}
print(prices_lookup['milk'])

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k2'])

print(d['k3']['insideKey'])

print(d['k2'][2])

e = {'key1':['a','b','c']}
mylist = e['key1']
print(mylist)
letter = mylist[2]
print(letter)
print(letter.upper())

print(e['key1'][2])

e = {'key2':3000}
print(e['key2'])

print(d.values())
print(d.items())