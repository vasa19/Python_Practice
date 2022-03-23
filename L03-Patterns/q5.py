'''
Q. Alpha Pattern
A
BB
CCC
DDDD
'''

n = int(input())
for row in range(1, n + 1):
    ch = chr(ord('A') + row - 1)
    for col in range(1, row + 1):
        print(ch, end='')
    print()
