user = {
  "name" : "Ram Bahadur" ,
  "monthly_income" : 200000
}
expenses = []
add = int(input("Dear user! How many expenses you want to add? "))

num = 0
while num < add:
 category = input("Enter category: ")
 amount = int(input("Enter amount: "))
 expenses.append({"category" : category , "amount": amount})
 num = num + 1

for expense in expenses:
  print(expense["category"] , ":" , expense["amount"])

total = 0
for expense in expenses:
  total = total + expense["amount"]
print("Total expenses:" , total)

remainingbalance = user["monthly_income"] - total
print("Remaining balance:" , remainingbalance)

if total > user["monthly_income"]:
  print("Warning, You are overspending")
else:
  print("Good job , You are within budget")

for expense in expenses:
  print(expense["category"])