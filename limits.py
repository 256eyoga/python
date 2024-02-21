print("%" * 60)
print("\tOptions")
print("\t1: programming marks")
print("\t2: Islam and science")
print("\t3: Networking and Cisco")
print("\t4: Statistics")

marks = 0
score = []

for i in range(1,5):
 marks = int(input("\tenter marks\n\t"))
 if marks <= 100 and marks >=0:
  score.append(marks)
 else:
        print("\tinvalid values entered\n\t")
 
print(f"\n\tthe scores are:\n Programming: \t{score[0]}\n Islam:\t\t {score[1]}\n Networking and Cisco: {score[2]}\n Statistics:\t\t {score[3]} Statistics: \n")
print("%" * 60)