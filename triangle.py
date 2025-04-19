rows=int(input("Enter no of rows:"))
for i in range(rows,0,-1):
    print("\n")
    for j in range (rows-i+1):
        print(i,"",end="")
