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

The matrix calculation mode allows for simple matrix and vector calculations. Calculations include multiplication/dot product, inverse, addition & subtraction, and determinant. The calculations for matrices are also done in reverse polish notation, meaning they are also store in the stack. To push a new matrix or vector to the stack, enter it in the numpy array format. Each matrix/vector is stored in the stack as a letter. To view what the letter represents, type the letter into the input field and press 'enter'. This will print the contents of that letter. Typing 'help' will show the available commands and usage help within the matrix calculation mode.

The plotting mode allows users to make simple plots using the termplotlib package that uses gnuplot (note that gnuplot must be installed). The plots will be displayed within the terminal in ASCII format. The plotting mode currently only supports 2D line plots. Enter the x and y arrays in the following format: '[#, #,...]'. Additionally, numpy linspace arrays can be specified for the x-data. To do this, type 'linspace <enter>'. You will be prompted to enter the linspace parameters in the format '[start val, end val, divisions]'. A function can be specified for the y-data by typing 'func <enter?'. The user will be prompted to enter a Pythone expression using x as a variable to find the y-values of the plot. Typing 'help' will show the available commands and usage help within the plotting mode.

## Adding Shortcut to Powershell Profile on Windows
We can add a shortcut to run the program from any directory. To do this, we will set an alias in our Powershell profile. In the Windows terminal, type 'nvim $PROFILE' and replace 'nvim' with your text editor of choice. Add the following lines to your Powershell profile.
```
function Run-CLRPC {
    python pathtofolder\CLRPC.py
}
Set-Alias clrpc Run-CLRPC
```
Make sure to replace 'pathtofolder' with the path to the folder containing both CLRPC.py and calculations.py. Save the file and relaunch the terminal. When you type 'clrpc' the program should run.
