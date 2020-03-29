"""
Write a decorator to validate the function’s input to make sure that all the parameters are the
types that you specified beforehand.
For example:
@check_types(int, float, str)
def f(a, b, c):
...
Functionality:
●
Add some tests to validate this functionality.
"""


def check_types(*params):
    def checker(func):
        def validator(*args, **kwargs):
            if all([type(arg) is _type for arg, _type in zip(args, params)]):
                resp = func(*args, **kwargs)
            else:
                raise Exception('arguments are not valid')
            return resp
        return validator
    return checker


@check_types(int, str, str)
def call_for_dinner(time, target, location):
    for t in range(time):
        print(f'{t}) {target}, come to {location} to dinner')

if __name__ == '__main__':
    call_for_dinner(5, 'kitten', 'kitchen')
    call_for_dinner(5, 3, 'kitchen')