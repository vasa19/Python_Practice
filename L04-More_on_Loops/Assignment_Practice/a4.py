'''
Q. Trailing zeros in n!
Find and return number of trailing 0s in n factorial without calculating n factorial.
'''

n = int(input())
count = 0
i = 5

while(n / i >= 1):
    count = count + (int(n / i))
    i *= 5
print(count)
