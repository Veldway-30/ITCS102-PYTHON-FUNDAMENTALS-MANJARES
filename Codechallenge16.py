import os

os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("-----------------------------------------------\n")



student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \nA- Add Information\nB-Search a Record\nC-Delete a record \nD-Modify  a record\nE-Exit")

    choice = input("Your choice          --->").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("---------------------------")
        search_code = input("Key search for this student use this pattern(course-IDNO)---> ").lower()
        first_name = input("Input Student First Name: ")
        last_name = input("Input Student last Name: ")
        course = input("Input Student course: ")
        email = input("Input Student email: ")
        isSingle = input("Is student single (True/False)---> ")

        student_records = {search_code : [first_name, last_name, course, email]}
        print("DATA SAVED")
        os.system('cls')
        continue
    elif choice == 'b':
        os.system('cls')
        code = input("Input search code ---> ")

        for j in student_records.keys():
                if code in student_records.keys():
                     print("Record Found")

                     print("RECORD")
                     print("---------------")
                for i in  student_records[code].value():
                          print(i)
        else:
                print("NO RECORD FOUND")
                     
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'c':
         pass
         continue
    elif choice == 'e':
         print("System EXit")
         break