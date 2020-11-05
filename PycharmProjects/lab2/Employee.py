class Employee:
    def __init__(self, first_name, last_name, email, room_num):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.room_num = room_num
        self.inbox = list()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_room_num(self):
        return self.room_num

    def send_mail(self, message):
        self.inbox.append(message)
        return "Treść wiadomości: \"" + message + "\" została wysłana na adres email: " + self.email

    def __str__(self):
        return ('Employee: ' + self.first_name + ' ' + self.last_name + ', email: '
                + self.email + ', Room number: ' + str(self.room_num) + ', Inbox: ' + str(self.inbox))
