user ={
    "Name" : "Samiksha Ghimire" ,
    "Age" : 19 ,
    "country" : "Nepal" ,
    "hobby" : "Nothing" ,
    "language" : "Nepali"
}
print(user)
print(user["Name"])
user["Age"] = 20 
del user["hobby"]
print(user.keys())
print(user.values())

