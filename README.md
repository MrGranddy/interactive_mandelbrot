# Interactive Mandelbrot

This is a program to zoom in to the Mandelbrot Set to see the details hidden in it. You can crank up the max iteration parameter
to see more details or you can move around on the fractal. You can take screenshots of the current frame you are on and
most of the parameters are very easy to adjust. The main calculating is done by a compiled C code, then the UI is created
with python.

## New Features!

I added some new features to travel around the awesome fractal space of the Mandelbrot Set. Some major changes are:
* Cleaning up the code a little bit and removing redundant code.
* Changed the main logic of the recursion function of Mandelbrot:

> In the older versions the creation of the fractal was straight forward, the code was just iterating z = z^2 + c formula.   Now the complex number operations are done using the "complex.h" standart library,  this means we can try different terms with different powers and coefficients,   for example: z = z ** 3.2 + c, and indeed you can now do exactly that!   How it works is simple, now the recursion formula is in the form of

```z = a * z ^ p1 + b * z ^ p2 + c * z ^ p3 + c```

> This means you can change the coefficients and powers of these three terms and see the effects on runtime!   Instructions on how to change there parameters are given in the "How To" section.

> Initially: [a, b, c] = [0.0, 1.0, 0.0], [p1, p2, p3] = [1.0, 2.0, 3.0] so initially you will see our classic Mandelbrot fractal.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Here is a quick list of the things you'll have to run this program.

```
Python 3.6 or higher
```
```
PyGame, NumPy, Matplotlib Module
```

## How to run the program?
Firstly you should compile the C code to do the calculating, to do this you should have a C compiler,
me and probably most of you uses GCC so we run this simple line of command:
```
>>> gcc -shared -fpic -O3 -o mandelbrot.so mandelbrot.c
```
This command compiles the C code and creates an executable called "mandelbrot", the name must stay this way to
let the python script run the executable. After compiling you can run the program by simply calling the "interactive_mandelbrot.py"
script, the command may vary on different systems, for me it is simply:
```
>>> python3 interactive_mandelbrot.py
```

## How to use the program?


* Zooming In

> To zoom in the fractal you click on the point you want to zoom in. After clicking the screen will show one tenth of the previous screen and the new center will be the point you click on.


* Reseting to Initial State

> If you press BACKSPACE the screen will return to its initial state.


* Moving on Fractal

> Using WASD keys you can move along the canvas, the center move to the direction and the frame will be recalculated.


* Changing the Max Iteration

> Pressing LEFT ARROW will decrease and pressing RIGHT ARROW will increase the max iteration.


* Reseting Max Iteration

> Pressing DOWN ARROW will reset the max iteration.


* Taking a Screen Shot

> Pressing ENTER key will save a screen shot of the current frame.


* Selecting Coefficients to Adjust

> Pressing 1, 2, or 3 key will select a coefficient to adjust. i.e. [a, b, c]


* Selecting Powers to Adjust

> Pressing 4, 5, or 6 key will select a power to adjust. i.e. [p1, p2, p3]


* Changing Selected Parameters

> Pressing O key will decrease the selected parameter by 0.1 and, pressing P key will increase the selected value by 0.1.

