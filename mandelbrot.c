#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

unsigned int manderIter(long double cx, long double cy, unsigned int maxIter, long double divRange) {
    
    double complex c = cx + cy * I;
    double complex z = 0;

    unsigned int iter = maxIter;
    while (iter && cabs(z) <= divRange) {
        z = cpow(z, 2) + c;
        iter--;
    }
    
    return maxIter - iter;
}

unsigned int* mandelbrot(unsigned int height, unsigned int width, long double xmin, long double xmax, 
                    long double ymin, long double ymax, unsigned int maxIter, 
                    long double divRange) {

    long double x_unit = (xmax - xmin) / width;
    long double y_unit = (ymax - ymin) / height;
    unsigned int *values = (unsigned int *)malloc(width * height * sizeof(unsigned int));

    unsigned int m = 0;

    for (unsigned int i = 0; i < height; ++i)
    {
        values[m] = manderIter(xmin, ymax - i * y_unit, maxIter, divRange);
        m++;
        for (unsigned int j = 1; j < width; ++j)
        {
            values[m] = manderIter(xmin + j * x_unit, ymax - i * y_unit, maxIter, divRange);
            m++;
        }
    };
    return values;
}