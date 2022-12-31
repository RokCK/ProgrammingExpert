#Conditions

cond = 3.0 == 3
print(cond)
cond = 3.1 == 3
print(cond)

cond = 3.0 != 3
print(cond)
cond = 3.1 != 3
print(cond)

x = 9
y = 4

cond = x < y #You can use <= less or equal to
print(cond)
cond = x > y #You can use >= greater or equal to
print(cond)

cond = x + 8 > y #Note you can use operations
print(cond)

str1 = "hello"
str2 = "Hello"
cond = str1 == str2
print(cond) #Capitalization does matter in a string

str1 = "a"
str2 = "B"
cond = str1 < str2
print(cond) #Compares numeric ASCII values

print(ord("a")) #97 is the ASCII value
print(ord("A")) #65 is the ASCII value
print(chr(97)) #Prints "a"

cond = True == 1
print(cond)
cond = False == 0
print(cond)

#and, or, not

x = 2
y = 4
compound = x < y and y + 2 > 3
print(compound) #All conditions are True
compound = x < y or y + 2 > 3
print(compound) #At least one condition is True
compound = not (x < y)
print(compound) #Not reverses the condition
compound = not True == False
print(compound)
compound = True == (not False)
print(compound)
#compound = True == not False does NOT work

#Order of these operators
#1. Conditional/Comparison Operators
#2. Not
#3. And
#4. Or

#DeMorgan's Law
#not (x and y) == (not x) or (not y)
#not (x or y) == (not x) and (not y)

'''
W-Z
-----
F-F->True
T-F->True
F-F->True
T-T->False
'''
