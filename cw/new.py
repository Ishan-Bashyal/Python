#import keyword
#print(len(keyword.kwlist))
#print(keyword.iskeyword('True'))

#string
firstName='ram'
lastName='kc'
print(id(firstName))
print(id(lastName))
print(firstName is lastName)


#int
firstName=1
lastName=1
print(id(firstName))
print(id(lastName))
print(firstName is lastName)


#float
firstName=0.1
lastName=0.1
print(id(firstName))
print(id(lastName))
print(firstName is lastName)


#tuple
firstName=1,2
lastName=1,2
print(id(firstName))
print(id(lastName))
print(firstName is lastName)


#complex
firstName=1+2j
lastName=1+2j
print(id(firstName))
print(id(lastName))
print(firstName is lastName)


#list
firstName=[1,2,3]
lastName=[1,2,3]
print(id(firstName))
print(id(lastName))
print(firstName is lastName)




