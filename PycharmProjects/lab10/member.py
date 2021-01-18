
class LibraryMember:

    def __init__(self, name, surname, login, password):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password

    def __repr__(self):
        return f'(name: {self.name}, surname: {self.surname}, login: {self.login}, password: (password))'


class Reader(LibraryMember):    # te dwie klasy nic nie wnoszą + mogłyby być puste

    def __init__(self, name, surname, login, password):
        super().__init__(name, surname, login, password)

    def __repr__(self):
        return super(Reader, self).__repr__()


class Employee(LibraryMember):

    def __init__(self, name, surname, login, password):
        super().__init__(name, surname, login, password)

    def __repr__(self):
        return super(Employee, self).__repr__()
