print("""
Please Choose your code:
1 for Manager
2 for Hourly Worker
3 for Commision worker
4 for Piece Worker""")

employee_code = int(input("Please Enter your pay code: "))
wage = 0

if employee_code == 1:
    wage = int(20000)

elif employee_code == 2:
    hours_worked = int(input("Please Enter hours worked: "))
    if  hours_worked <= 40:
        wage = int(300 * hours_worked)
    else:
        overtime =  (hours_worked - 40)
        pay = int(300 * (hours_worked - overtime))
        ot_rate = float(1.5*300)
        overtime_pay  = float(overtime * ot_rate)
        wage = int((pay + overtime_pay))

elif employee_code == 3:
    total_sales = int(input("Please Enter your weekly sales: "))
    pay = int(250)
    wage =  float(pay + (5.7 * total_sales))

elif employee_code == 4:
     items_produced = int(input("Please Enter your weekly produce: "))
     pay = int(200)
     wage = float(items_produced*pay)
else:
    print("Invalid Employee Code")

print(f"""
Your Employee Code is:  {employee_code}
Your Wages are ${wage}
""")


    



    