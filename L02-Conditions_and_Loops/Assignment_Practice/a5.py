'''
Q. Nth Fibonacci Number
Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
    F(n) = F(n-1) + F(n-2), 
    Where, F(1) = F(2) = 1
Provided N you have to find out the Nth Fibonacci Number.
'''

n = int(input())
a = 0
b = 1
sum = 0
i = 0
while i <= n:
    sum = sum + a
    a = b
    b = sum
    i += 1

print(b)
