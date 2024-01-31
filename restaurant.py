#types of restaurants
print("FANCY RESTAURANT\n")

print("\n")
#meals and costs
meal = input("Enter meal:\n")
quantity = input("Enter quantity of meal:\n")
cost_per_meal = int(10000)
#calcultions
amount = int(quantity) * int(cost_per_meal)
discount = int(amount) * float(0.1)
final_pay = amount-discount

print(f"the meal costs: {amount}\n")
print(f"discounted amount is: {discount}\n")
print(f"the total pay is: {final_pay}")