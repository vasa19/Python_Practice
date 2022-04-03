'''
Q. Check Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters.
A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.
'''

s = input()
reverse_s = s[::-1]
if reverse_s == s:
    print("True")
else:
    print("False")
