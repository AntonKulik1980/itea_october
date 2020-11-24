# 1/0
# print('!!!!!')

# number = 10
#
# number.isalpha()

# t_1 = {1,2}
# t_2 = {2,3}
# t_1+t_2


t_1 = '1'
t_2 = '2'

try:
    result =  t_1+t_2
except TypeError as e:
    print(e.args)
    error_text = str(e)
    result = 'Error'
except  ArithmeticError:
    result = 'Error Arithmetic'

else:
    print('Ura')

finally:
    print('try exept finish')

print(result)


def hate_ones(arg1,arg2):
    if 1 in (arg1,arg2):
        raise ValueError ('Will not work with 1')
    return arg1 + arg2
hate_ones(2,2)