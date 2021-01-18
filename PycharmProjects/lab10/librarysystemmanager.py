from getpass import getpass  # getpass works only when run from normal console, not PyCharm console

from library import Library
from member import Reader, Employee


class LibrarySystemManager:

    def __init__(self, library=None):
        if library is None:
            self.library = Library()
        else:
            self.library = library
        self.logged_person = None

    def run_list_books(self):
        self.library.list_books()

    def run_borrow_book(self):
        book_id = int(input('Type id of the book you want to borrow: '))
        borrowed = self.library.borrow_book(book_id, self.logged_person.login)
        if borrowed:
            print(f'{self.logged_person.name}, you borrowed following book: {self.library.get_book_by_id(book_id)}')
        else:
            print(f'{self.logged_person.name}, unfortunately this book is already taken.')

    def run_search_a_book(self):
        phrase = input("Type a search phrase: ")
        print("Results:")
        print([f'ID: {book.id}, title: {book.title}, author: {book.author}, year: {book.year}'
               for book in self.library.search_for_book(phrase)])

    def run_book_return(self):
        book_id = input('Type book id that is to be returned: ')
        is_returned = self.library.manage_book_return(book_id)
        if is_returned:
            print(f'Book with id: {book_id} returned successfully.')
        else:
            print(f'There is no rent book with id: {book_id}')

    def run_add_new_book(self):
        next_free_id = self.library.books[0].id # myląca nazwa
        for book in self.library.books:
            if book.id > next_free_id:
                next_free_id = book.id
        next_free_id += 1
        book_id = input(f'Book id (Next free id is: {next_free_id}): ')
        title = input('Book title: ')
        author = input('Book author: ')
        year = int(input('Book year: '))
        book_added = self.library.add_book(title, author, year, book_id)
        if book_added:
            print(f'Book with id {book_id} added successfully.')
        else:
            print(f'Could not add book with id {book_id} (Either id or year is wrong).')

    def run_delete_a_book(self):
        book_id = input('Type book id you want to delete: ')
        is_deleted = self.library.delete_book(book_id)
        if is_deleted:
            print(f'Book with id {book_id} deleted successfully')
        else:
            print(f'There is no book with id: {book_id}')

    def run_add_new_reader(self):
        flag = False
        while not flag:
            name = input('Type name of a reader: ')
            surname = input('Type surname of a reader: ')
            login = input('Type login of a reader (must be unique): ')
            password = getpass(prompt='Password: ', stream=None)
            reader_added = self.library.add_reader(name, surname, login, password)
            if reader_added:
                flag = True
                print(f'User {name} {surname} added successfully.')
            else:
                print('Login of a reader must be unique.')

    def run_read_library_status(self):
        self.library.read_library_status()

    def run_save_library_status(self):
        self.library.save_library_status()

    def no_such_option_message(self):
        print("There is no such option. Choose option number from the menu.")

    def login(self):
        login = input("First, log in to the library management system. Type your login: ")
        self.logged_person = self.library.get_member_by_login(login)
        if self.logged_person is None:
            print(f'There is no such user as {login}.')
        else:
            password = getpass(prompt='Password: ', stream=None)
            if self.logged_person.password == password:
                print(f'Logged in successfuly as {login}, {type(self.logged_person).__name__}')
            else:
                self.logged_person = None

    def logout(self):
        self.logged_person = None
        print("You have successfully logged out.")

    def run(self):
        while True:
            try:
                print("------------------ Library management system ------------------")
                if self.logged_person is None:
                    self.login()
                else:
                    if type(self.logged_person) == Employee:  # ----------------------Employee--------------------  # przydałaby się dekompozycja
                        print("1. Manage book return")
                        print("2. Add new book")
                        print("3. Delete book")
                        print("4. Add new reader")
                        print("5. List books")
                        print("6. Log out")
                        print("7. Exit")
                        option = int(input())
                        if option == 1:
                            self.run_book_return()
                        elif option == 2:
                            self.run_add_new_book()
                        elif option == 3:
                            self.run_delete_a_book()
                        elif option == 4:
                            self.run_add_new_reader()
                        elif option == 5:
                            self.run_list_books()
                        elif option == 6:
                            self.logout()
                        elif option == 7:
                            exit()
                        else:
                            self.no_such_option_message()
                        self.run_save_library_status()
                        input("\nType something to get to the menu... ")
                    elif type(self.logged_person) == Reader:  # --------------------Reader-----------------
                        print("1. List books")
                        print("2. Borrow a book")
                        print("3. Search for a book")
                        print("4. Log out")
                        print("5. Exit")
                        option = int(input())   # DRY
                        if option == 1:
                            self.run_list_books()
                        elif option == 2:
                            self.run_borrow_book()
                        elif option == 3:
                            self.run_search_a_book()
                        elif option == 4:
                            self.logout()
                        elif option == 5:
                            exit()
                        else:
                            self.no_such_option_message()
                        self.run_save_library_status()
                        input("\nType something to get to the menu... ")
                    else:
                        print(f'No actions available for user type: {type(self.logged_person)}')
                        input("\nType something to get to the menu... ")
                        self.logged_person = None
            except (ValueError, IndexError, TypeError) as e:
                print(e)
