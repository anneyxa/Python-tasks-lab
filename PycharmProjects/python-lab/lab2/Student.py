class Student:
    def __init__(self, first_name, last_name, email, index_num, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.index_num = index_num
        if grades is None:
            self.grades = dict()
        else:
            self.grades = dict(grades)
        self.inbox = list()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_index_num(self):
        return self.index_num

    def get_grades(self):
        return self.grades

    def send_mail(self, message):
        self.inbox.append(message)
        return "Treść wiadomości: \"" + message + "\" została wysłana na adres email: " + self.email

    def add_grade(self, subject, value):
        if subject in self.grades.keys():
            self.grades[subject] = list(map(int, str(self.grades[subject])+str(value)))
        else:
            self.grades[subject] = value

    def __str__(self):
        return ('Student: ' + self.first_name + ' ' + self.last_name + ', email: ' + self.email
                + ', Index: ' + str(self.index_num) + ', Grades: ' + str(self.grades) + ', Inbox: ' + str(self.inbox))
