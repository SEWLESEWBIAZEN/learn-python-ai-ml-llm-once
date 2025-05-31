class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        self.status = "Available" if not self.is_borrowed else "Borrowed"
        print("\n----Book Details-----")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self):
        title= input("Enter the title: ")
        author = input("Enter the author: ")
        book = Book(title,author)
        self.books.append(book)
        print(f"Book with title {book.title} has been added successfuly!")

    def borrow_book(self):
        title= input("Enter title to borrow: ")
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip() and not book.is_borrowed:
                book.is_borrowed = True
            else:
                print (f"Book with title {book.title} has been borrowed!")
    
    def return_book(self, title):
        title= input("Enter title to return: ")
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip() and  book.is_borrowed:
                   book.is_borrowed = False
            else:
                print (f"Book with title {book.title} has been returned!")
    
    def view_all_books(self):
        count = 0
        if len(self.books)>0:
            try:
                for book in self.books:
                    count+=1
                    status = "Borrowed" if book.is_borrowed else "Available"
                    print (f"({count}). {book.title} By {book.author} is {status}")
            except:
                print("Error Occured while reading books.\n")
        else:
            print("No book found\n")

def show_menu():
    print("\n-----Select from 1-4--------")
    print("1. Add Book.")
    print("2. Borrow Book.")
    print("3. Return Book.")
    print("4. View all books")
    print("5. Exit")

def choose():
    show_menu()
    try:
        choice = int(input("\nWhat are going to do: "))
        return choice
    except ValueError as e:
        print("Please select valid number, please try again!")
        choose()
        return None   

def main():
    library =  Library()
    while True:
        choice = choose()
        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.borrow_book()
        elif choice == 3:
            library.return_book()
        elif choice == 4:
            library.view_all_books()
        elif choice == 5:
            exit()
        else:
            print("It is not valid choice.\n")
        quit = input("\nEnter q to quit, anything otherwise.")
        if quit.lower() == 'q':
            return

if __name__=="main":
    main()  








