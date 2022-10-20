withdrawal_amt = input("Please Enter Your Withdrawal Amount: ")
currency_opt = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
currency_opt.reverse()
rem_curr= int(withdrawal_amt)
while rem_curr>0:
    for sel_currency in currency_opt:
        if sel_currency <= rem_curr:
            rem_curr = rem_curr - sel_currency
            print("Rs.",sel_currency," Dispensed")
            break

#print("Rs. 100 Dispensed")