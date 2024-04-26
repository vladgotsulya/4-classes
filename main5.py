class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

class Borrower:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, library, book):
        if book in library.books:
            library.remove_book(book)
            return f"{self.name} позаимствовал {book.title}"
        else:
            return f"{book.title} недоступен для заимствования"

class ReturnBook:
    def __init__(self):
        pass

    def return_book(self, library, book):
        library.add_book(book)
        return f"{book.title} был возвращен в библиотеку"