x = -2  # Given value of x
y = 3 * (abs(2 * x) + 4)  # Calculate y
print(y)  # Print the result

print(f"a: {21 > 8}")
print(f"b: {6 == 7}")
print(f"c: {2 == 1}")
print(f"d: {2 == 2}")

print("one is equal to 3:",int(1==3))
print("two is equal to 2:",int(2==2))

myname = "Stone"
myage = 22
print(f"a: {75}") #numeric literal
print(f"b: {'Howdy'}") #String literal
print(f"c: {True}") #Constant literal
print(f"d: {myname}") #String variable
print(f"e: {myage}") #Numeric variable

print((4 - 5 + 6),(6 - 5 + 4))
print((4 * 5 + 6),(6 * 5 + 4))

print(f"is 'stone'=='stoney'? {'stone'=='stoney'}")
print(f"is 'abc'=='abc'? {'abc'=='abc'}")
print(f"is 'abc'=='def'? {'abc'=='def'}")

my_name = "stone"
print("assignment: ",my_name)
print("equality: ",my_name == "stone")

print("comparison:","cc" < "dd")
print("comparison:",7 < 8)

a = 8
b = 9
print(f"comparison: {a} is greater than {b}" if a > b else "")
print(f"comparison: {a} is less than {b}" if a < b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a >= b else "")
print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")

bank_balance = 50
if bank_balance < 100:
    money = 1500
    bank_balance += money

bank_balance = 50
if bank_balance < 100:
    money = 2000
    bank_balance += money
else:
    print("balance is less than or equal to 100.")

bank_balance = 50
savings = 100
if bank_balance < 100:
    money = 3000
    bank_balance += money
elif bank_balance > 200:
    savings += 100
    bank_balance -= 100
else:
    savings += 50
    bank_balance -= 50

fuel = 0
print("Fill tank now" if fuel <= 1 else "There's enough fuel")

fuel = 8
while fuel > 1:
    #keep driving
    print("There's enough fuel")
    fuel -= 1

books = ['harry potter', 'lord of the rings','stones autobiography']
for book in books:
    print(f"book: {book}")
for i in range(5):
    print(f'i: {i}')

for count in range(13):
    print(f"{count} times 15 is {count * 15}")
    if count == 8:
        break

for count in range(13):
    if count == 8:
        continue #skips equation
    print(f"{count} times 15 is {count * 15}")