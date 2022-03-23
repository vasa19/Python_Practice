'''
Q. Inverted Number Pattern
4444
333
22
1
'''

n = int(input())

for row in range(n, 0, -1):
    for col in range(1, row + 1):
        print(row, end='')
    print()
