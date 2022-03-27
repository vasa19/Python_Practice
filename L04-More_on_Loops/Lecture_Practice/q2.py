'''
Q. Sum or Product
Write a program that asks the user for a number N and a choice C. And then give them the possibility
to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).
If C is equal to -
 1, then print the sum
 2, then print the product
 Any other number, then print '-1' (without the quotes)
'''

n = int(input())
c = int(input())

sm = 0
pt = 1

if c == 1:
    for i in range(1, n + 1):
        sm = sm + i
    print(sm)
elif c == 2:
    for i in range(1, n + 1):
        pt = pt * i
    print(pt)
else:
    print('-1')
