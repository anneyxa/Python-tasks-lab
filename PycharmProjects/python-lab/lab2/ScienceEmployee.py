from Employee import Employee


class ScienceEmployee(Employee):

    def __init__(self, first_name, last_name, email, room_num, publications=None):
        super().__init__(first_name, last_name, email, room_num)
        if publications is None:
            self.publications = list()
        else:
            self.publications = list(publications)

    def get_publications(self):
        return self.publications

    def add_publication(self, publication):
        self.publications.append(publication)

    def __str__(self):
        return super().__str__() + ', Publications: ' + str(self.publications)
