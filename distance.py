distance = int(input("Enter distance covered\n\t"))
rate = int(0)
bill = int(0)

if distance >= 0 and distance <= 10:
    rate = 5000
elif distance > 10 and distance <= 50:
    rate = 10000
elif distance > 50:
    rate = 15000
else:
    print("invalid distance entered")

bill = distance * rate

print(bill)
