# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import os
scandir = os.listdir("C:\Windows")

print(scandir)

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("C:\/nginx") if isfile(join("C:\/nginx", f))]

print(onlyfiles)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

print("676765765"+"jyujuy")

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# Program to generate a random number between 0 and 9

# importing the random module
import random

print(random.randint(0,  999999999999999999999999999999))


# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2014  # year
mm = 11    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)