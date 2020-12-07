# 1) Создать базу данных студентов (ФИО, группа, оценки, куратор
# студента, факультет). Описать метод для вывода отличников по
# каждому факультету. Описать метод для вывода всех студентов
# определенного куратора.
# 2) Создать модуль, который будет заполнять базу данных
# случайными валидными значениями (минимум 100 студентов).


import mongoengine as me
import datetime
from statistics import mean


me.connect('Univer')


class Students(me.Document):
    fio = me.StringField(min_length=10, max_length=50)
    group = me.IntField()
    marks = me.ListField()
    kurator = me.StringField(min_length=10, max_length=50)
    faculty = me.StringField(min_length=2, max_length=50)

    def get_student_by_kurator(self, kur):
        a = Students.objects(kurator = kur)
        for user in a:
            print(user.fio,user.kurator)

    def get_superstudent(self):
        a = self.objects()
        for u in a:
            li = list(u.marks)
            avg_mark = mean(li)
            if avg_mark == 5:
                print(u.fio, u.faculty)


# Students.get_student_by_kurator(Students,'Носков Галактион Владленович')

Students.get_superstudent(Students)







