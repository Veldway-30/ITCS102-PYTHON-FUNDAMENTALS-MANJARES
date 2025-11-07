name = input("Hi! What is your name?: ")

print("************************")
print("ODD number compiler: type:", 0, "to terminate the loop")

isODD = True

while isODD == True:
    confirm = eval(input("Please input a number ----> "))

    if confirm % 2 == 1:
        print("Odd number detected")
        odd = confirm + confirm
        continue
    elif confirm % 2 == 0:
        print("Even number detected")

    elif confirm == 0:
        print("Hi ", name,"The total sum of all the ODD Number is", odd)
        break

    else:
        print("Invalid")
        continue
        