char=input("enter a single ncharacter:")
if len(char)!=1:
    print("please enter only one character!")
else:
     if char.isdigit():
            print(f"'{char}'is a digit.")
     elif char.islower():
            print(f"'{char}'is a lowercase character.")
     elif char.isupper():
            print(f"'{char}'is a uppercase character.")
     else:
            print(f"'{char}'is a special character.")
