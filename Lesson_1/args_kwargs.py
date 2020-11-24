def sum_(requierd_value, *args):
    print(args)
    result = 0
    for i in (requierd_value,) + args:
        result += i
    return result



data = []
#


result = sum_(1,2)
print(result)
#
#
#
sum_(100,200,300,400)
#
 def products_sum(**kwargs):
    print(kwargs)
#
#
#

products = {
        'tomato':10,
        'orange':20,
        'carrot':3,
        'meat':2



}

 #products_sum(tomato=10,orange=20,carrot=3,meat=2)







data = [100,200,300,400]

# a1,a2,a3,a4 = data[0],data[1],data[2],data[3],data[4]

a1,a2,a3,a4 = data

print(a1,a2,a3,a4)