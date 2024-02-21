marks = []

for i in range(1,5):
 scores = int(input(f"enter students score:\n"))
 marks.append(scores)

print(marks)

total = sum(marks[:5])
average = int(total/len(marks))
print(total)
print(average)