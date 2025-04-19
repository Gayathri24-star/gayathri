n_terms=int(input("Enter the no of fibonacci terms to display"))
a,b=0,1
count=0
if n_terms<=0:
    print("Please enter a positive integer.")
elif n_terms==1:
     print("print fibonacci sequence:")
     print(a)
else:
     print("fibonacci sequence:")
     while count < n_terms:
            print(a,end="")
            a,b=b,a+b
            count+= 1
