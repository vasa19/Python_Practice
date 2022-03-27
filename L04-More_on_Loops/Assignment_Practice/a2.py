'''
Q. Binary to Decimal
Given a binary number as an integer N, convert it into decimal and print.
'''

n = int(input())
decimal = 0
power = 1

while n > 0:
    lastdigit = n % 10
    decimal = decimal + (lastdigit * power)
    power *= 2
    n = n // 10

print(decimal)
