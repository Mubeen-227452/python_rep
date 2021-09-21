name = input('what is your name?')
birth_year = input('your birth year?')
age = 2020 - int(birth_year)
print(name, '-', age)
"python tutorials"
' hi iam A'
"""Hi ,
How are you?
i am A
Thank you"""

course = 'python for Beginners'
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:5])

"Formatted Strin:"

First = 'John'
Last = 'Smith'
message = First + '[' + Last + '] is a coder'
msg = f'{First} [{Last}] is a coder'
print(message)
print(msg)

"String Function"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('p'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('python' in course)

"IF Statement"
is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("Its a cold day")
    print("wear warm clothes")

weight = int(input('weight: '))
unit = input('(L) bs or (K)g:')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f" you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")

"While"
i = 1
while i <= 5:
    print(i, end=" ")
    i = i + 1

print("\ndone")

i = 5
while i >= 1:
    print(i, end=" ")
    i -= 1

print("\ndone")

secret = 9
guess_count = 0
while guess_count < 3:
    guess = int(input('GUESS> '))
    guess_count += 1
    if guess == secret:
        print("YOU WON !!")
        break
    else:
        print("SORRY YOU HAVE FAILED.")

command = ""
started = False
while command != "quit":
    command = input(">").lower()
    if command == 'start':
        print("car started...")
    elif command == 'stop':
        print("cart stopped.")
    elif command == 'help':
        print("""
        Strat - to start cart
        stop- stop the car
        quit- to quit the program""")
    elif command == 'quit':
        break
    else:
        print("I dont understand!")
for item in 'python':
    print(item)
for i in [1, 2, 3, 4]:
    print(i)

for i in range(10):
    print(i)

for i in range(2, 10, 2):
    print(i)

prices = [10, 20, 30]
total = 0
for p in prices:
    total += p
print(total)

for x in range(4):
    for y in range(3):
        print(f'{x},{y}')

n = [5, 2, 5, 2, 2, 2]
for num in n:
    print('x' * num)

p = [5, 2, 5, 2, 2, 2]
for num in p:
    o = ''
    for c in range(num):
        o += 'Y'
    print(o)

number = [2, 4, 6, 1, 3, 8, 9, 5]
max = number[0]
for i in number:
    if i > max:
        max = i
print(max)

number = [2, 2, 3, 3, 44, 44, 5, 6]
unique = []
for i in number:
    if i not in unique:
        unique.append(i)
print(number)
print(unique)

phone = input("enter ph number:> ")
digit_map = {"1": "one", "2": "two", "3": "Three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight",
             "9": "nine", "0": "zero"}
op = ''
for ch in phone:
    op += digit_map.get(ch, "!") + " "
print(op)


def greet_user(f_name, l_name):
    print(f"Hi {f_name} {l_name}!")
    print('welcome aboard')

greet_user("john","mosh")
greet_user(l_name="mosh",f_name="john")

def square(n):
    return n*n

r=square(3)
print(r)