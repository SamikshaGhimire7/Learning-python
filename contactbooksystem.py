contacts = []
num = int(input("user , how many contacts you want to add? "))

for i in range(num):
  name = input("Enter contact name: ")
  phonenum =int(input("Enter phone number: "))
  store = name + "-" + str(phonenum)
  contacts.append(store)
  
print(contacts)
print(len(contacts))

search = input("Enter name to search: ")
if search in contacts:
  print("contact found:)")
else:
  print("contact not found:()")
  
print(contacts[0])
print(contacts[-1])


contacts.sort()
print(contacts)
