isFish=True

while isFish == True:
    confirm = input("Do you wish to fish? yes/no: ").lower()

    if confirm == "yes":
        print("fishing")
        continue

    elif confirm == "no":
        print("Stopping")
        break

    else:
        print("Invalid!")
        continue

