import numpy as np
import latex2sympy2 as lat
from numpy.linalg import inv
import termplotlib as tpl
import ast
import os
import sys



"""
Help messages
"""
def help_message():
    print(' Type \'help -[command]\' for command-specific help.\n')
    print(' Type \'c\' to clear the stack.')
    print(' Type \'b\' to remove an entry from the stack.')
    print(' Type \'x\' to exit.')
    print(' Type \'ans\' to push most recent calculation to the stack.\n')
    print(' Type \'matrix\' to enter matrix/vector calculation mode.')
    print(' Type \'eval\' to enter Python expression evaluation mode.')
    print(' Type \'latex\' to enter matrix/vector calculation mode.')
    print(' Type \'plot\' to enter plotting mode.')
    print('------------------------------------------------------------\n')

def matrix_help():
    print('Perform matrix calculations using numpy package. Input 1D arrays in the format [#,#,...]. Input 2D arrays in the format [[#,#,...],[#,#,...],...]. Operations are still performed in reverse polish notation. Available operations include: *, +, -, det, inv. Matrices/vectors are represented in the stack with a letter. To view a matrix or vector, type the letter associated to it and press \'enter\'. Use \'c\' to clear the stack, \'b\' to clear the most recently added value to the stack, and \'x\' to exit.\n')

def latex_help():
    print('Evaluate expressions using LaTeX formatted input. Returns the output in LaTeX format. Use \'clear\' to clear the screen, and use \'x\' to exit.\n')

def python_eval_help():
    print('Evaluate expressions using Python formatted input. To access elements in the stack, use lst[i], where i is the index of the desired element. Use \'c\' to clear the stack, \'b\' to clear the most recently added value to the stack, and \'x\' to exit.\n')

def plot_help():
    print('Plot using termplotlib. Input x and y data in array format ([#,#,...]). x-data can also be inputted as a linspace array by typing \'linspace\' then pressing \'enter\'. It will prompt you to enter the linspace parameters in array format. To use a function to calculate y, type \'func\'. You will be promped to enter an expression. The expression uses the eval() function to calculate the y-values, with x defined as the global varibale for the x-data. Functions like sin and cos can be used, as well as contants like pi and e. Use \'clear\' to clear the screen, and use \'x\' to exit.\n')



"""
Error messages
"""
errors = {0:'Process exited with 0 errors.', 1:'Error 1: Problem encountered in push operation.',
            2:'Error 2: Problem encountered in pop operation.', 3:'Error 3: Problem encountered in stack empty',
            4:'Error 4: No value to delete.', 5:'Error 5: ans list is empty.',
            6:'Error 6: Problem encountered in ans retrieval.',
            100:'Error 100: Invalid stack size for operation.', 
            101:'Error 101: Problem encountered in factorial calculation.',
            102:'Error 102: Problem encounted in trigonometric calculation.',
            103:'Error 103: Problem encountered in logarithmic/exponential calculation.', 
            200:'Error 200: Problem encountered in Python eval.',
            201:'Error 201: Problem encountered in LaTeX eval.', 
            202:'Error 202: Cannot be converted to numpy array.',
            203:'Error 203: Problem encountered in matrix multiply.',
            204:'Error 204: Problem encountered in matrix add.',
            205:'Error 205: Problem encountered in matrix subtraction.',
            206:'Error 206: Problem encountered in determinant.', 
            207:'Error 207: Invalid choice.', 208:'Error 208: Problem encountered while plotting.',
            209:'Error 209: Problem creating linspace array.',
            210:'Error 210: Problem encountered in defining y function.'}


"""
Clear terminal
"""
def clear_terminal():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


"""
Stack operations and errors
"""
def print_error(error):
    """ Print an error from errors dict in yellow text.
    """
    print('\033[93m' + error + '\033[0m')

def push(lst, val):
    """ Pushes a value to the stack (lst).
    """
    try:
        return lst.append(val)
    except:
        print_error(errors[1])

def pop(lst):
    """ Pops a value from the stack (lst).
    """
    try:
        return lst.pop()
    except:
        print_error(errors[2])

def clear_stack():
    """ Returns an empty list.
    """
    try:
        return []
    except:
        print_error(errors[3])

def exit_program():
    """ Print exit message.
    """
    print_error(errors[0])

def unknown_operation():
    """ Print error message for invalid input.
    """
    print_error(errors[1])

def ans(lst, ans):
    """ Used to push the answer to the last operation to the stack (lst).
    """
    try:
        push(lst, ans)
    except:
        print_error(errors[6])



""" 
Operations
"""
def multiply(stack, ans):
    """ Multiply two values.
    """
    try:
        b = pop(stack)
        a = pop(stack)
        result = a * b
        push(stack, result)
        ans.append(result)
    except:
        stack.append(b)
        print_error(errors[100])

def power(stack, ans):
    """ Computes exponent.
    """
    try:
        b = pop(stack)
        a = pop(stack)
        result = a ** b
        push(stack, result)
        ans.append(result)
    except:
        stack.append(b)
        print_error(errors[100])

def add(stack, ans):
    """ Adds two values.
    """
    try:
        b = pop(stack)
        a = pop(stack)
        result = a + b
        push(stack, result)
        ans.append(result)
    except:
        stack.append(b)
        print_error(errors[100])

def subtract(stack, ans):
    """ Subtracts two values.
    """
    try:
        b = pop(stack)
        a = pop(stack)
        result = a - b
        push(stack, result)
        ans.append(result)
    except:
        stack.append(b)
        print_error(errors[100])

def divide(stack, ans):
    """ Divides two values.
    """
    try:
        b = pop(stack)
        a = pop(stack)
        result = a / b
        push(stack, result)
        ans.append(result)
    except:
        stack.append(b)
        print_error(errors[100])

def divide_no_remainder(stack, ans):
    """ Divides two values with no remainder.
    """
    try:
        b = pop(stack)
        a = pop(stack)
        result = a // b
        push(stack, result)
        ans.append(result)
    except:
        stack.append(b)
        print_error(errors[100])

def remainder(stack, ans):
    """ Returns modulus of two numbers.
    """
    try:
        b = pop(stack)
        a = pop(stack)
        result = a % b
        push(stack, result)
        ans.append(result)
    except:
        stack.append(b)
        print_error(errors[100])

def factorial(stack, ans):
    """ Computes the factorial of a value.
    """
    try:
        a = pop(stack)
        result = 1.0
        for i in range(1,int(a)+1):
            result = result*i
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[101])

def sine(stack, ans):
    """ Computes the sine of a value.
    """
    try:
        a = pop(stack)
        result = np.sin(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[102])

def arcsin(stack, ans):
    """ Computes the arcsine of a value.
    """
    try:
        a = pop(stack)
        result = np.arcsin(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[102])

def cine(stack, ans):
    """ Computes the cine of a value.
    """
    try:
        a = pop(stack)
        result = np.c(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[102])

def arcc(stack, ans):
    """ Computes the arcc of a value.
    """
    try:
        a = pop(stack)
        result = np.arcc(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[102])

def tangent(stack, ans):
    """ Computes the tangent of a value.
    """
    try:
        a = pop(stack)
        result = np.tan(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[102])

def arctan(stack, ans):
    """ Computes the arctan of a value.
    """
    try:
        a = pop(stack)
        result = np.arctan(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[102])

def logarithm(stack, ans):
    """ Computes the natural logarithm of a value.
    """
    try:
        a = pop(stack)
        result = np.log(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[103])

def exp(stack, ans):
    """ Computes the e raised to a value.
    """
    try:
        a = pop(stack)
        result = np.exp(a)
        push(stack, result)
        ans.append(result)
    except:
        print_error(errors[103])



"""
Submenus
"""
def python_evaluate():
    """ This function requests an expression as input until user enters 'x' to exit.
    Will return to main calculator if 'x' is chen.
    Use eval() to evaluate expression and print it.
    """
    lst = []
    while True:
        print('\033[0;32m' + ' Python Eval Mode' + '\033[0m')
        print('\033[0:32m' + '------------------' + '\033[0m' + '\n')
        string = ''
        for i in lst:
            string = string + str(i) + ' '
        python_eval_input = input(string + '\033[0;32m' + "| " + '\033[0m')
        clear_terminal()
        match python_eval_input:
            case 'b':
                pop(lst)
            case 'c':
                lst = clear_stack()
            case 'x':
                clear_terminal()
                break
            case 'help':
                python_eval_help()
            case _:
                try:
                    python_eval_ans = eval(python_eval_input)
                    lst.append(python_eval_ans)
                except:
                    print_error(errors[200])

def latex():
    """ This function requests an expression as input until user enters 'x' to exit.
    Will return to main calculator if 'x' is chosen. Use 'clear' to clear the screen.
    Evaluates inputted LaTeX expression.
    """
    print('\033[0;32m' + ' LaTeX Eval Mode' + '\033[0m')
    print('\033[0:32m' + '-----------------' + '\033[0m' + '\n')
    while True:
        latex_eval_input = input('Enter expression: ')
        match latex_eval_input:
            case 'x':
                clear_terminal()
                break
            case 'clear':
                clear_terminal()
                print('\033[0;32m' + ' LaTeX Eval Mode' + '\033[0m')
                print('\033[0:32m' + '-----------------' + '\033[0m' + '\n')
            case 'help':
                clear_terminal()
                latex_help()
                print()
                print('\033[0;32m' + ' LaTeX Eval Mode' + '\033[0m')
                print('\033[0:32m' + '-----------------' + '\033[0m' + '\n')
            case _:
                try:
                    result = lat.latex2latex(latex_eval_input)
                    result2 = result.replace('[', '')
                    result3 = result2.replace(']', '')
                    print(f'Result: {result3}\n')
                except:
                    print_error(errors[201])

def matrix_and_vector():
    """ This function requests an expression as input until user enters 'x' to exit.
    Performs matrix calculations with the numpy package.
    """
    nums_to_letters = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                       8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                       16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W',
                       23:'X', 24:'Y', 25:'Z'}
    m_v_dict = {}
    while True:
        print('\033[0;32m' + ' Matrix/Vector Mode' + '\033[0m')
        print('\033[0:32m' + '--------------------' + '\033[0m' + '\n')
        string = ''
        for keys, value in m_v_dict.items():
            string = string + keys + ' '
        m_v_input = input(string + '\033[0;32m' + "| " + '\033[0m')
        clear_terminal()
        match m_v_input:
            # Operations
            case '*':
                matrix_multiply(m_v_dict, nums_to_letters)
            case '+':
                matrix_add(m_v_dict, nums_to_letters)
            case '-':
                matrix_subtract(m_v_dict, nums_to_letters)
            case 'det':
                matrix_det(m_v_dict, nums_to_letters)
            case 'inv':
                matrix_inv(m_v_dict, nums_to_letters)

            # Menu controls
            case 'c':
                m_v_dict = {}
            case 'b':
                m_v_dict.popitem()
            case 'x':
                clear_terminal()
                break
            case 'help':
                matrix_help()

            # Push new matrices and vectors
            case _:
                if m_v_input in m_v_dict:
                    print(m_v_dict[m_v_input])
                    continue
                try:
                    m_v_input = ast.literal_eval(m_v_input)
                    m_v_input = np.array(m_v_input, dtype=float)
                    temp = nums_to_letters[len(m_v_dict)]
                    m_v_dict[temp] = m_v_input
                except:
                    print_error(errors[202])

# Matrix operations
def matrix_multiply(m_v_dict, nums_to_letters):
    """ Multiplies two arrays.
    """
    try:
        b = m_v_dict.popitem()
        a = m_v_dict.popitem()
        result = np.matmul(a[1], b[1])
        temp = nums_to_letters[len(m_v_dict)]
        m_v_dict[temp] = result
    except:
        print_error(errors[203])

def matrix_add(m_v_dict, nums_to_letters):
    """ Adds two arrays.
    """
    try:
        b = m_v_dict.popitem()
        a = m_v_dict.popitem()
        result = np.add(a[1], b[1])
        temp = nums_to_letters[len(m_v_dict)]
        m_v_dict[temp] = result
    except:
        print_error(errors[204])

def matrix_subtract(m_v_dict, nums_to_letters):
    """ Subtracts two arrays.
    """
    try:
        b = m_v_dict.popitem()
        a = m_v_dict.popitem()
        result = np.subtract(a[1], b[1])
        temp = nums_to_letters[len(m_v_dict)]
        m_v_dict[temp] = result
    except:
        print_error(errors[205])

def matrix_det(m_v_dict, nums_to_letters):
    """ Calculates determinant of a matrix.
    """
    try:
        a = m_v_dict.popitem()
        result = np.linalg.det(a[1])
        temp = nums_to_letters[len(m_v_dict)]
        m_v_dict[temp] = result
    except:
        print_error(errors[206])

def matrix_inv(m_v_dict, nums_to_letters):
    """ Computes the inverse of a matrix.
    """
    try:
        a = m_v_dict.popitem()
        result = inv(a[1])
        temp = nums_to_letters[len(m_v_dict)]
        m_v_dict[temp] = result
    except:
        print_error(errors[206])


def plot():
    """ This function plots x and y data in ASCII chart form with termplotlib.
    Will return to main calculator if 'x' is chosen. Use 'clear' to clear the screen.
    """
    print('\033[0;32m' + ' Plotting Mode' + '\033[0m')
    print('\033[0:32m' + '---------------' + '\033[0m' + '\n')
    while True:
        try:
            x_data = input('Input x-data: ')
            if x_data == 'linspace':
                x_linspace = input('Input linspace array: ')
                try:
                    x_linspace = ast.literal_eval(x_linspace)
                    x_data = np.linspace(x_linspace[0], x_linspace[1], x_linspace[2])
                except:
                    print_error(errors[209])
            elif x_data == 'x':
                clear_terminal()
                break
            elif x_data == 'help':
                clear_terminal()
                plot_help()
                print()
                print('\033[0;32m' + ' Plotting Mode' + '\033[0m')
                print('\033[0:32m' + '---------------' + '\033[0m' + '\n')
                continue
            elif x_data == 'clear':
                clear_terminal()
                print('\033[0;32m' + ' Plotting Mode' + '\033[0m')
                print('\033[0:32m' + '---------------' + '\033[0m' + '\n')
                continue
            else:
                x_data = ast.literal_eval(x_data)
                x_data = np.array(x_data, dtype=float)

            y_data = input('Input y-data: ')
            if y_data == 'func':
                y_function = input('Enter function expression: ')
                try:
                    y_data = []
                    for x in x_data:
                        y = eval(y_function, {"x": x, "sin":np.sin, "cos":np.cos, "ln":np.log, "exp":np.exp, "pi":np.pi, "e":np.e})
                        y_data.append(y)
                    print()
                except:
                    print_error(errors[210])
            elif y_data == 'x':
                clear_terminal()
                break
            elif y_data == 'help':
                plot_help()
                continue
            elif y_data == 'clear':
                clear_terminal()
                print('\033[0;32m' + ' Plotting Mode' + '\033[0m')
                print('\033[0:32m' + '---------------' + '\033[0m' + '\n')
                continue
            else:
                y_data = ast.literal_eval(y_data)
                y_data = np.array(y_data, dtype=float)
                print()

            fig = tpl.figure()
            fig.plot(x_data, y_data, label="data", width=50, height=15)
            fig.show()
        except:
            print_error(errors[208])
