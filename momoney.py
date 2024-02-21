print("options")
print("""
1. Deposit
2. Withdraw
3. Check balance""")

option = int(input("Please, Enter a number of ervice required"))
deposit_amount = 0
withdraw_amount = 0
new_balance = 0
balance = 1000000

if option == 1:
    deposit_amount = int(input("Enter Amount to be deposited:\n"))
    if deposit_amount > 5000:
        new_balance = balance + deposit_amount
    else:
        print("Lease deposit  amount is '5000'")
elif option == 2:
    withdraw_amount = int(input("Enter Amount to be Withdrawn:\n"))
    if withdraw_amount < balance:
        new_balance = balance - withdraw_amount
    else:
        print("Insufficient account balance")
elif option == 3:
        print(f"Your current account balance is:\n\t{balance}")
else:
     print("Invalid Option")