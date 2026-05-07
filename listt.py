numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7]
print(numbers[0:3])   #first three elements
print( numbers[-3:]) #last three elements
numbers.reverse()
print(numbers)

print(numbers[::2])  #every second number

names = ["Tony" , "sammy" , "peter" , "Bruce" , "steve"]
user = input("Enter your name: ")
if user in names:
  print("Found!")
else:
  print("Not found")

 
sun = []
for i in range(5):
  user_2 = int(input("Enter 5 numbers: "))
  sun.append(user_2)

print(sun)
print(sun[::-1]) #reverse slicing
print(sun[0:3])

min(sun)
print(min(sun))
max(sun)
print(max(sun))
 