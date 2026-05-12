
#using parameters and arguments
def student_info(name , age , course):
  print("Name: " + name )
  print("\nAge : " + str(age))
  print("\nCourse: " + course)
  
student_info("Samiksha" , 19 , "Bsc.csit")
  
student_info("tony" , 20 , "Bsc.csit")
  
student_info("peter" , 19 , "Bsc.csit")
  
  
  #using function with conditional statements
def calculate(a , b , operator):
  if operator == "+":
    return a + b
  elif operator == "-":
   return a - b
 
  elif operator == "*":
    return a * b
  
  elif operator == "/":
   return a/b 
 
  else:
   print("operator is invalid")
print(calculate(12 , 13 , "+"))
print(calculate(12 , 13 , "-"))
print(calculate(12 , 13 , "*"))
print(calculate(12 , 13 , "/"))
print(calculate(12 , 13 , "%"))


#using default parameters
def make_coffee(coffee_type , size = "medium"):
  print("Making a " + size + coffee_type)
  
  
make_coffee("latte")
make_coffee("Espresso" , "large ")
make_coffee("Americano" , "medium ")



#with global variable (anywhere in function)
bank_balance = 10000
def deposit(amount):
  print( bank_balance + amount)
  
  
def withdraw(amount):
  result =bank_balance - amount
  if result < 0:
    print("Warning")
    
  else:
   print(result)
  


deposit(234)
withdraw(15000)

