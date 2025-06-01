### This function is used to test where the given string palindrome and symmetric.

s = "amaama"
def is_palindrome(s):
    return s == s[::-1]

def is_symmetric(s):
    length = len(s)
    mid = len(s)//2
    if length % 2 == 0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]
    
if is_palindrome(s):
    print("The string entered is palindrome")
else:
    print("The string entered is not palindrome")

if is_symmetric(s):
    print("The string entered is symmetrical")
else:
    print("The string entered is not symmetrical")



