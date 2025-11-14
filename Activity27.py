print("Adding Data to Dictionary")
print("===================================")
tuloy = True

empty_dictionary = {}

def print_anime():
    for i,j in empty_dictionary.items():
        print(f"CODE {i} TITLE -- {j}")

def pang_search(key):
    print("Searching....")
    print(f"results shows {empty_dictionary[key].upper()} on our database")


while tuloy == True:
    keys = input("Input a keys for this anime --->")
    value = input("Enter anime title ---> ")

    
    empty_dictionary[keys] = value

    choice = input("Would you like to continue adding anime \ny- YES\nn- NO\np- PRINT\ns-SEARCH ---> ").lower()
    if choice == 'y':
        print("Continuing...")
        continue
    elif choice == 'n':
        print("program stops")
        break
    elif choice == "p":
        print_anime()
        continue
    elif choice == "s":
        code = input("Please input the code of the anime ---> ")
        pang_search(code)
    else:
        print("Error")
        continue