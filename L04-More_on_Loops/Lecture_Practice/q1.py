'''
Q. Terms of AP
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
'''

n = int(input())
current = 1
count = 1

while count <= n:
    num = 3 * current + 2

    if num % 4 != 0:
        print(num, end=' ')
        count += 1
    current += 1
