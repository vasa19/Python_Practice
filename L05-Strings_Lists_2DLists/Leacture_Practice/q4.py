'''
Q. Array equilibrium index
For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)]
is equal to the sum of elements at indices [(i + 1) to (N-1)]. One thing to note here is, the item at the
index 'i' is not included in either part.
If more than one equilibrium indices are present, then the index appearing first in left to right fashion
should be returned. Negative one(-1) if no such index is present.
'''


def equilibriumIndex(arr):
    totalSum = sum(arr)
    leftSum = 0
    for i, num in enumerate(arr):
        totalSum -= num
        if leftSum == totalSum:
            return i
        leftSum += num
    return -1


n = int(input())
arr = [int(i) for i in input().strip().split()[:n]]
print(equilibriumIndex(arr))
