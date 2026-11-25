
# Student Study Pattern Tracker

print("================================")
print("     STUDENT DASHBOARD")
print("================================")
#Reading Student Information
Studentid= int(input("Enter Student ID: "))
Studentname=input("Enter your name: ")
Subject1=input("Enter your subject1: ")
Subject2=input("Enter your subject2: ")
Subject3=input("Enter your subject3: ")
NumofHrspersubject1=int(input("Enter how many hrs per subject1 you can read in a day: "))
NumofHrspersubject2=int(input("Enter how many hrs per subject2 you can read in a day: "))
NumofHrspersubject3=int(input("Enter how many hrs per subject3 you can read ina day: "))
Date=input("Enter your date: ")

total_hours=NumofHrspersubject1+NumofHrspersubject2+NumofHrspersubject3 #Calculating Total number of hrs we are providing for the student
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

#Appling Conditional statemtmens
if total_hours >= 9:
    print("You are maintaining a good study schedule!")
else:
    print("You have to incrase the number of hrs to maintain good study schedule!")




print("Welcome to Student Study Pattern Tracker")
print("Dashboard project started successfully!")