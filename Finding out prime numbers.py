n= int(input("Enter a number: "))
prime_numbers = []
for i in range(2, n+1):
    p = True
    for j in range(2, i):
        if i%j == 0:
            p = False
    if p:
        prime_numbers.append(i)
        print(i, end=", ")

total = input(f"Do you want to know the number of prime numbers between 1 and {n}? (yes/no): ")

if total.lower() == "yes":
    print(f"Total prime numbers = {len(prime_numbers)}")

else:
    print("")