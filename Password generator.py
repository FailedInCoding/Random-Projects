import random

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz12343567890~!@#$%^&*'

number = input('Number of Passwords? - ')
number = int(number)

length = input('Password Length - ')
length = int(length)

for p in range(number):
    Password = ''
    for c in range(length):
        Password += random.choice(chars)
    print(Password)