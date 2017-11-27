#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random

# if语句
number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    print('Congratulations, you guessed it.')
elif guess < number:
    print('No, it is a litter higher than that.')
else:
    print('No, it is a litter lower than that.')


# while语句
number = 23
running = True

while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a litter higher than that.')
    else:
        print('No, it is a litter lower than that.')
print('Game Over!')

# 循环猜一个随机数，直至猜中为止
secret = random.randint(1, 10)
guess = int(input('Enter an integer:'))
if guess == secret:
    print('You get it!')
while guess != secret:
    if guess < secret:
        print('Sorry, it is litter!')
        print('again!')
        guess = int(input('Enter an integer:'))
    else:
        print('Sorry, it is big!')
        print('again!')
        guess = int(input('Enter an integer:'))
print('Game Over!')


# for循环
for i in range(1, 5):
    print(i)
print('The for Loop is over!')


# break语句
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done!')


# continue语句
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print('Input is of sufficient length')
print('Over!')




