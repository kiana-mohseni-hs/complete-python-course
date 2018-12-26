print (f'hello exercise 1')

"""
for the function below, add your code in appropriate place that checks the input n.
n should be a non-negative integer, otherwise a ValueError should be raised
and a proper error message should be provided informing the user of the error
for simplicity, you may assume that the input is always an integer for this exercise

def count_from_zero_to_n(n):
    for x in range(0, n+1):
        print(x)

user_number = int(input(f'enter a number:'))
print (user_number.__class__)
if user_number < 0:
    raise ValueError ('the number has to be a positive integer')
count_from_zero_to_n(user_number)

class My_class:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'name is: {self.name}, number is: {self.number}'

x_class = My_class ('kiana', '604 562 2446')
print(x_class)


class My_error(TypeError):
    def __init__(self, message, code):
        super().__init__(f'message {message}, {code}')
        self.code = code


raise My_error('that was a big one!', 400)

"""

# - define a UncountableError that takes in wrong_value as the only argument
# - the UncountableError should inherit ValueError
# - the UncountableError should indicate an error message like this:
#    'Invalid value for n, WRONG_VALUE. n must be greater than 0.'
#    where WRONG_VALUE should be replaced by the given value in the argument
# define your UncountableError here:

"""
class UncountableError(ValueError):
    def __init__(self, value):
        super().__init__('Invalid value for {}, n must be greater than 0.'.format(value))

# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)

count_from_zero_to_n(int(input('enter n: ')))

"""
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return(0)
    else:
        n_square = n ** 2
        return(n_square)
    finally:
        return n_square

print(power_of_two())
print(f'goodbye friend!')
