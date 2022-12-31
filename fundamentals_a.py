#Data Types
#int 1, 10000, -199
#float .56, 8.0, -1.2
#str "hola", 'mundo', '''peludo'''
#bool True, False

#Comments
#This is a comment

variable = "This is a variable"
print(variable)

name = input("What is your name? ")
print("Your name is ", name)
print("Your name also is " + name)
print(type(name))
print("-----")
print("")

input("Press enter to begin!")
name = input("Enter name: ")
age = input("Hello " + name + ", what is your age?: ")
print("Hello " + name + ", you are " + age + " years old!")
print("-----")
print("")

print("+, -, *, /, **, //")
x = 7
y = 2
r = x + y
print("x + y = ", r) #Addition
r = x - y
print("x - y = ", r) #Subtraction
r = x * y
print("x * y = ", r) #Multiplication
r = x / y
print("x / y = ", r) #Division (always float)
r = x ** y
print("x ** y =", r) #Exponential
r = x // y
print("x // y =", r) #Integer Division
r = x % y
print("x % y =", r) #Modulus
word1 = "hello"
word2 = "world"
print(word1 + word2) #Concatenation

#Order of operations
#1. Brackets/Parathesis
#2. Exponents
#3. Multiplication, Division and Modulus
#4. Addition & Subtraction
