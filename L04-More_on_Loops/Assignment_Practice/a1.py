'''
Q. Decimal to Binary
Given a decimal number (integer N), convert it into binary and print.
The binary number should be in the form of an integer.
'''

n = int(input())
power = 1
binary = 0

while n > 0:
    lastbit = n % 2
    binary = binary + (lastbit * power)
    power *= 10
    n = n // 2

print(binary)
