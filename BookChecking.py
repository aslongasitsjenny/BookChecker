def create_tuple(l):
  items = l.split(", ")

  return tuple(items)

def get_year(book):
  try:
    return int(book[4])
  except ValueError:
    return 0

def update_book(books):
  # Prompt the user for the ISBN of the book to update
  isbn = input("Enter the ISBN of the book to update: ")

  # Search the list of books for a match
  for book in books:
    if book[3] == isbn:
      # Book found - prompt the user for updated details
      if book[0] == "1":
        title = input("Enter the updated title: ")
        publisher = input("Enter the updated author: ")
        year = input("Enter the updated year published: ")

        # Create a new tuple with the updated book information
        updated_book = ("1", title, publisher, isbn, year)
        i = books.index(book)
        books[i] = updated_book
        print("All done!")
      else:
        print("You do not have permission to update book details")
        
filename = input("Enter a filename and path: ")

try:
  f = open(filename, "r")
  books = []

  for line in f:
    books.append(create_tuple(line))

  f.close()

except:
  print("Error: Could not open file")
  exit()

while True:
  # Print the available options
  print("\nOptions:")
  print("1. Print all book information")
  print("2. Enter a book")
  print("3. Search for book by ISBN")
  print("4. Search for a book by upper and lower year")
  print("5. Update Book")
  print("6. Quit")
  
  # Prompt the user to choose an option
  option = input("\nEnter an option: ")

  # Handle the user's chosen option
  if option == "1":
    # Print all book information
    print("\nBook Information:")
    for book in books:
      print("Access: " + book[0])
      print("Title: " + book[1])
      print("Publisher: " + book[2])
      print("ISBN: " + str(book[3]))
      print("Year published: " + str(book[4]))
  elif option == "2":      

    access = input("Enter the book's access: (1 or 0) ")
    if access not in ["1", "0"]:
        print("Error: access must be 1 characters or less, including spaces.")
        access = input("Enter the book's access again: ")
    
    title = input("Enter the book's title: ")
    if len(title) > 50:
        print("Error: author must be 10 characters or less, including spaces.")
        title = input("Enter the title again: ")
        
    publisher = input("Enter the book's publisher: ")
    if len(publisher) > 10:
        print("Error: publisher must be 10 characters or less, including spaces.")
        publisher = input("Enter the publisher again: ")
    
    isbn = input("Enter the book's ISBN: ")
    if not isbn.isdigit() or len(isbn) > 5:
        print("Error: ISBN must be a maximum of 5 digits.")
        isbn = input("Enter the book's ISBN again: ")
    
    else:
        year = input("Enter the book's year: ")
        if not year.isdigit() or len(year) > 4:
            print("Error: year must be a maximum of 4 digits.")
            year = input("Enter the book's year again: ")
    

    # Reopen the file for writing
    f = open(filename, "a")

    # Write a new line with the book's information
    f.write("\n" + access + ", " + title + ", " + publisher + ", " + isbn + ", " + year)

    f.close()
    
  elif option == "3":
    isbn = input("Enter the book's ISBN: ")
    for book in books:
      if book[3] == isbn:
        print("Access: " + book[0])
        print("Title: " + book[1])
        print("Publisher: " + book[2])
        print("ISBN: " + str(book[3]))
        print("Year published: " + str(book[4]))
  elif option == "4":
      
    lower = input("Enter the lower bound for the publishing year: ")
    if not lower.isdigit() or len(lower) > 5:
        print("Error: Lower bound must be a maximum of 5 digits.")
        lower = input("Enter the lower bound again: ")
    else:
            upper = input("Enter the upper bound for the publishing year: ")
            if not upper.isdigit() or len(upper) > 5:
                print("Error: upper bound must be a maximum of 5 digits.")
                upper = input("Enter the upper bound again: ")


    sorted_books = sorted(books, key=get_year, reverse=True)

    filtered_books = [book for book in sorted_books if lower <= book[4] <= upper]

    for book in filtered_books:
          print("Access: " + book[0])
          print("Title: " + book[1])
          print("Publisher: " + book[2])
          print("ISBN: " + str(book[3]))
          print("Year published: " + str(book[4]))

  elif option == "5":
      update_book(books)

  elif option == "6":
      userinputforquit = input("Are you sure you want to quit, Yes or No")
      if userinputforquit == "Yes":
       quit()

