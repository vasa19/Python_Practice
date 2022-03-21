'''
Q. Sum of Even Numbers
Given a number N, print sum of all even numbers from 1 to N.
'''

n = int(input())
sum = 0
while n > 0:
    if (n % 2 == 0):
        sum += n
        n -= 1
    else:
        n -= 1

print(sum)
