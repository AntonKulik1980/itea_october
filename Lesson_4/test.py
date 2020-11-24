# Создать подобие социальной сети.
# 1) Создать класс авторизации, в котором описать методы регистрации, аутентификации, добавить
# методы проверки на валидность пароля (содержание символов и цифр), проверка на уникальность
# логина пользователя. В классовых переменных хранить всех пользователей сети. (Отдельно
# объекты этого класса создаваться не будут, такие классы называются миксинами)
# 2) Создать класс пользователя, наследующий класс авторизации. который будет разделять роли
# админа и простого пользователя (этот вопрос можно решить с помощью флага is_admin, либо
# создав 2 разных класса для админа и обычного пользователя и наследовать их). Класс
# пользователя должен наследовать класс авторизации. На момент создания каждого объекта этого
# класса, в переменную объекта сохранять время и дату его создания.
# 3) Создать класс поста, который имеет дату публикации и её содержимое.
# Что должно быть в клиентском коде:
# Человек заходит, и имеет возможность зарегистрироваться (ввод логин, пароль, подтверждение
# пароля), далее входит в свою учетную запись. Добавить возможность выхода из учетной записи, и
# вход в новый аккаунт.
# При входе под обычным пользователем мы можем создать новый пост, с определённым
# содержимым. Под учётной записью администратора мы можем увидеть всех пользователей нашей
# системы, дату их регистрации, и их посты.

from abc import ABC, abstractmethod





class autho(ABC):
    users = []


    SpecialSym = ['$', '@', '#', '%']
    val = True

    def __init__(self, login, password, isadmin):
        self.login = login
        self.password = password
        self.isadmin = isadmin

    @classmethod
    def login_pop(cls):
        users_logins = dict([x for x in cls.users])
        return users_logins

    def register(self):

        if len(self.password) < 6:
            print('length should be at least 6')

        if len(self.password) > 20:
            print('length should be not be greater than 8')

        if not any(char.isdigit() for char in self.password):
            print('Password should have at least one numeral')

        if not any(char.isupper() for char in self.password):
            print('Password should have at least one uppercase letter')

        if not any(char.islower() for char in self.password):
            print('Password should have at least one lowercase letter')

        if not any(char in self.SpecialSym for char in self.password):
            print('Password should have at least one of the symbols $@#')
        # if  self.login in self.Login_pop():
        #     print('!!!!')

        #
        # self.dict([x for x in self.users]).get(self.login,'error') == self.login:
        #     print('!!!!!!!!!!')
        # self.login in dict(kv for d in self.users for kv in d.items()):
        #     print('!!!!!!!!!!')
        # filter(lambda x: x['Login'] == 'self.login', self.users) is True:
        #     return Exception

        else:
            autho.users.append(dict(login=self.login, password=self.password,isadmin=self.isadmin))


autho('Anton', '121@asQW',1).register()
autho('Anton1', '122@asQW',0).register()
autho('Anton2', '123@asQW',0).register()
autho('Anton3', '124@asQW',0).register()
autho('Anton4', '125@asQW',0).register()
autho('Anton4', '125@asQW',0).register()
print(autho.users)
# print(autho.login_pop())
