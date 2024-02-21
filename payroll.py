#inputs for the program
employee_name = input("Please, Enter employee name\t\n")
employee_number = int(input("Please, Enter employee number\t\n"))
weekly_sales = int(input("Please, Enter weekly sales\t\n"))

#constants
pay = 1000000
rate = float(0.0)
extra_rate = float(0.0)
bal = 0

#processes for the program
if weekly_sales > 0 and weekly_sales <= 5000000:
    rate = 0.10
    extra_rate = 0
elif weekly_sales > 5000000:
    bal = weekly_sales - 5000000
    rate = 0.10
    extra_rate = 0.15

commission = ((rate * weekly_sales) + (extra_rate * bal) )
total_pay = (pay + commission)

#outputs
print(f"{employee_name} with employee no:\t {employee_number}\n has weekly sales of:\t{weekly_sales} and commission of:\t{commission}")
print(f"total Pay is:\t{total_pay}")