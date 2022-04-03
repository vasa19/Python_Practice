'''
Q. Swap Alternate
You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
You don't need to print or return anything, just change in the input array itself.
'''


def rev(li):
    l = len(li)
    if l % 2 == 0:
        for i in range(0, l, 2):
            li[i], li[i + 1] = li[i + 1], li[i]
    else:
        for i in range(0, l - 1, 2):
            li[i], li[i + 1] = li[i + 1], li[i]

    for i in li:
        print(i, end=' ')


n = int(input())
li = [int(s) for s in input().split()[:n]]
rev(li)
