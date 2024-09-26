class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    raise Exception("Book is already borrowed")
                book.is_borrowed = True
                return
        raise Exception("Book not found")

    def view_available_books(self):
        return [book for book in self.books if not book.is_borrowed]
