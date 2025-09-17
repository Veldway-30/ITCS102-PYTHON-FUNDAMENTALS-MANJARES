print("Factorial Program")
n = eval(input("Please Input a number: "))

factorial = 1
for x in range(n, 0, -1):
    factorial *= x

print("The factorial of", n, "is", factorial)
