#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

int manderIter(long double cx, long double cy, int maxIter, long double divRange) {
    
    double complex c = cx + cy * I;
    double complex z = 0;

    int iter = maxIter;
    while (iter-- && cabs(z) <= divRange) {
        z = cpow(z, 2) + c;
    }
    return maxIter - iter - 1;
}

double* mandelbrot(unsigned int height, unsigned int width, long double xmin, long double xmax, 
                    long double ymin, long double ymax, unsigned int maxIter, 
                    long double divRange) {

    long double x_unit = (xmax - xmin) / width;
    long double y_unit = (ymax - ymin) / height;
    double *values = (double *)malloc(width * height * sizeof(double));

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