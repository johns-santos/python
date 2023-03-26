def palindrome(s):
    # if s == s[::-1]:
    #     return True
    # return False
    return s == s[::-1]
 
print(palindrome("abc"))
print(palindrome("abba"))