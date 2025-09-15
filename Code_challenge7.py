print("ODD NUMBER SUMMATION")

num_odd = 0
for x in range(1, 11, 1):
	num = eval(input("Please input a number: "))
	if num % 2 != 0:
		num_odd += num
print("The total sum of all the odd number is:", num_odd)
