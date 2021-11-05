#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

double complex formula_calculator(double complex z, long double *coeffs, long double *powers, size_t num_terms) {

    double complex t = 0;

    for(unsigned int i = 0; i < num_terms; i++) {
        t += cpow(z, powers[i]) * coeffs[i];
    }

    return t;
}

unsigned int manderIter(long double cx, long double cy, unsigned int maxIter, long double divRange,
                        long double *coeffs, long double *powers, size_t num_terms) {
    
    double complex c = cx + cy * I;
    double complex z = 0;

    unsigned int iter = maxIter;
    while (iter && cabs(z) <= divRange) {
        z = formula_calculator(z, coeffs, powers, num_terms) + c;
        iter--;
    }

    return maxIter - iter;
}

unsigned int* mandelbrot(unsigned int height, unsigned int width, long double xmin, long double xmax, 
                    long double ymin, long double ymax, unsigned int maxIter, 
                    long double divRange, long double *coeffs, long double *powers, size_t num_terms) {

    long double x_unit = (xmax - xmin) / width;
    long double y_unit = (ymax - ymin) / height;
    unsigned int *values = (unsigned int *)malloc(width * height * sizeof(unsigned int));

    unsigned int m = 0;

    for (unsigned int i = 0; i < height; ++i)
    {
        values[m] = manderIter(xmin, ymax - i * y_unit, maxIter, divRange, coeffs, powers, num_terms);
        m++;
        for (unsigned int j = 1; j < width; ++j)
        {
            values[m] = manderIter(xmin + j * x_unit, ymax - i * y_unit, maxIter, divRange, coeffs, powers, num_terms);
            m++;
        }
    };
    return values;
}