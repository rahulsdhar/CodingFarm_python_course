#Data
#Student Management System
#DSA

StudentA_Roll='11'
StudentA_Name="Rahul"
StudentA_Marks="70"

StudentB_Roll='12'
StudentB_Name="Subham"
StudentB_Marks="80"

StudentA={"Name":"Rahul","Roll":'11',"Marks":70}
StudentB={"Name":"Subham","Roll":'12',"Marks":90}
StudentC={"Name":"Suman","Roll":'13',"Marks":80}

sel=StudentA if StudentA["Marks"]>StudentB["Marks"] else StudentB

print(sel["Name"],sel["Roll"],sel["Marks"])


ClassA=[StudentA,StudentB,StudentC]

TotalNumber=len(ClassA)
TotalMarks=0
Topper=StudentA

#0
#Set StudentA -> 0 Add StudentA :: 0 + StudentA = StudentA
#Add StudentB :: StudentA + StudentB
#Add StudentC :: (StudentA + StudentB) +StudentC

for sel in ClassA:
    TotalMarks=TotalMarks+sel["Marks"]
    Topper=sel if sel["Marks"]>Topper["Marks"] else Topper

print("Topper:", Topper)
print("Average:", TotalMarks/TotalNumber)