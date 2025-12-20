from book import Book
from collections import defaultdict

class BookCollection:
    def __init__(self):
        self._books = []

    def __iter__(self):
        return iter(self._books)
    
    def add_book(self, book):
        self._books.append(book)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return BookCollection(self._books[key])
        return self._books[key]
    
    def __len__(self):
        return len(self._books)
    
    def __contains__(self, book):
        if not isinstance(book, Book):
            return False
        return book in self._books

    def remove_book(self, book_or_isbn):
        if isinstance(book_or_isbn, Book):
            for i, book in enumerate(self._books):
                if book.isbn == book_or_isbn.isbn:
                    return self._books.pop(i)
            return None
        
        elif isinstance(book_or_isbn, str):
            for i, book in enumerate(self._books):
                if book.isbn == book_or_isbn:
                    return self._books.pop(i)
            return None
        
        else:
            raise TypeError("Дай книжку или ISBN")

class IndexDict(dict):
    def __init__(self):
        super().__init__()
        
        self.isbn_index = {}
        self.author_index = defaultdict(list)
        self.year_index = defaultdict(list)
    
    def __setitem__(self, key, value):
        if not isinstance(value, Book):
            raise TypeError("Можно добавлять только объекты Book")
        
        super().__setitem__(key, value)
        
        self._add_to_indexes(key, value)

    def __delitem__(self, key):
        if key in self:
            book = self[key]
            self._remove_from_indexes(key, book)
        
        super().__delitem__(key)
    
    def _add_to_indexes(self, key, book):
        self.isbn_index[book.isbn] = book
        
        self.author_index[book.author].append(book)
        
        self.year_index[book.year].append(book)

    def _remove_from_indexes(self, key, book):
        self.isbn_index.pop(book.isbn, None)
        
        if book.author in self.author_index:
            self.author_index[book.author] = [b for b in self.author_index[book.author] if b.isbn != book.isbn]
            if not self.author_index[book.author]:
                del self.author_index[book.author]
        
        if book.year in self.year_index:
            self.year_index[book.year] = [b for b in self.year_index[book.year] if b.isbn != book.isbn]
            if not self.year_index[book.year]:
                del self.year_index[book.year]

    def find_by_isbn(self, isbn):
        return self.isbn_index.get(isbn)
    
    def find_by_author(self, author):
        return self.author_index.get(author, [])
    
    def find_by_year(self, year):
        return self.year_index.get(year, [])
    
    def reindex(self):
        self.isbn_index.clear()
        self.author_index.clear()
        self.year_index.clear()
        
        for key, book in self.items():
            self._add_to_indexes(key, book)

    def update_indexes(self):
        self.reindex() 