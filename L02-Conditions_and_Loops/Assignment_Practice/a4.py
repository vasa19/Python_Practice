'''
Q. Sum of even and odd
Write a program to input an integer N and print the sum of all its even digits
and sum of all its odd digits separately.
Digits mean numbers, not the places! That is, if the given integer is "13245",
even digits are 2 & 4 and odd digits are 1, 3 & 5.
'''

n = int(input())

sumEven = 0
sumOdd = 0
while n != 0:
    if (n % 2 == 0):
        a = n % 10
        sumEven = sumEven + a
    else:
        a = n % 10
        sumOdd = sumOdd + a
    n = n // 10

print(sumEven, "\t", sumOdd)
