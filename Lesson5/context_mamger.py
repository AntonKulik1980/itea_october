class Dot:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type,exc_val,exc_tb)
        self.x = 0
        self.y = 0


with Dot(10,20) as dot:
    dot.x = dot.x ** 2
    dot.y = dot.y ** 2
    print(dot.x, dot.y)


print(dot.x)


file = open('text.txt','w')
file.write('QWERTY')
file.close()


with open('test1.txt','w') as file:
    file.write('QWERTY')
    