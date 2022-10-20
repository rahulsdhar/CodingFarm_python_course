# Student Management System
# DSA - Data Structure and Algorithm

# Rahul Subham Ram

StudentA_Name= "Rahul"
StudentA_Attendance = 70
StudentA_Marks = 82

StudentB_Name= "Subham"
StudentB_Attendance = 90
StudentB_Marks = 80

StudentC_Name= "Ram"
StudentC_Attendance = 80
StudentC_Marks = 70

StudentA = {"Name": StudentA_Name, "Attendance": StudentA_Attendance, "Marks": StudentA_Marks}
StudentB = {"Name": StudentB_Name, "Attendance": StudentB_Attendance, "Marks": StudentB_Marks}
StudentC = {"Name": StudentC_Name, "Attendance": StudentC_Attendance, "Marks": StudentC_Marks}

sel = StudentA if StudentA["Marks"] > StudentB["Marks"] else StudentB # StudentA VS StudentB
sel = sel if sel["Marks"] > StudentC["Marks"] else StudentC # Winner VS StudentC

print("Topper Name:", sel["Name"])
print("Marks:", sel["Marks"])
print("Attendance", sel["Attendance"])
print()
ClassA = [StudentA,StudentB,StudentC]

# Average Marks = Total Marks / Total Number Of Students

Total_students=len(ClassA)

Total_Marks=0

for x in ClassA:
    Total_Marks = Total_Marks + x["Marks"]

Avg_Marks = Total_Marks/Total_students
print("Average Marks: ", int(Avg_Marks))
