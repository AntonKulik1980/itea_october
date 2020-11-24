class Custom_array:

    def __init__(self,size,type_):
        self.list =[0] * size
        self._type = type_

    def __getitem__(self, item):
        return self.list[item]


    def __setitem__(self, key, value):

        if isinstance(key,int) and type(value) == self._type:
            self._list[key] = value
        else:
            raise TypeError('Terror')




array = Custom_array(10,int)
print(array[1])



numbers = [10,20,8,300]

counter = 0

for i, v in enumerate(numbers):
    print(i,v)
