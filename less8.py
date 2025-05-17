'''def logger(func):
    def wrapper(expression):
        result = func(expression)
        print(f'[LOG] Вираз: {expression} = {result}')
        return result
    return wrapper

def safe_input(func):
    def wrapper(expression):
        allowed = set('0123456789+-=*/(). ')
        if not set(expression).issubset(allowed):
            raise ValueError('Неприпустимі символи')
        return func(expression)
    return wrapper

@logger
@safe_input

def calculate(expression):
    return eval(expression)

while True:
    try:
        expr = input('Введіть вираз: ')
        if expr == 'exit':
            break
        print('Результат: ', calculate(expr))
    except Exception as e:
        print('Помилка:', e)'''

import logging
import time

logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asktime)s - %(levelname)s - %(message)s'
)
def devide(a,b):
    logging.info('Divide function with arguments: a={a}, b={b}')
    try:
        result = a/b
        logging.info(f'Result: {result}')
        return result
    except ZeroDivisionError as e:
        logging.error('Division by zero!', exc_info= True)
        return None


