# Interactive Mandelbrot

This is a program to zoom in to the Mandelbrot Set to see the details hidden in it. You can crank up the max iteration parameter
to see more details or you can move around on the fractal. You can take screenshots of the current frame you are on and
most of the parameters are very easy to adjust. The main calculating is done by a compiled C code, then the UI is created
with python.

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
>>> gcc -shared -fpic -o mandelbrot.so mandelbrot.c
```
This command compiles the C code and creates an executable called "mandelbrot", the name must stay this way to
let the python script run the executable. After compiling you can run the program by simply calling the "interactive_mandelbrot.py"
script, the command may vary on different systems, for me it is simply:
```
>>> python3 interactive_mandelbrot.py
```

## How to use the program?

* Zooming In
```
To zoom in the fractal you click on the point you want to zoom in. After clicking the screen will show one tenth of the previous
screen and the new center will be the point you click on.
```

* Reseting to Initial State
```
If you press BACKSPACE the screen will return to its initial state.
```

* Moving on Fractal
```
Using WASD keys you can move along the canvas, the center move to the direction and the frame will be recalculated.
```

* Changing the Max Iteration
```
Pressing LEFT ARROW will decrease and pressing RIGHT ARROW will increase the max iteration.
```

* Reseting Max Iteration
```
Pressing DOWN ARROW will reset the max iteration.
```

* Taking a Screen Shot
```
Pressing ENTER key will save a screen shot of the current frame.
```
