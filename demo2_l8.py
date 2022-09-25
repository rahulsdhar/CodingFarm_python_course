#demo2_l8
# Subham

if __name__ == "__main__":
    print("Hello from demo2_l8")
    import demo_l8
    print("Exited from demo2_l8")
else:
    print("IMPORTED DEMO2")
Required_Attendance = 80

def CalculateAttendance( Days_Present,Total_Days ):
    Present_Attendance = (Days_Present/Total_Days)*100
    print("Total Days Present:",Days_Present)
    print("Current Attendance:", Present_Attendance)
    if Present_Attendance >= Required_Attendance:
        # R = (P/T+x)*100
        # T + x = P/R * 100
        # x = (P/R * 100) - T
        x = int(Days_Present/Required_Attendance * 100 - Total_Days) # Type_Casting
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
        x = ( (Required_Attendance * Total_Days) / 100 - Days_Present) / (1 - Required_Attendance/100)
        print("Required Cover-up Attendance:", x)
    print()
    return Present_Attendance, x
