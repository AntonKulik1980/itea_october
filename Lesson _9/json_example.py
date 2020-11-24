import  json

products = {'Onion': {
        'price': 12,
        'in_stock': 1000,
        'description': 'Лук'

    },
        'Tomato': {
        'price': 4,
        'in_stock': 10000,
        'description': 'Помидоры'

    }, 'Cucumber': {
        'price': 10,
        'in_stock': 500,
        'description': 'Огурцы'

    }}



# products_json = json.dumps(products)
# print(products)
# print(products_json)


f = open('myjson.json','w')
json.dump(products,f)
f.close()
