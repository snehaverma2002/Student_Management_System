# Student Management System
student_list = []

sms=open("student_database.txt","a+")
# Function to view all students from the file
def view_student():
    sms=open("student_database.txt", "r") 
    for i in sms:
        print(i)
    sms.close()

# Function to add a new student to the list and file
def add_student():
    sms=open("student_database.txt","a+")
    a=input("Enter new Student name:")
    a=a+'\n'
    sms.write(a)
    print("Student name Added!!")
    sms.close()
    
# Function to remove a student from the list and file
def remove_student():
    sms=open("student_database.txt","a+")
    a=input("Enter student name for remove:")
    a=a+'\n'
    sms.seek(0)
    rn=sms.readlines()
    if a in rn:
        rn.remove(a)
        print("Removed student name from list:",a)
        s=''
        s=''.join([str(i) for i in rn])
        f1=open("student_database.txt","w")
        f1.write(s)
        f1.close()
    else:
        print("Student name not found!")
    sms.close()
# Function to search for a student in the list
def search_student():
    sms=open("student_database.txt","r")
    a=input("Search student name:")
    readfile=sms.read()
    if a in readfile:
        print("Student name found")
    else:
        print("Student name not found")
    sms.close()
while True:
    print("_______________________________________________________________")
    print("\n***STUDENT MANAGEMENT SYSTEM***")
    print("_______________________________________________________________")
    print("\nPlease choose an option:")
    print("1. To view a Student")
    print("2. To add students")
    print("3. To remove a student")
    print("4. To search for a student")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == '1':
        view_student()
    elif choice == '2':
        add_student()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        search_student()
    elif choice == '5':
        exit()
    else:
        print("Invalid choice. Please choose a valid option!")

    g = input("Do you want to continue (y/n): ")
    if g == 'y':
        continue
    elif g=='n':
        break
