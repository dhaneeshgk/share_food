def Palindrome(str):
    i = 0
    j = len(str) - 1
    while(i <= j):
        if(str[i] != str[j]):
            return False
        i += 1
        j -= 1
    return True
s = "nikki"
if(Palindrome(s)):
    print("string is palindrome")
else:
    print("string is not palindrome")
