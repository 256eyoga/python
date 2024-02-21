print("wage system")

age = int(input("Enter age:\n"))
gender = str(input("Enter gender (male / female):\n"))
days_worked = int(input("Enter days worked:\n"))
rate = 0

if age >= 18 and age <= 29:
    if gender.lower()== "male":
        rate = 15000
    elif gender.lower() == "female":
        rate == 20000
    else:
        print("Invalid gender")
elif age >=30 and age <= 49:
    if gender.lower()== "male":
        rate = 30000
    elif gender.lower() == "female":
        rate == 35000
    else:
        print("Invalid gender")
else:
    print("Invalid age rage!")

wage = days_worked * rate

print(f"The wage is:\t {wage}")