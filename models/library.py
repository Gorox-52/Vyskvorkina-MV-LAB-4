from .book import Book
from .collection import BookCollection, IndexDict

class Library:
    def __init__(self):
        self.books = BookCollection()
        self.indexes = IndexDict()

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты Book")
        
        try:
            self.books.add_book(book)
            
            self.indexes[book.isbn] = book
            
            return True
            
        except (ValueError, KeyError) as e:
            print(f"Ошибка при добавлении книги: {e}")
            return False
        
    def remove_book(self, book_or_isbn):
        removed_from_collection = self.books.remove_book(book_or_isbn)
        
        if removed_from_collection:
            if isinstance(book_or_isbn, Book):
                isbn_to_remove = book_or_isbn.isbn
            else:
                isbn_to_remove = book_or_isbn
            
            if isbn_to_remove in self.indexes:
                del self.indexes[isbn_to_remove]
            
            return removed_from_collection
        
        return None

    def find_by_author(self, author):
        return self.indexes.find_by_author(author)

    def find_by_year(self, year):
        return self.indexes.find_by_year(year)
    
    def find_by_isbn(self, isbn):
        return self.indexes.find_by_isbn(isbn)
    
    def find_by_genre(self, genre):
        result = []
        for book in self.books:
            if book.genre == genre:
                result.append(book)
        return result
    
    def search_books(self, **criteria):
        result = []
        for book in self.books:
            matches = True
            for key, value in criteria.items():
                if hasattr(book, key):
                    if getattr(book, key) != value:
                        matches = False
                        break
                else:
                    matches = False
                    break
            
            if matches:
                result.append(book)
        
        return result