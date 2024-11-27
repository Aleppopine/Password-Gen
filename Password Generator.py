import random

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.-1234567890'

number = input('HOW MANY PASSWORDS?')
number = int(number)

length = input('PASSWORD LENGTH?')
length = int(length)

print('PASSWORDS')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
    