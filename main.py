
# Student Study Pattern Tracker

print("================================")
print("     STUDENT DASHBOARD")
print("================================")

Studentid= int(input("Enter Student ID: "))
Studentname=input("Enter your name: ")
Subject1=input("Enter your subject1: ")
Subject2=input("Enter your subject2: ")
Subject3=input("Enter your subject3: ")
NumofHrspersubject1=int(input("Enter how many hrs per subject1 you can read in a day: "))
NumofHrspersubject2=int(input("Enter how many hrs per subject2 you can read in a day: "))
NumofHrspersubject3=int(input("Enter how many hrs per subject3 you can read ina day: "))
Date=input("Enter your date: ")

total_hours=NumofHrspersubject1+NumofHrspersubject2+NumofHrspersubject3
average_hours=total_hours/3
print("Student ID: ",Studentid)
print("Studentname: ",Studentname)
print("Subject: ",Subject1)
print("Subject2: ",Subject2)
print("Subject3: ",Subject3)
print("NumofHrspersubject1: ",NumofHrspersubject1)
print("NumofHrspersubject2: ",NumofHrspersubject2)
print("NumofHrspersubject3: ",NumofHrspersubject3)
print("Date: ",Date)
print("Total hours: ",total_hours)
print("Average hours: ",average_hours)





print("Welcome to Student Study Pattern Tracker")
print("Dashboard project started successfully!")