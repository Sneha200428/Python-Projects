class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
        else:
            print("Book is not available")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
        else:
            print("Book is not returned yet")

    def display_info(self):
        print("=================================== Book Details ===================================")
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        if self.is_available:
            print("Availability: Available")
        else:
            print("Availability: Borrowed")


