
from insert import insertdata
from update import updatedata
from delete import deletedata
from read import readdata

obj = insertdata()
obj1 = updatedata()
obj2 = deletedata()
obj3 = readdata()

print("--------------------------------- STUDENT MANAGEMENT SYSTEM ----------------------------------")

print("For Insertion ----> Press 1,\n Updation ----> Press 2,\n Deletion ----> Press 3,\n Reading ----> Press 4")

num = int(input("Please enter your options: "))

if num == 1:
    print("For Student Info -----> Press 1 \nFor Course -----> Press 2 \nFor Transaction -----> Press 3")
    n = int(input("Please enter your option: "))
    if n ==1:
        sid = int(input("Please enter your ID: "))
        sname = input("Please enter your Name: ")
        email = input("Please enter your Email ID: ")
        city = input("Please enter your City: ")
        obj.insertstudent(sid, sname, email, city)

    if n == 2:
        cid = int(input("Please enter your Course ID: "))
        coursename = input("Please enter your Course Name: ")
        sid = int(input("Please enter your ID: "))
        price = float(input("Please enter the Price: "))
        obj.insertcourse(cid, coursename, sid, price)

    if n == 3:
        tid = int(input("Enter Transaction ID: "))
        sid = int(input("Enter Student ID: "))
        cid = int(input("Enter Course ID: "))
        method = input("Enter the mode of payment: ")
        obj.inserttransactions(tid, sid, cid, method)

if num == 2:
    print("To update Student Table -----> Press 1\nTo update Course Table -----> Press 2\nTo update Transaction Table -----> Press 3")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        field = input("For Updation \nEnter 1 for Name\nEnter 2 for Email\nEnter 3 for City\nEnter your Choice : ")

        if field == '1':
            sid = int(input("Enter student ID: ")) 
            new_value = input("Enter new name: ")
            obj1.updatestudent( field, sid, new_value)

        if field == '2':
            sid = int(input("Enter student ID: "))
            new_value = input("Enter new email: ")
            obj1.updatestudent(field, sid, new_value)

        if field == '3':
            sid = int(input("Enter student ID: "))
            new_value = input("Enter new city: ")
            obj1.updatestudent(field, sid, new_value)

    if choice == 2:
        field = input("For Updation \nEnter 1 for CourseID\nEnter 2 for Course Name\nEnter 3 for Course Price\nEnter your Choice : ")

        if field == '1':
            sid = int(input("Enter student ID: ")) 
            new_value = int(input("Enter new CourseID: "))
            obj1.updatecourse( field, sid, new_value)

        if field == '2':
            sid = int(input("Enter student ID: "))
            new_value = input("Enter new Course Name: ")
            obj1.updatecourse(field, sid, new_value)

        if field == '3':
            sid = int(input("Enter student ID: "))
            new_value = float(input("Enter new Course Price: "))
            obj1.updatecourse(field, sid, new_value)

    if choice == 3:
        field = input("For Updation \nEnter 1 for Transaction ID\nEnter 2 for Course ID\nEnter 3 for Transaction Method\nEnter your Choice : ")

        if field == '1':
            sid = int(input("Enter student ID: ")) 
            new_value = int(input("Enter new Transaction ID: "))
            obj1.updatetransaction( field, sid, new_value)

        if field == '2':
            sid = int(input("Enter student ID: "))
            new_value = input("Enter new Course ID: ")
            obj1.updatetransaction(field, sid, new_value)

        if field == '3':
            sid = int(input("Enter student ID: "))
            new_value = input("Enter new Transaction Method: ")
            obj1.updatetransaction(field, sid, new_value)

if num == 3:
    print("To delete Student Info -----> Press 1 \n To delete Course Info -----> Press 2 \n To delete Transaction Info -----> Press 3")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        sid = int(input("Enter student ID to delete: "))
        obj2.deletestudent(sid)

    if choice == 2:
        cid = int(input("Enter Course ID to delete: "))
        obj2.deletecourse(cid)

    if choice == 3:
        tid = int(input("Enter Transaction ID to delete: "))
        obj2.deletetransaction(tid)
    
if num == 4:
    print("To Print Student Info -----> Press 1\nTo Print Course Info -----> Press 2\nTo Print Transaction Info -----> Press 3")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        sid = int(input("Enter the Student ID: "))
        obj3.readstudent(sid)

    if choice == 2:
        cid = int(input("Enter the Course ID: "))
        obj3.readcourse(cid)
    
    if choice == 3:
        sid = int(input("Enter the Transaction ID: "))
        obj3.readtransaction(sid)

    