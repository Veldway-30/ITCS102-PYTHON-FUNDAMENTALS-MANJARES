print("Multiplaticaion Table Maker")
number = eval(input("Please input a number: "))

print("\nMultiplication table for", number,":")
for x in range(1, 11, 1):
	print(number,"x",x ,"=", number * x)