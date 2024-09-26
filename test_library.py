import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book =  Book("B001", "Zero to One", "Peter Thiel", 2014)
        library.add_book(book)
        self.assertIn(book, library.books)
    def test_borrow_book(self):
        library = Library()
        book = Book("123", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book("123")
        self.assertTrue(book.is_borrowed)

    def test_borrow_unavailable_book(self):
        library = Library()
        book = Book("123", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book("123")
        with self.assertRaises(Exception):
            library.borrow_book("123")

    def test_return_book(self):
        library = Library()
        book = Book("123", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book("123")
        library.return_book("123")
        self.assertFalse(book.is_borrowed)
    
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    raise Exception("Book is not borrowed")
                book.is_borrowed = False
                return
        raise Exception("Book not found")



if __name__ == '__main__':
    unittest.main()