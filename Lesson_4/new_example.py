class Person:

    def __new__(cls, *args, **kwargs):
        person_odbject = super().__new__(cls)
        person_odbject.age = 25
        return person_odbject

    def __init__(self, first_name, sername):
        self._first_name = first_name
        self.sername = sername

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        self.first_name = value


Person = Person('Jhon', 'Dou')
print(Person.age)
