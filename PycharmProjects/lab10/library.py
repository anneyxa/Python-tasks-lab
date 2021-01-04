import json

from book import Book
from member import Reader


class Library:

    def __init__(self, books=None, readers=None, employees=None, rents=None):
        if books is None:
            self.books = list()
        else:
            self.books = books
        if readers is None:
            self.readers = list()
        else:
            self.readers = readers
        if employees is None:
            self.employees = list()
        else:
            self.employees = employees
        if rents is None:
            self.rents = dict()
        else:
            self.rents = rents

    def search_for_book(self, phrase):
        for book in self.books:
            if phrase in book:  # search by every field - everything taken into consideration (title, author, year, ...)
                yield book

    def borrow_book(self, book_id, login):
        if str(book_id) in self.rents:
            return False
        else:
            self.rents[book_id] = login
            return True

    def add_reader(self, name, surname, login):
        self.readers.append(Reader(name, surname, login))

    def add_book(self, title, author, year, id):
        self.books.append(Book(title, author, year, id))

    def list_books(self):
        for book in self.books:
            print(f'ID: {book.id}, title: {book.title}, author: {book.author}, year: {book.year}')

    def get_book_by_id(self, book_id):
        return next((book for book in self.books if book.id == book_id), None)

    def save_library_status(self):
        with open("./resources/books.json", "w") as books_data:
            json.dump([book.__dict__ for book in self.books], books_data, indent=2)
        with open("./resources/readers.json", "w") as readers_data:
            json.dump([reader.__dict__ for reader in self.readers], readers_data, indent=2)
        with open("resources/rents.json", "w") as rents_data:
            json.dump(self.rents, rents_data, indent=2)

    def get_member_by_login(self, login):
        member = next((reader for reader in self.readers if reader.login == login), None)
        if member is None:
            member = next((employee for employee in self.employees if employee.login == login), None)
        return member

    def read_library_status(self):
        with open("./resources/books.json", "r") as books_data:
            json_books = json.load(books_data)
            for elem in json_books:
                self.books.append(Book(elem['title'], elem['author'], elem['year'], elem['id']))
            print(f'Books read: {self.books}')
        with open("./resources/readers.json", "r") as readers_data:
            json_readers = json.load(readers_data)
            for elem in json_readers:
                self.readers.append(Reader(elem['name'], elem['surname'], elem['login']))
            print(f'Readers read: {self.readers}')
        with open("./resources/rents.json", "r") as rents_data:
            self.rents = json.load(rents_data)
            print(f'Rents read: {self.rents}')
