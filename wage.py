print("\t\tWAGE CALCLUTION SYSTEM")

workers_name = input("enter workers name: \n")
hours_worked = input("enter hours worked by employee: \n")
RATE = int(30000)

#calculations
wage = int(hours_worked) * RATE
allowance = wage * float(0.05)
gross_wage = allowance + wage
tax = gross_wage * float(0.05)
net_wage = gross_wage - tax

#output
print(f"WAGE Earned IS:\n {wage},\nALLOWANCE Earned IS:\n {allowance},\nGROSS WAGE Earned IS:\n {gross_wage},\nTAXES: \n{tax},\nNET WAGE Earned IS:\n {net_wage}")
