
name = input("USER KINDLY INPUT YOUR NAME: ")
subject = int(input("How many subjects you have? "))
total = 0
for i in range(1 , subject+1):
  marks = float(input("Enter marks for subject" + str(i)+ ":"))


total = total + marks
average = total/subject
print("STUDENT: " , name)
print("TOTAL MARKS: ", total)
print("AVERAGE: " , average)

