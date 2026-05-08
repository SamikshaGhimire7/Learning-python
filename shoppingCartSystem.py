Cart = []
cart = []
for i in range(5):
 available = input("Enter  available products:")
 price = int(input("Enter price of  product: "))
 print(available)
 Total = available + "-" + str(price)
 Cart.append(Total)
 
 
 
print(Cart)
 
 
item = int(input("Dear user , how many items you want to Buy? "))

for i in range(item):
  product = input("Which product they want to buy: ")
  
  if product in Cart:
    cart.append(product)
    print("Product available")
  else:
    print("Product not available")
    
    
print("Cart: " , cart)
print("Total item bought: " , len(cart))
print(Cart)
Cart.sort()
print(Cart)
print(Cart[0])
print(Cart[-1])