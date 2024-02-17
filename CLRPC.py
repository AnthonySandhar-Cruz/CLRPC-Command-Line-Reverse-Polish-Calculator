import os
import numpy as np
import calculations as c

c.clear_terminal()
print()
print('\033[94m' + '     _________ .____   _____________________________  ' + '\033[0m')
print('\033[94m' + '     \_   ___ \|    |  \______   \______   \_   ___ \ ' + '\033[0m')
print('\033[94m' + '     /    \  \/|    |   |       _/|     ___/    \  \/ ' + '\033[0m')
print('\033[94m' + '     \     \___|    |___|    |   \|    |   \     \____' + '\033[0m')
print('\033[94m' + '      \______  /_______ \____|_  /|____|    \______  /' + '\033[0m')
print('\033[94m' + '             \/        \/      \/                  \/ ' + '\033[0m')
print('\033[94m' + '          Command Line Reverse Polish Calculator   ' + '\033[0m')
print('\033[94m' + '-----------------------------------------------------------' + '\033[0m')
print('Type \'help\' to list available commands.\n')

ans = []
stack = []
tracker = 0
while True:
    # Print the RPN Mode header after first iteration
    if tracker == 1:
        print('\033[94m' + ' RPN Mode' + '\033[0m')
        print('\033[94m' + '----------' + '\033[0m' + '\n')
    tracker = 1

    # Print the stack and ask for input on the same line
    string = ''
    for i in stack:
        string = string + str(i) + ' '
    answer = input(string + '\033[94m' + "| " + '\033[0m')
    c.clear_terminal()

    # Attempt to convert input to float and add it to the stack.
    try:
        answer = float(answer)
        stack.append(answer)
        continue
    
    # Check the input if it cannot be converted to a float.
    except:
        match answer:
            # Operations go here
            case '*':
                c.multiply(stack, ans)
            case '**':
                c.power(stack, ans)
            case '+':
                c.add(stack, ans)
            case '-':
                c.subtract(stack, ans)
            case '/':
                c.divide(stack, ans)
            case '//':
                c.divide_no_remainder(stack, ans)
            case '%':
                c.remainder(stack, ans)
            case '!':
                c.factorial(stack, ans)
            case 'sin':
                c.sine(stack, ans)
            case 'arcsin':
                c.arcsin(stack, ans)
            case 'cos':
                c.cosine(stack, ans)
            case 'arccos':
                c.arccos(stack, ans)
            case 'tan':
                c.tangent(stack, ans)
            case 'arctan':
                c.arctan(stack, ans)
            case 'ln':
                c.logarithm(stack, ans)
            case 'exp':
                c.exp(stack, ans)
            case 'e':
                c.push(stack, np.e)
            case 'pi':
                c.push(stack, np.pi)
            case 'ans':
                try:
                    c.ans(stack, ans[-1])
                except:
                    c.print_error(c.errors[5])


            # Submenus go here
            case 'eval':
                c.python_evaluate()
            case 'latex':
                c.latex()
            case 'matrix':
                c.matrix_and_vector()
            case 'plot':
                c.plot()


            # Menu controls go here
            case 'help':
                c.help_message()
            case 'help -matrix':
                c.matrix_help()
            case 'help -latex':
                c.latex_help()
            case 'help -eval':
                c.python_eval_help()
            case 'help -plot':
                c.plot_help()
            case 'c':
                stack = c.clear_stack()
            case 'b':
                c.pop(stack)
            case 'x':
                c.exit_program()
                break
            case _:
                c.unknown_operation()
