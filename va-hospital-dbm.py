#importing the mysql connector to establish Python-MySQL connectivity
import mysql.connector as mc
cn=mc.connect(host="localhost",user="root",password="vjm")
cur=cn.cursor()


#creating all the required tables for the VA hospital
cur.execute("use VA_Hospital")
cur.execute("create table patients(pid int(10) primary key,name varchar(30),mobile int(15),age int(3),city varchar(50),doc_rec varchar(30))")
cur.execute("create table doctors(name varchar(30) primary key,department varchar(40),age int(2),city varchar(30),mobile varchar(15),fees int(10),salary int(10))")
cur.execute("create table nurses(name varchar(30) primary key,age int(2),city varchar(30),mobile varchar(15),salary int(10))")
cur.execute("create table workers(name varchar(30) primary key,age int(2),city varchar(30),mobile varchar(15),salary int(10))")
cur.execute("create table users(username varchar(30) primary key, password varchar(30))")

print("""
       ================================
                 The VA Hospital
       ================================
""")
print()


#Creating the sign-up page function
def sign_up():
   print("Welcome! Please create a username and password\n")
   u=input("Enter New User Name: ")
   p=input("Create password (Combination of Letters, Digits etc.): ")


#Making it necessary to re-enter password for added security
   p2=input("Re enter password: ")
   if p==p2:
    if len(p)>8:
       cur.execute("insert into users values('"+u+"','"+p+"')")
       cn.commit()
       print("New account created !")


       #Attaching a built-in Cybersecurity feedback measure
       #Attaching a built-in Cybersecurity feedback measure
       if len(p)==8:
                print("Password Strength: Moderate")
       elif 8 < len(p) < 10:
                print("Password Strength: Decent")
       elif 10 < len(p) < 13:
                print("Password Strength: Good")
       elif 13 < len(p) < 16:
                print("Password Strength: Great")
       elif len(p)==16:
                print("Password Strength: Amazing")
       elif len(p)>16:
                print("Super Password ! You are a certified Cybersecurity Master !") 
       else:
            print("Sorry, Password is too short") 
    else:
        print("Sorry, Passwords do not match")



#Creating the login page function
def login():
           print("\nWelcome Back! Please enter your username and password\n")
           un=input("Username :")
           ps=input("Password :")
           cur.execute("select password from users where username='"+un+"'")
           rec=cur.fetchall()
           for i in rec:
               a=list(i)
               if a[0]==str(ps):
                       #Extracting information from the users table and checking whether the entered username and password match
                       print("""\n1.Hospital Members 2.Status of Patients 3.Sign Out""")
                       ch=int(input("Enter your choice: \n"))
                       if ch==1:
                               print("""\n1. Show Details 2. Add new member 3. Delete existing member 4. Exit\n""")
                               ch2=int(input("Eter your choice: "))
                               if ch2==1:
                                     print("Would you like the information of\n1. Doctors\n2. Nurses\n3. Workers")
                                     ch3=int(input("ENTER YOUR CHOICE:"))
                                     if ch3==1:
                                           #Displaying the details of Doctors, Nurses, Workers
                                           cur.execute("select * from doctors")
                                           rec=cur.fetchall()
                                           for i in rec:
                                                 print("Details of Doctors: \n",i)
                                                 print()
                                     elif ch3==2:
                                           cur.execute("select * from nurses")
                                           rec=cur.fetchall()
                                           for i in rec:
                                                 print("Details of Nurses: \n",i)
                                                 print()
                                     elif ch3==3:
                                           cur.execute("select * from workers")
                                           rec=cur.fetchall()
                                           print("Details of Workers: \n",i)
                                           print()
                                     else:
                                           print("Invalid option. Try again !")
                               elif ch2==2:
                                      #Adding new Doctors, Nurses, Workers
                                       print("What would you like to add?\n1. Doctor\n2. Nurse\n3. Worker")
                                       ch4=int(input("Enter your choice:"))
                                       if ch4==1:
                                               n=int(input("How many Doctors would you like to add? "))
                                               for i in range(n):
                                                       name=input("Enter name of doctor:")
                                                       dep=input("Enter department:")
                                                       age=input("Enter age:")
                                                       city=input("Enter city doctor belongs to:")
                                                       mno=input("Enter 10 digit mobile no.:")
                                                       fees=input("Enter fees:")
                                                       sal=input("Enter Salary of doctor:")
                                                       docrec=(name,dep,age,city,mno,fees,sal)
                                                       cur.execute(f"insert into doctors values{docrec}")
                                                       cn.commit()
                                                       print("New doctor details added successfully. ")
                                                       print()
                                       elif ch4==2:
                                               n=int(input("How many Nurses would you like to add? "))
                                               for i in range(n):
                                                       name=input("Enter name of nurse:")
                                                       age=input("Enter age:")
                                                       city=input("Enter city nurse belongs to:")
                                                       mno=input("Enter mobile no.:")
                                                       sal=int(input("Enter salary:"))
                                                       nurserec=(name,age,city,mno,sal)
                                                       cur.execute(f"insert into nurses values{nurserec}")
                                                       cn.commit()
                                                       print("New nurse details has been added successfully.")
                                                       print()
                                       elif ch4==3:
                                               n=int(input("How many Workers to be added? "))
                                               for i in range(n):
                                                     name=input("Enter name of worker:")
                                                     age=input("Enter Age:")
                                                     city=input("Enter city:")
                                                     mno=input("Enter mobile no:")
                                                     ms=input("Enter Salary:")
                                                     workerrec=(name,age,city,mno,ms)
                                                     cur.execute(f"insert into workers values{workerrec}")
                                                     cn.commit()
                                                     print("New worker details added successfully.")
                               elif ch2==3:
                                      #Deleting Doctors, Nurses, Workers
                                      print("What would you like to delete? \n1. Doctor\n2. Nurse\n3. Patient\n")
                                      c=int(input("Enter your choice:"))
                                      if c==1:
                                             name=input("Enter doctor name to delete:")
                                             cur.execute("select * from doctors where name='"+name+"'")
                                             rec=cur.fetchall()
                                             print(rec)
                                             p=input("Are you sure you want to delete this doctor?(Yes/No):")
                                             if p in "YESyesYes":
                                                    cur.execute("delete from doctors where name='"+name+"'")
                                                    cn.commit()
                                                    print("Doctor has been deleted successfully")
                                             else:
                                                print("Error in deletion")
                                      elif c==2:
                                            name=input("Enter nurse name to delete:")
                                            cur.execute("select * from nurses where name='"+name+"'")
                                            rec=cur.fetchall()
                                            print(rec)
                                            p=input("Are you sure you want to delete this nurse?(Yes/No):")
                                            if p in "YESyesYes":
                                                    cur.execute("delete from nurses where name='"+name+"'")
                                                    cn.commit()
                                                    print("Nurse has been deleted successfully")
                                            else:
                                                print("Error in deletion")
                                      elif c==3:
                                            name=input("Enter worker name to delete:")
                                            cur.execute("select * from workers where name='"+name+"'")
                                            rec=cur.fetchall()
                                            print(rec)
                                            p=input("Are you sure you want to delete this worker?(Yes/No):")
                                            if p in "YESyesYes":
                                                    cur.execute("delete from workers where name='"+name+"'")
                                                    cn.commit()
                                                    print("Worker has been deleted successfully")
                                            else:
                                                print("Error in deletion")
                       
                               elif ch2==4:
                                      print("Thank you! Have nice Day!")
                                      break
                       elif ch==2:
                             #The Patient manager system
                              print("""\n1. Show patient record 2. Admit new patient 3. Discharge Patient 4. Exit\n""")
                              b=int(input("ENTER YOUR CHOICE:"))
                              if b==1:
                                    cur.execute("select * from patients")
                                    rec=cur.fetchall()
                                    for i in rec:
                                           print("Patient Details: \n",i)
                              elif b==2:
                                    pid=str(input("Enter patient id: "))
                                    name=str(input("Enter name of patient: "))
                                    age=str(input("Enter age: "))
                                    city=str(input("Enter City: "))
                                    mn=str(input("Enter Mobile no.: "))
                                    cur.execute("select name from doctors")
                                    rec=cur.fetchall()
                                    print(rec)
                                    dr=str(input("Enter doctorname to be recommended:"))
                                    cur.execute ("insert into patients values('"+str(pid)+"','"+str(name)+"','"+str(mn)+"','"+str(age)+"','"+str(city)+"','"+str(dr)+"')")
                                    cn.commit()
                                    print("\nNew Paitent has been Admitted\n")
                              elif b==3:
                                     name=input("Enter the name of patient to discharge:")
                                     cur.execute("select * from patients where name='"+name+"'")
                                     rec=cur.fetchall()
                                     print(rec)
                                     
                                     #Checking whether patient has paid his hospital bills before being discharged
                                     bill=input("Has the patients bill been paid (Yes/No)")
                                     if bill in "YESyesYes":
                                            cur.execute("delete from patients where name like'%"+name+"%'")
                                            print("\nYou may discharge the patient.\n")
                                            cn.commit()
                                     elif bill in "NOnoNo":
                                            print("Please pay your pending bill amount to discharge patient.")
                                     else:
                                            print("Bill payment status is unknown....")
                              elif b==4:
                                      print("Thank you! Have nice Day!")
                                      break
               else:
                       print("Username and Password not Found !")


#Creating the password change function
def change_pass():
  cur.execute("select username from users")
  rec=cur.fetchall()
  for i in rec:
     v=list(i)
     k=["USERNAME"]

     #using the zip function: attaching the k to v in order to create a key-value pair in the dictionary
     d=dict(zip(k,v))
     print(d)
     u=input("Enter username to change password from above:")
     if u in d.values():
            p=input("Enter New Password:")
            p2=input("Re enter password: ")
            if p==p2:
                   if len(p)>8:
                        #Attaching a built-in Cybersecurity feedback measure
                          if len(p)==8:
                                 print("Password Strength: Moderate")
                          elif 8 < len(p) < 10:
                                 print("Password Strength: Decent")
                          elif 10 < len(p) < 13:
                                 print("Password Strength: Good")
                          elif 13 < len(p) < 16:
                                 print("Password Strength: Great")
                          elif len(p)==16:
                                 print("Password Strength: Amazing")
                          elif len(p)>16:
                                 print("Super Password ! You are a certified Cybersecurity Master !") 
                   else:
                          print("Sorry, Password is too short") 
            else:
                print("Sorry, Passwords do not match")
                cur.execute("insert into users values('"+u+"','"+p+"')")
                cn.commit()
                print("New account created !")
        



#Using File Concept
def hospinfo():
      f1=open(“Hospinfo.txt”,”r”)
      r=f1.read()
      print(r)

#The Main Page
while True:
  print("\n1. Sign Up(New User)\n2. Log in\n3. Change Password\n4. Hospital Information\n5. Exit")
      print()
      choice=int(input("Enter your choice: "))
      if choice==1:
        sign_up()
      elif choice==2:
        login()
      elif choice==3:
        change_pass()
      elif choice==4:
        hospinfo():
      elif choice==5:
       print("Thank you for using VA Hospital, Have a nice day!")
       break
      else:
        print("Invalid option! Try Again!")
              

        
