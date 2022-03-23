'''
Q. Interesting Alphabets
E
DE
CDE
BCDE
ABCDE
'''

n = int(input())
for row in range(1, n + 1):
    startCh = chr(ord('A') + n - row)
    for col in range(1, row + 1):
        ch = chr(ord(startCh) + col - 1)
        print(ch, end='')
    print()
