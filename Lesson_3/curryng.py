def a(a_):
    print('A')
    def b(b_):
        print('B')
        def c(c_):
            return a_,b_,c_
        print('C')

        return c


    return b


result = a(10)

result2 = result(20)
result3 = result2(30)
print(result3)
print(a(10)(20)(30))