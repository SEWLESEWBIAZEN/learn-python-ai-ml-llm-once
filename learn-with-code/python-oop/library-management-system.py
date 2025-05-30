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
    
    def add_book(self,book):
        self.books.append(book)
        print(f"Book with title {book.title} has been added successfuly!")

    def borrow_book(self,title):
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip() and not book.is_borrowed:
                book.is_borrowed = True
            else:
                print (f"Book with title {book.title} has been borrowed!")
    
    def return_book(self, title):
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip() and  book.is_borrowed:
                   book.is_borrowed = False
            else:
                print (f"Book with title {book.title} has been returned!")

library =  Library()
title= input("Enter title")
author = input("Enter author")

book = Book(title,author)

library.add_book(book)
title= input("Enter title to borrow: ")
library.borrow_book(title)
title= input("Enter title to borrow: ")
library.borrow_book(title)
title= input("Enter title to return: ")
library.return_book(title)