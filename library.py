class LibraryPass:
    def __init__(self, user_name, library):
        self.user_name = user_name
        self.library = library

my_pass = LibraryPass("John Smith", "Central Library")

print(my_pass.user_name)  # prints "John Smith"
print(my_pass.library)    # prints "Central Library"

class Book:
    def __init__(self, title, author, isbn, genres, score):
        self.title = title
        self.author = author
        self.isbn = self.convert_isbn(isbn)
        self.genres = genres
        self.score = score

    def __str__(self):
        return f"{self.title} by {self.author}"

    def convert_isbn(self, isbn):
        if len(isbn) == 10:
            return "978" + isbn[0:9] + self.get_isbn_13_check_digit("978" + isbn[0:9])
        elif len(isbn) == 13:
            return isbn
        else:
            raise ValueError("Invalid ISBN length")

    def get_isbn_13_check_digit(self, isbn):
        evens = sum(int(digit) for digit in isbn[::2])
        odds = sum(int(digit) * 3 for digit in isbn[1::2])
        return str((10 - (evens + odds) % 10) % 10)

def create_book(title, author, isbn, genres, score):
    return Book(title, author, isbn, genres, score)

my_book = create_book("The Catcher in the Rye", "J.D. Salinger", "0316769487", ["Fiction", "Coming-of-age"], 4)
print(my_book)  # prints "The Catcher in the Rye by J.D. Salinger"

import json
from pathlib import Path
from typing import Dict, List


class Book:
    def __init__(self, isbn: str, title: str, author: str, genre: List[str], score: float):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.score = score if score is not None else 0


class LibraryPass:
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.rented_books = []


class BookNotAvailableError(ValueError):
    pass


class LibraryUserError(ValueError):
    pass


class Library:
    def __init__(self, name: str, books_data_path: str | Path):
        self.name = name
        self.number_of_users = 0
        self.number_of_books = 0
        self.available_genres = []
        self.rented_books = {}
        self.users = {}
        self.books = self.load_books(books_data_path)

    def load_books(self, books_data_path: str | Path) -> Dict[str, Book]:
        with open(books_data_path) as f:
            books_data = json.load(f)

        books = {}
        for book_data in books_data:
            isbn = book_data["ISBN"]
            if not isbn[:-1].isdigit() or (isbn[-1] == "X" and not isbn[:-1].isdigit()):
                continue  # skip invalid ISBNs

            check_digit = sum((i+1) * int(digit) for i, digit in enumerate(isbn[:-1])) % 11
            if check_digit != int(isbn[-1]):
                continue  # skip invalid ISBNs

            book = Book(
                isbn=isbn,
                title=book_data["Title"],
                author=book_data["Author"],
                genre=book_data["Genre"].split(", "),
                score=float(book_data["Score"]) if book_data["Score"] else 0
            )

            books[isbn] = book
            self.number_of_books += 1
            for g in book.genre:
                if g not in self.available_genres:
                    self.available_genres.append(g)
        self.available_genres.sort()
        return books

    def register_user(self, user_name: str) -> LibraryPass:
        if user_name in self.users:
            raise LibraryUserError("User name already taken.")
        library_pass = LibraryPass(user_name)
        self.users[user_name] = library_pass
        self.number_of_users += 1
        return library_pass

    def books_rented_by_user(self, user: LibraryPass) -> List[Book]:
        if user not in self.users.values():
            raise LibraryUserError("User not registered.")
        return user.rented_books

    def checkout_book(self, isbn: str, user: LibraryPass) -> Book:
        if user not in self.users.values():
            raise LibraryUserError("User not registered.")
        book = self.books.get(isbn)
        if not book or isbn in self.rented_books:
            raise BookNotAvailableError("Book not available.")
        self.rented_books[isbn] = user
        user.rented_books.append(book)
        return book

    def return_book(self, rented_book: Book, user: LibraryPass) -> None:
        if user not in self.users.values():
            raise LibraryUserError("User not registered.")
        if rented_book.isbn not in self.rented_books or self.rented_books[rented_book.isbn] != user:
           return 0
