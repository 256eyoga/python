print("studenst scores")

#cappture students marks in four subjects
python = int(input("enterthe student python marks\n\t"))
if python <= 100 and python >=0:
    cisco = int(input("enterthe student Cisco marks\n\t"))
    repair = int(input("enter the student Reapair and maintenance marks\n\t"))
    islam = int(input("entert he student Islam marks\n\t"))
else:
    print("Marks out of range!!!")

#calculations
total_scores = (python + cisco + repair + islam)
average = int(total_scores/4)

print(f"thetotal scores are : {total_scores}")
print(f"average marks ={average}")
