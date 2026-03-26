n = int(input("Enter a number to check: "))
original = n
num_of_digits = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** num_of_digits
    temp //= 10

if(sum == original):
    print("Armstrong number")
else:
    print("Not a armstrong number")
