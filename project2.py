print("welcome to an student organizer data program!!")
print("1 to add student data")
print("2 to display all student")
print("3 to update student information")
print("4  to delete student")
print("5 to display subjects offered")
print("6 to exit")
studentinformation=[]
choice=0
while choice<7:
     choice=int(input("enter your choice: "))
         match choice:
          case 1:
               name=input(("enter your name:"))
               age=int(input("enter your age:"))
               grade=int(input("enter your grade:"))
               subject1=input("enter your subjects:")
               studentid2=int(input("enter your student id:"))
               dateofbirth3=(input("enter your date of birth (yyyy-mm-dd):"))
               print(f"name:{name}  age:{age}   grade:{grade}  subjects:{subject1}  student is:{studentid2}  date of birth (yyyy-mm-dd):{dateofbirth3}")
               subject=set(subject1.split(","))
               studentid=(studentid2,)
               dateofbirth=(dateofbirth3,)
               student={
                    "name_student=":name,
                    "age_student":age,
                    "subject_student":subject,
                    "studentid_student":studentid,
                    "dateofbirth_student":dateofbirth           
                      }
               studentinformation.append(student)
          case 2:
                print("your display is")
                print(studentinformation)
          case 6:
               print("thank you student")
               break
          case 3:
               print("for update")
               studentid_for_update=int(input("enter your student id for changes:"))
               for i in range(len(studentinformation)):
                    if(studentid_for_update==studentinformation[i].get("studentid_student")):
                         i+=1
                         print("1 for updating name")
                         print("2 for updating grade")
                         print("3 for updating age")
                         c=int(input("enter your choice"))
                         match c:
                           case 1:
                            name1=input("enter your name")
                            name=name1
                           case 2:
                            grade1=int(input("enter your grade"))
                            grade=grade1
                           case 3:
                            age1=int(input("enter your age"))
                            age=age1
                           case _ :
                            print("invalid choice")          
          case 4:
              print("give me your delete record")
              del_studentid=int(input("enter your student id:"))
              for i in range(len(studentinformation)):
                   if(del_studentid==studentinformation[i].get("studentid_student:")):
                        del studentinformation[i]
          case 5:
               print("subjects offered are")
               print(" physical education")
               print("maths")
               print("accounts")
               print("economics")
               print("english")
               print("computers")

