'''
Q. Square rooot(integral)
Given a number N, find its square root. You need to find and print only the integral part of square root of N.
For eg. if number given is 18, answer is 4.
'''

n = int(input())
check = 1

while (check ** 2 <= n):
    check += 1
print(check - 1)
