# 1) Написать контекстный менеджер для работы с SQLite DB.
import sqlite3


class dbconnection():
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.close()



# 2) Создать базу данных студентов. У студента есть факультет,
# группа, оценки, номер студенческого билета. Написать программу,
# с двумя ролями: Администратор, Пользователь. Администратор
# может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки,
# факультет)



class user:

    @classmethod
    def get_best_students(cls):
        with dbconnection('univer.db') as conn:
            cursor = conn.cursor()
            cursor.execute('select  name ,Surname from Students where st_id in ( select st_id from marks group '
                           'by St_id having avg(mark)=5)')
            print(list((cursor.fetchmany(100))))

    @classmethod
    def get_all_students(cls):
        with dbconnection('univer.db') as conn:
            cursor = conn.cursor()
            cursor.execute('select  name, Surname from Students')
            print(list((cursor.fetchmany(100))))

    @classmethod
    def get_student_by_std_id(cls,id_):
        with dbconnection('univer.db') as conn:
            cursor = conn.cursor()

            cursor.execute('select  name, Surname from Students where St_id = ?', (id_,))
            print(list((cursor.fetchmany(100))))

    @classmethod
    def get_full_info(cls,id_):
        with dbconnection('univer.db') as conn:
            cursor = conn.cursor()
            cursor.execute('select name,Surname,Faculty,Gr_no from students where St_id = ?', (id_,))
            print((cursor.fetchmany(100)))
        with dbconnection('univer.db') as conn:
            cursor = conn.cursor()
            cursor.execute('select St_id,Subject,Mark from Marks where St_id = ?', (id_,))
            print((cursor.fetchmany(100)))


class admin(user):

    @classmethod
    def update_students(cls,name,surname,faculty,gr_no,St_id):
        with dbconnection('univer.db') as conn:
            cursor = conn.cursor()
            cursor.execute('update students set name = ?,surname =?,faculty=?,gr_no=? where st_id=?', (name,surname,faculty,gr_no,St_id,))
            conn.commit()

    @classmethod
    def insert_students(cls,name,surname,faculty,gr_no,St_id):
        with dbconnection('univer.db') as conn:
            cursor = conn.cursor()
            cursor.execute('insert into students (name,surname,faculty,gr_no,St_id) values(?,?,?,?,?)', (name,surname,faculty,gr_no,St_id,))
            conn.commit()

# user.get_all_students()
# user.get_student_by_std_id()
user.get_full_info(40586)
# admin.insert_students()
# admin.update_students()

