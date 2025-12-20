from models.book import Book
import random
from models.library import Library

class LibrarySimulator:
    def __init__(self):
        self.titles = ["Война и мир", "1984", "Мастер и Маргарита", 
                      "Преступление и наказание", "Гарри Поттер", 
                      "Властелин колец", "Маленький принц", "Шерлок Холмс"]
        self.authors = ["Толстой", "Оруэлл", "Булгаков", "Достоевский", 
                       "Роулинг", "Толкин", "Сент-Экзюпери", "Конан Дойл"]
        self.genres = ["Роман", "Антиутопия", "Фэнтези", "Детектив", "Классика"]
        self.years = list(range(1800, 2024))
    
    def _create_random_book(self):
        isbn = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(100, 999)}"
        return Book(
            title=random.choice(self.titles),
            author=random.choice(self.authors),
            year=random.choice(self.years),
            genre=random.choice(self.genres),
            isbn=isbn
        )
    
    def run_simulation(self, steps=20, seed=None):
        if seed:
            random.seed(seed)
        
        library = Library()
        
        for step in range(1, steps + 1):
            print(f"\n=== Шаг {step} ===")
            
            actions = [
                'add',                   
                'remove',                
                'search_author',         
                'search_year',           
                'search_genre',          
                'search_isbn',           
                'search_nonexistent',    
                'update_indexes'
            ]
            
            action = random.choice(actions)
            
            if action == 'add':
                new_book = self._create_random_book()
                success = library.add_book(new_book)
                if success:
                    print(f"Добавлена книга: {new_book.title} (ISBN: {new_book.isbn})")
                else:
                    print(f"Ошибка при добавлении книги")

            elif action == 'remove':
                if len(library.books) > 0:
                    book = random.choice(list(library.books))
                    removed = library.remove_book(book.isbn)
                    if removed:
                        print(f"Удалена книга: {book.title} (ISBN: {book.isbn})")
                    else:
                        print(f"Не удалось удалить книгу")
                else:
                    print(f"Нет книг для удаления")

            elif action == 'search_author':
                if len(library.books) > 0:
                    authors = list(set(b.author for b in library.books))
                    author = random.choice(authors)
                    books = library.find_by_author(author)
                    print(f"Поиск по автору '{author}': найдено {len(books)} книг")
                    for b in books[:3]:
                        print(f"    - {b.title} ({b.year})")
                else:
                    print(f"Нет книг для поиска по автору")

            elif action == 'search_year':
                if len(library.books) > 0:
                    years = list(set(b.year for b in library.books))
                    year = random.choice(years)
                    books = library.find_by_year(year)
                    print(f"Поиск книг {year} года: найдено {len(books)} книг")
                else:
                    print(f"Нет книг для поиска по году")

            elif action == 'search_genre':
                if len(library.books) > 0:
                    genres = list(set(b.genre for b in library.books))
                    genre = random.choice(genres)
                    books = library.find_by_genre(genre)
                    print(f"Поиск по жанру '{genre}': найдено {len(books)} книг")
                else:
                    print(f"Нет книг для поиска по жанру")

            elif action == 'search_isbn':
                if len(library.books) > 0:
                    book = random.choice(list(library.books))
                    found = library.find_by_isbn(book.isbn)
                    if found:
                        print(f"Поиск по ISBN {book.isbn}: найдена книга '{found.title}'")
                    else:
                        print(f"Поиск по ISBN {book.isbn}: книга не найдена")
                else:
                    print(f"[i] Нет книг для поиска по ISBN")

            elif action == 'search_nonexistent':
                fake_isbn = "000-000-000"
                found = library.find_by_isbn(fake_isbn)
                if found:
                    print(f"Очень странно: найдена книга с несуществующим ISBN {fake_isbn}")
                else:
                    print(f"Поиск несуществующей книги (ISBN: {fake_isbn}): не найдено")
                
                fake_author = "Неизвестный Автор"
                books = library.find_by_author(fake_author)
                print(f"Поиск несуществующего автора '{fake_author}': найдено {len(books)} книг")

            elif action == 'update_indexes':
                if hasattr(library.indexes, 'update_indexes'):
                    library.indexes.update_indexes()
                    print(f"Индексы обновлены. Всего книг в индексах: {len(library.indexes)}")
                else:
                    print(f"Метод update_indexes не найден")
            
            print(f"Всего книг в библиотеке: {len(library.books)}")