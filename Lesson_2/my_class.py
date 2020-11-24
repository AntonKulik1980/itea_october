class Phone:

    type_ = 'Mobile phone'

    def __init__(self, model, imei, phone_number):
        self.model = model
        self.imei = imei
        self.phone_number = phone_number

    def call(self, to_number):
        self.to_number = to_number
        print(f'Звоним с {self.phone_number} to {self.to_number}')


class Satelitephone:

    def make_satelte_call(self):
        print('Make satelite call')



class Smartphone(Satelitephone,Phone):

    type_ = 'Smart phone'

    # def call(self, to_number):
    #     print(f'dzin,callinf c {self.model} {self.phone_number} to {to_number}')

    def download_aplication(self):
        print('Downloading aplication')


phone1 = Phone('Nokia', 'wspdksfdhoss', '095673676')
print(phone1.model, phone1.imei)
phone1.model = 'Motorola'
phone1.call('0343448650')
print(phone1.model, phone1.imei)
print('-' * 45)
phone2 = Phone('Siemens', 'sojdfhks', '096387433')
phone2.call('03246837456')
print('-' * 45)
Smartphone1=Smartphone('Iphone', 'asdfafsd', '283787443')
Smartphone1.call()
Smartphone1.download_aplication()
print('-' * 45)
print(Phone.type_)
print(Smartphone.type_)
print('-' * 45)



object