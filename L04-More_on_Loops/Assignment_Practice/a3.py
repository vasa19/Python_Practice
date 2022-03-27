'''
Q. Even Fibonacci Numbers
Given a number N find the sum of all the even valued terms in the fibonacci sequence
less than or equal to N. Try generating only even fibonacci numbers instead of iterating
over all Fibonacci numbers.
'''

n = int(input())
fib1 = 0
fib2 = 2
sum = 0
if n > 2:
    sum = fib1 + fib2
    while fib2 <= n:
        fib3 = (4 * fib2) + fib1
        if(fib3 > n):
            break

        fib1 = fib2
        fib2 = fib3
        sum = sum + fib2
print(sum)
