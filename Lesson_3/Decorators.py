from symbol import decorator
from functools import wraps

def decorartor(number=3):


        def actual_decorartor(func):

            @wraps(func)
            def wrapper(*name):
                print('-'* number)
                result = func(*name)
                print('-' * number)
                return result
            return wrapper
        return actual_decorartor

@decorartor(3)
def target_function( age, name):
    print(f'Hello world, {age},{name}')
    return 'Hello world'

result = target_function(15,'Anton')

decorartor(3)(target_function.__wrapped__)(15,'Anton')