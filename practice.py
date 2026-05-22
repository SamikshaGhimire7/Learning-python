x = 43
print(x)
print(type(x))
print(isinstance(x , float))

#Typeconversion
print(float(x))
print(str(x))
print(bool(x))


#swapping two variables 
a , b = 10 , 20
a,b = b , a
print(a , b)



#Create variables for your name, age, height (float), and is_student (bool). Print each with its type.

name = input("Enter a name: ")
age = int(input("Enter your age:  "))

height = float(input("Enter your height: "))

is_student = True

print(name , type(name))
print(age , type(age))
print(height , type(height))



#A product costs Rs. 1500. Apply a 15% discount and print: "Original: 1500 | Discount: 225.0 | Final: 1275.0"

product_cost = 1500
discount = (15/100)*1500
after_discount = product_cost - discount
print(f"The discount is: {discount}")
print(f"Cost after discount is: {after_discount}")





#Predict the output (without running): print(True + True + False), print(bool("")), print(bool("False")). Then verify and explain why!

print(True + True + False)  #true = 1 and false = 0 so we get 2
print(bool("")) #false as empty string = false
print(bool("False"))  #True as non empty string is always true