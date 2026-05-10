country = {
"Nepal" : "Kathmandu" ,
"India" : "New Delhi",
"Japan" : "Tokyo",
"France" : "Paris",
"Australia" : "Canberra"
}
for key in country.keys():
    print(key)
    
for value in country.values():
    print(value)
    
name = input("Dear user please enter a country name: ")
if name in country:
    print("yes it is present in dictionary")
else:
    print("No country you name is not present there")