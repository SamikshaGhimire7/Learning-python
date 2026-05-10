library = {
  "name" : "Samiksha",
  "library_name" : "Genius World"
}
books = []
number = int(input("Dear user , how many books you want to add?  "))
i = 0
while i < number:
  title = input("Enter title of book: ")
  author = input("Enter name of the author: ")
  year = int(input("Enter year: "))
  available = input("Enter availablity of book") == "True"
  books.append({"title" : title , "author": author , "year": year , "available" : available})
  i = i + 1


while True:
  print("1.show all books:")
  print("2.search book by title: ")
  print("3. Show only available books:")
  print("4. Show books by author:")
  print("5. Count total books:")
  print("6. Newest book:")
  print("7. Oldest book:")
  print("8. Exit:")
    
  choice = int(input("Enter your choice: "))
  if choice == 1:
    for book in books:
        print(book["title"], "-", book["author"], "-", book["year"], "-", book["available"])

  elif choice == 2:
   search = input("Enter title to search: ")
  found = False
  for book in books:
        if search == book["title"]:
            print("Found!", book["title"], "by", book["author"])
            found = True
            break
  if not found:
        print("Book not found!")

  elif choice == 3:
    for book in books:
        if book["available"] == True:
            print(book["title"], "-", book["author"])

  elif choice == 4:
    search = input("Enter author name: ")
    for book in books:
        if search == book["author"]:
            print(book["title"], "-", book["year"])

  elif choice == 5:
    print("Total books:", len(books))

  elif choice == 6:
    newest = books[0]["year"]
    for book in books:
        if book["year"] > newest:
            newest = book["year"]
    print("Newest book year:", newest)

  elif choice == 7:
    oldest = books[0]["year"]
    for book in books:
        if book["year"] < oldest:
            oldest = book["year"]
    print("Oldest book year:", oldest)

  elif choice == 8:
    print("Goodbye!")
    break