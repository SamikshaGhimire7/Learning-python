students = {
    "student1": {"name": "Sammy", "age": 20},
    "student2": {"name": "sammy", "age": 19}
}

print(students["student1"]["name"])  
print(students["student2"]["age"])   


for key, value in students.items():
    print(key, ":", value)
    
    
    
person = {
    "name": "sammy",
    "hobbies": ["coding", "gaming", "music"]
}

print(person["hobbies"])      
print(person["hobbies"][0])   

# add new hobby
person["hobbies"].append("cooking")
print(person["hobbies"])