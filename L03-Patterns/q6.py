'''
Q. Character Pattern
A
BC
CDE
DEFG
'''

n = int(input())
for row in range(1, n + 1):
    startCh = chr(ord('A') + row - 1)
    for col in range(1, row + 1):
        ch = chr(ord(startCh) + col - 1)
        print(ch, end='')
    print()
