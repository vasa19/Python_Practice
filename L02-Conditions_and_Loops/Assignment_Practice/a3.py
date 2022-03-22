'''
Q. Palindrome Number 
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
'''

n = int(input())
rev = 0
temp = n

while temp != 0:
    last = temp % 10
    temp = temp // 10
    rev = rev * 10 + last

if rev == n:
    print('True')
else:
    print("False")
