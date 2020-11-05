from Employee import Employee


class EducationEmployee(Employee):

    def __init__(self, first_name, last_name, email, room_num, consultation_hrs, learning_subjects=None):
        super().__init__(first_name, last_name, email, room_num)
        self.consultation_hrs = consultation_hrs
        if learning_subjects is None:
            self.learning_subjects = list()
        else:
            self.learning_subjects = list(learning_subjects)

    def get_consultation_hrs(self):
        return self.consultation_hrs

    def get_learning_subjects(self):
        return self.learning_subjects

    def add_learning_subject(self, subject):
        self.learning_subjects.append(subject)

    def __str__(self):
        return super().__str__() + ', Consultation hrs: ' + str(self.consultation_hrs) + ', Learning subjects: ' + str(self.learning_subjects)
