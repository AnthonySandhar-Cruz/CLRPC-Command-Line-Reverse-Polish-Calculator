```
_________ .____   _____________________________  
\_   ___ \|    |  \______   \______   \_   ___ \ 
/    \  \/|    |   |       _/|     ___/    \  \/ 
\     \___|    |___|    |   \|    |   \     \____
 \______  /_______ \____|_  /|____|    \______  /
        \/        \/      \/                  \/ 
```
# CLRPC: Command Line Reverse Polish Calculator
A command line calculator written in Python that uses reverse polish notation for calculations. Also includes Python expression mode, matrix operation mode, LaTeX expression mode, and an ASCII based plotting mode.

## Dependencies
This tool utilizes the following Python packages: numpy, ast, os, latex2sympy2, and termplotlib. Note that termplotlib requires gnuplot to be installed on your machine.

## Features & Usage
Typing 'help' will show a list of available commands. Typing 'help -[command]' will show help for a specific command if it is available.

The basic calculator allows for simple arithmetic calculations, as well as some basic functions, such as trigonometric and logarithmic functions. Constants like pi and e are available as well. The calculations are done in reverse polish notation. Typing a value and pressing 'enter' pushes that value to the stack and is displayed on the left side of the on-screen pipe ('|'). Typing an operator or function will perform that operation on the stack. Ex: '2 <enter> 4 <enter> + <enter>' will return '6' and push it to the stack. Use 'ans' to push the answer to the most recent calculation to the stack.

The calculator also features a Python expression mode where you can enter an expression in the Python format and it will be evaluated using the eval() function. Ex: '(2+2)/4 + 8**2 <enter>' will return '65' and push it to the stack. Use 'lst[i]' to access an element in the stack, where 'i' is the index of the element. Typing 'help' will show the available commands and usage help within the Python expression mode.

The LaTeX expression mode allows for the user to input expressions in LaTeX formatting, and they will be evaluated using the latex2sympy2 package and displayed in LaTeX format. Typing 'help' will show the available commands and usage help within the LaTeX expression mode.

The plotting mode allows users to make simple plots using the termplotlib package that uses gnuplot (note that gnuplot must be installed). The plots will be displayed within the terminal in ASCII format. The plotting mode currently only supports 2D line plots. Enter the x and y arrays in the following format: '[#, #,...]'. Additionally, numpy linspace arrays can be specified for the x-data. To do this, type 'linspace <enter>'. You will be prompted to enter the linspace parameters in the format '[start val, end val, divisions]'. A function can be specified for the y-data by typing 'func <enter?'. The user will be prompted to enter a Pythone expression using x as a variable to find the y-values of the plot. Typing 'help' will show the available commands and usage help within the plotting mode.
