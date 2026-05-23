#Login system
correct_user = "Samiksha"
correct_password = "sammy343"
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_user and password == correct_password:
  print("Access Granted!")
  
elif username == correct_user and password != correct_password:
  print("Wrong password")
  
else:
  print("User not found")