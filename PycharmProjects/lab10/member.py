
class LibraryMember:

    def __init__(self, name, surname, login):
        self.name = name
        self.surname = surname
        self.login = login

    def __repr__(self):
        return f'(name: {self.name}, surname: {self.surname}, login: {self.login})'


class Reader(LibraryMember):

    def __init__(self, name, surname, login):
        super().__init__(name, surname, login)

    def __repr__(self):
        return super(Reader, self).__repr__()


class Employee(LibraryMember):

    def __init__(self, name, surname, login):
        super().__init__(name, surname, login)

    def __repr__(self):
        return super(Employee, self).__repr__()
