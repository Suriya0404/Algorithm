""""
First class functions can be passed as argument, can be returned from a function and can be assigned to a variable.
higher order function --> function returns a function or takes a function as argument
closure is a inner function which remember the variables in the local scope even after the outer function completes
execution. Also called free variables.

Decorators are function which takes another function as argument, add additional functionalities and returns anthoner
function without altering the source of passed function.


"""
import logging


############### First class function : Takes function as argument  #####################
def user_map(func, user_list):
    temp = []

    for i in user_list:
        temp.append(func(i))

    return temp


def square(num):
    return num * num


########## First class function: return another function ######################
### This is an example of closure since the inner function remember the tag even after the outer function completes
# execution

def html_tag(tag):
    def wrap_text(line):
        return '<{0}>{1}</{0}>'.format(tag,line)

    return wrap_text


### Another example - python logger.
def logger(func):

    def log_func(*args):
        logging.info('Logs for the function {}. The argument list - {}'.format(func.__name__, args))
        return func(*args)

    return log_func


def adder(a, b):
    return a + b


def subtract(a, b):
    return a - b

### Decorators #####

def decorator_func(original_func):
    def wrapper_func():
        print('This is wrapper function for the function {}'.format(original_func.__name__))
        original_func()

    return wrapper_func

@decorator_func
def print_message():
    print('Hello from original function')


if __name__ == '__main__':
    if __name__ == '__main__':

        # function takes function as argument
        num_list = [1, 2, 3, 4, 5]
        print(user_map(square,num_list))

        # function returns another function
        html_header = html_tag('h1')
        header_message1 = html_header('Title 1')
        print(header_message1)

        html_header = html_tag('h2')
        header_message1 = html_header('Title 2')
        print(header_message1)

        # Another example of closure with python logging
        logging.basicConfig(filename='log.txt', level=logging.INFO)

        user_add = logger(adder)
        user_minus = logger(subtract)

        print(user_add(1,2))
        print(user_minus(10,4))


        # decorators -
        # Without @ keyword  we can also assign decorator as
        # print_message = decorator_func(print_message)
        print_message()
