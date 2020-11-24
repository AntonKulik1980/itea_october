from abc import ABC, abstractmethod


class Phone(ABC):

    def __init__(self, model, emei):
        self.model = model
        self.emei = emei

    @abstractmethod
    def call(self):
        pass



class Smartphone(Phone):

    def __init__(self, model, emei, os_):
        super().__init__(model, emei)
        self.os_ = os_

    def call(self):
        print(f'calling from {self.model}')

    def download(self):
        print('Downloading')


Smartphone('iphone', '1322143124').call()
