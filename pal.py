def palindrome(string):
 string=string.replace("","").lower()
 return string==string[::-1]
print(palindrome("hello"))
