#indexing and slicing
name = "Samiksha"

print(name[0])
print(name[-1])
print(name[3:])


#string methods

name = "samiksha Ghimire"
print(name.upper()) #for upper case
print(name.lower()) #for lower case
print(name.title()) #capitalize each word


name2 = "      Hello"
print(name2.strip())  #removes the begininning white spaces

print(name2.replace("l" , "p"))  #replace l with p
print(name.split())  #splits name into list


print(name.find("k"))  #find index

print(name.count("a")) #count occurrence

print(name.startswith("sam"))  #returns true if true then false if it isnt true

print(name.endswith("hjgj"))  

print(name.isdigit()) #print true if correct if not prints false

print(name2.isalpha())

print(len(name)) #prints length of string


print("s" in name)  #print true if its true





#practice question
#Given " python is AWESOME " — strip spaces, title case it, replace "Awesome" with "The Best", print length of result.


hi = "   python is AWESOME"
result =hi.strip().title().replace("AWESOME" , "The Best")
print(result)
print(len(result))



