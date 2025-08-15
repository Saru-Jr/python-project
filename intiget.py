number = int(input("Enter an integer: "))
total = 0

for i in range(1, number + 1):
    total += i * i  # or i**2

print(total)
