print('howdy world!')
#This is a single line comment! Nu multi-line comments

print('Dragon') #Object type of string
print(6.21) # number type, technically float

A = 1
a = 2
print(a)
print(A)

user_name = "stonep"
gpa = 4.0
print(user_name)
print(gpa)

print("My username is " + user_name + " not Inigo")

print(f"My username is {user_name} not Inigo")

number = 345 * 3 
print(str(number)[1:3]) #use str() to convert the number to a string. using [1:3] to get the first 3 numbers

def add_numbers(a,b):
    output = a + b
    return output
print(add_numbers(5,6)) #Positional arguments
print(add_numbers(b = 10,a = 11)) #Named arguments

name = "Globalvar"
def say_hello():
    name = "LocalVar"
    return f"hello {name}"
print(say_hello())