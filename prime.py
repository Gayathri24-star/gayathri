start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print(f"\nPrime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num < 2:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime=False
            break
        else:
            print(num, end=" ")
