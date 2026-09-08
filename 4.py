first = int(input("Enter first number : "))
second = int(input("Enter second number : "))



result = 1

for i in range(second):
    result *= first

print(f"{first} raised to the power {second} is : {result}")
