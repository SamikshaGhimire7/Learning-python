
#practicing some basics functions question 

#1qn wap using function to greet 
def greet(name):
  
    print(f"Hello,{name}")
  
  
greet("Ram")

#qn write a program using function to get sq of two numbers
def square(num):
 
  print(num**2)
 
 
square(3)


#qn 3 WAP using function to add tw numbers
def add(a , b):
  return a+b

result = add(3 , 4)
print(result)




#qn 4 wap using function to check whether the given number is even or not
def is_even(num):
  if num % 2 == 0:
    return True
    
  else:
   return False
    
conclusion = is_even(56)
print(conclusion)
    
#qn 5 wap using function to find larger among two numbers and print the larger one
def find_larger(a ,b):
  if a>b:
    return a
  
  elif b>a:
    return b
  
  else:
    print("invalid")
    
final = find_larger(24 , 67)
print(final)



#qn 6 multiplication of two numbers using function
def multiply(a ,b):
  return a*b

ans = multiply(45 , 67)
print(ans)


# qn7 Write a function calculate_area(length, width) that returns the area of a rectangle.
def Calculate_area(length , width):
  return length * width

result = Calculate_area(45 , 38)

print(result)

#qn8 Write a function count_vowels(text) that counts how many vowels (a, e, i, o, u) are in a string.
def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count


result = count_vowels("Samiksha")
print(result)

#qn9  Write a function celsius_to_fahrenheit(c) that converts Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    fahrenheit = (c * 1.8) + 32
    return fahrenheit

result = celsius_to_fahrenheit(2000)
print(result)


#qn10 Write a function check_password(password) that returns "Valid" if the password length is at least 8 characters, otherwise "Invalid".
def check_password(password):
  if len(password) >=8:
    return "Valid"
  else:
   return "Invalid"


check_password("Sammiscoding")


#qn11 Write a function factorial(n) that returns the factorial of a number.
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result



