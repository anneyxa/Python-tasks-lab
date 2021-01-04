from library import Library
from member import Employee, Reader

if __name__ == '__main__':
    library = Library()
    print("\nRead previous library status:\n")
    library.read_library_status()
    print("\n")
    logged_person = None

    while (True):
        library.save_library_status()
        print("------------------ Library management system ------------------")
        if logged_person is None:
            login = input("First, log in to the library management system. Type your login: ")
            logged_person = library.get_member_by_login(login)
            continue
        else:
            print("Select one of following numbers to execute following operations: ")
            if type(logged_person) == Employee:  # EMPLOYEE -------------------------------------------------------
                print("1. Manage book return")
                print("2. Add new book")
                print("3. Delete book")
                print("4. Add new reader")
                option = int(input())
                if option == 1:
                    print("Option 1")
                elif option == 2:
                    print("Option 2")
                elif option == 3:
                    print("Option 3")
                elif option == 4:
                    print("Option 4")
                else:
                    print("Choose option number from the menu.")
                input("\nType something to get to the menu... ")
                continue
            elif type(logged_person) == Reader:  # READER -----------------------------------------------------------
                print("1. List books")
                print("2. Borrow a book")
                print("3. Search for a book")
                option = int(input())
                if option == 1:
                    library.list_books()
                elif option == 2:
                    book_id = int(input('Type id of the book you want to borrow: '))
                    borrowed = library.borrow_book(book_id, logged_person.login)
                    if borrowed:
                        print(f'{logged_person.name}, you borrowed following book: {library.get_book_by_id(book_id)}')
                    else:
                        print(f'{logged_person.name}, unfortunately this book is already taken.')
                elif option == 3:
                    phrase = input("Type a search phrase: ")
                    print("Results:")
                    print([book for book in library.search_for_book(phrase)])
                else:
                    print("Choose option number from the menu.")
                input("\nType something to get to the menu... ")
                continue
            else:
                print(f'No actions available for user type: {type(logged_person)}')
                input("\nType something to get to the menu... ")
                logged_person = None
                continue
