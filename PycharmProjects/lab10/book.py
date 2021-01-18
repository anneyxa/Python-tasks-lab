
class Book:

    def __init__(self, title, author, year, id):
        self.title = title
        self.author = author
        self.year = year
        self.id = id

    def __repr__(self):
        return f'(title: {self.title}, author: {self.author}, year: {self.year}, ID: {self.id})'

    def __contains__(self, phrase):
        if phrase in f'{self.title} {self.author} {self.year} {self.id}':   # return warunek
            return True
        return False
