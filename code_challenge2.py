amount = eval(input("Enter amount to deposit: "))

n1000 = amount // 1000
amount = amount % 1000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

n5 = amount // 5
amount = amount % 5

n1 = amount // 1
amount = amount % 1

print("\nHere is the breakdown:")
print("Php1000 -", n1000)
print("Php500 -", n500)
print("Php200 -", n200)
print("Php100 -", n100)
print("Php50 -", n50)
print("Php20 -", n20)
print("Php10 -", n10)
print("Php5 -", n5)
print("Php1 -", n1)