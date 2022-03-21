'''
Q. Sum of n numbers
Given an integer n, find and print the sum of numbers from 1 to n.
'''

n = int(input())
sum = 0
while n > 0:
    sum += n
    n -= 1

print(sum)
