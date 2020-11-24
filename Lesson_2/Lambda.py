def hello_world(name):
    return f'Hello world my name is {name}'

print(hello_world('Anton'))

helow_world_lambda = lambda n: f'Hello world {n}'
print(helow_world_lambda('Anton'))


hw = hello_world

print(hw('Petya'))