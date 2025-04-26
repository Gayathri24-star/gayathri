def gcd(a,b):
    """
compute the greatest common divisor (GCD) of two numbers using the euclids algorithm
 :param a: first number (integer)
 :param b: second number (integer)
 :return:GCD of a and b.
 """
    while b!=0:
        a,b=b,a%b
    return abs(a)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
result=gcd(num1,num2)
print(f"The GCD of {num1} and {num2} is:{result}")
 
