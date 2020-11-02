import datetime

class Diary:
    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas

    @staticmethod
    def format_date(date):
        return date.strftime("%d-%b-%y")

    def show_birthday(self):
        return self.format_date(self.birthday)

    def show_christmas(self):
        return self.format_date(self.christmas)


my_diary = Diary(datetime.date(2020, 5, 14), datetime.date(2020, 12, 25))
print(my_diary.show_birthday())
