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


class CustomDiary(Diary):
    def __init__(self, birthday, christmas, date_format=None):
        self.date_format = date_format
        super().__init__(birthday, christmas)

    def format_date(self, date):
        return date.strftime(self.date_format)


first_diary = CustomDiary(datetime.date(2018, 1, 1), datetime.date(2018, 3, 3), "%d-%b-%Y")
second_diary = CustomDiary(datetime.date(2018, 1, 1), datetime.date(2018, 3, 3), "%d/%m/%Y")

print(first_diary.show_birthday())
print(second_diary.show_christmas())
