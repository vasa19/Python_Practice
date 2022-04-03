'''
Q. Print all substrings
For a given input string(str), write a function to print all the possible substrings.
A substring is a contiguous sequence of characters within a string. 
Example: "cod" is a substring of "coding". Whereas, "cdng" is not as the characters taken are not contiguous
'''

s = input()
x = len(s)

for i in range(x):
    for len in range(i + 1, x + 1):
        print(s[i: len])
