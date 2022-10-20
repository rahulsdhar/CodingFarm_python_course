Required_Attendance=80
Total_Days=20

class Student:
    def __init__(self, n,r,m,p):
        self.Name = n
        self.Roll = r
        self.Marks = m
        self.Present = p

    def show(self):
        print("Name: ",self.Name)
        print("Roll: ",self.Roll)
        print("Marks: ",self.Marks)
        print("Present: ",self.Present)

    def CalculateAttendance(self, Total_Days, Required_Attendance):
        Present_Attendance = (self.Present / Total_Days) * 100
        print("Total Days Present:", self.Present)
        print("Current Attendance:", Present_Attendance)
        if Present_Attendance >= Required_Attendance:
            # R = (P/T+x)*100
            # T + x = P/R * 100
            # x = (P/R * 100) - T
            x = int(self.Present / Required_Attendance * 100 - Total_Days)  # Type_Casting
            if x == 0:
                print("Attendance is Perfect!")
            else:
                print("Attendance Satisfied")
                print("Can Take Leave for ", x, " days")
        else:
            print("Attendance Not Satisfied!")
            # x days are required
            # A = [ (P+x) / (T+x) ] * 100
            # A/100 = (P+x) / (T+x)
            # A(T+x)/100 = P + x
            # AT/100 + Ax/100 = P + x
            # AT/100 - P = x - Ax/100
            # AT/100 - P = x (1 - A/100)
            # x = (AT/100 - P) / (1 - A/100)
            x = ((Required_Attendance * Total_Days) / 100 - self.Present) / (1 - Required_Attendance / 100)
            print("Required Cover-up Attendance:", x)
        print()
        return Present_Attendance, x

class Subject:
    def __init__(self,n,r,t):
        self.Name=n
        self.Required_Attendance=r
        self.Total_Days=t
        self.Students=[]

    def registerStudent(self, newStudent):
        if isinstance(newStudent, Student):
            self.Students.append(newStudent)
        else:
            raise(TypeError)

    def ShowAttendance(self):
        for s in self.Students:
            s.show()
            s.CalculateAttendance(self.Total_Days, self.Required_Attendance)

A=Student("Rahul",11,70,5)
B=Student("Subham",15,80,10)
C=Student("Rony",13,60,15)
D=Student("Ram",17,77,4)

English = Subject("English", 80, 20)

English.registerStudent(A)
English.registerStudent(C)
English.registerStudent(D)

English.ShowAttendance()