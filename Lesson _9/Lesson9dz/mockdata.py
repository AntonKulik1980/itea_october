import mongoengine as me
import datetime
from statistics import mean
from faker import Faker
fake = Faker(['ru_RU'])
import random

me.connect('Univer')


class Students(me.Document):
    fio = me.StringField( min_length=10,max_length=50)
    group = me.IntField()
    marks = me.ListField()
    kurator = me.StringField(min_length=10, max_length=50)
    faculty = me.StringField(min_length=2, max_length=50)




def student():

    group = [1, 2, 3, 4, 5]
    marks = [2, 4, 4, 5,5,5,5,5,5,3]
    kurator = ['Амвросий Филатович Ковалев', 'Светлана Степановна Лихачева', 'Носков Галактион Владленович',
               'Кузьма Эдгардович Никифоров']
    faculty = ['FTTS', 'OMTP', 'NTPD', 'HHJI']
    for i in range(101):
        fio = fake.name()
        st = Students(fio=fio,group= random.choice(group),
               marks=[random.choice(marks),random.choice(marks),random.choice(marks),
                      random.choice(marks),random.choice(marks),random.choice(marks)],
              kurator=random.choice(kurator),faculty=random.choice(faculty))
        st.save()




student()



    #  st = {fio:fio, group:random.choice(group),
    #                  marks:[random.choice(marks),random.choice(marks),random.choice(marks),random.choice(marks),random.choice(marks),random.choice(marks)],
    #                kurator:random.choice(kurator),faculty:random.choice(faculty)}
    #
    # print(st)

    # st = Students(fio=random(fio),group= random(group),
    #               marks=[random(marks),random(marks),random(marks),random(marks),random(marks),random(marks)],
    #               kurator=random(kurator),faculty=random(faculty))
# st.save()
