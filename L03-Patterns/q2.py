'''
Q. Triangular star pattern
*
**
***
****
'''

n = int(input())
for row in range(n):
    for col in range(row + 1):
        print("*", end='')
    print()
