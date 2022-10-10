# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

numbers=[]
def main():
    print('Hello, world!')


f=input("Enter a number:")
while f!='':
    numbers.append(int(f))
    f=input("Enter another number:")

i=0
cmmdc = math.gcd(numbers[i], numbers[i+1])
i=1
n=len(numbers)
for i in (1,n-1):
        cmmdc = math.gcd(numbers[i], cmmdc)
        i=i+1
print(cmmdc)