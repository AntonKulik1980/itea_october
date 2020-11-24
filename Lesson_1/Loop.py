# i = 0
# while i< 15:
#     print(i)
#     i += 1


list_of_numbers = list(range(0, 100))

for i in list_of_numbers:
    print(i)


my_dict = {
    1:2,
    5:10,
    10:20
}

for k,v in my_dict.items():
    print(k,v)
    if k == 5:
        continue
    print(k, v)

n = 10
My_list = list(range(0,n,1))
for i in My_list:
    if i % 2 == 0:
        print(i)


Countries = {
    'Ukraine':'Kyiv',
    'USA':'Vashington',
    'France':'Paris'
}
list_of_countries = ['Germany', 'USA', 'Ukraine', 'Italy']
for i in list_of_countries:
    if i in Countries:
        print(i)



My_numbers = range(1,100)
for i in My_numbers:
    if i % 3 == 0:
        print('Fizz')
    if i % 5 == 0:
        print('Buzz')
    if i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)


def dep(sum,years,pers):
    return sum*years*pers/100

money = dep(100,10,10)
print(money)

