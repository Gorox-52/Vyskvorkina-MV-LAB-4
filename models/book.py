class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __str__(self):
        return f"Book('{self.title}' '{self.author}' {self.year})"
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False
    
    def __hash__(self):
        return hash(self.isbn)

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'isbn': self.isbn
        }