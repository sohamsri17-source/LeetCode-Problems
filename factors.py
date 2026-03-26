n = int(input("Enter a number: "))
factors = []
temp = n
while temp > 0:
    if n % temp == 0:
        factors.append(temp)
    temp -= 1

print(factors)