from itertools import zip_longest

from EducationEmployee import EducationEmployee
from Polynomial import Polynomial
from ScienceEmployee import ScienceEmployee
from Student import Student

if __name__ == '__main__':
    p = Polynomial(1, -2, 2)  # this is 1 - 2x + 2x^2
    p2 = Polynomial(1, 0, 5)  # this is 1 + 5x^2

    print(p(3))
    print(p + p2)
    print(p.add(p2))
    print(p - p2)
    print(p * p2)
    (p2 * p).print_polynomial()  # more "mathematical" way of print
    print(bool(p(3)))
    print("###############################")
    student = Student("Ania", "Urban", "abc@interia.pl", "298005", {'history': 4})
    student2 = Student("Beata", "Kozidrak", "def@interia.pl", "298006")
    scienceEmployee = ScienceEmployee("Jakub", "Nowak", "employeeScience@gmail.com", 412, ["First publication"])
    educationEmployee = EducationEmployee('Adam', 'Radosny', 'employeeEducation@gmail.com', 523, {'Friday': '14;00 - '
                                                                                                            '15;00'})
    scienceEmployee.add_publication("some publication")
    educationEmployee.add_learning_subject("history")
    student.add_grade('history', 3)
    student.add_grade('mathematics', 5)
    student.send_mail("Abc message")
    student.send_mail("Def message")
    educationEmployee.send_mail("Some message")

    print(student)
    print(student2)
    print(scienceEmployee)
    print(educationEmployee)
    print(scienceEmployee.get_publications())
