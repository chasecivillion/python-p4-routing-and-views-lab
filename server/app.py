#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    count = f''
    for i in range(parameter):
        count += f'{i}\n'
    return count

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation.lower() == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    else:
        print('whoa that is not available!')



if __name__ == '__main__':
    app.run(port=5555, debug=True)


# - A `math()` view should take three parameters: `num1`, `operation`, and `num2`.
#   It must perform the appropriate operation on the two numbers in the order that
#   they are presented. The included operations should be: `+`, `-`, `*`, `div`
#   (`/` would change the URL path), and `%`. Its URL should be of the format
#   `/math/<num1><operation><num2>`.