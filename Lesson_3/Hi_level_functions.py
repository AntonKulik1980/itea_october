list_of_numbers =[1,2,3,4,5]
list_of_numbers2 =[6,7,8,9,10]

lambda n: n**2

result = list(map(lambda n,n2: (n+n2)** 2,list_of_numbers,list_of_numbers2))
print(result)

result =list(filter(lambda n: n > 100,result))
print(result)