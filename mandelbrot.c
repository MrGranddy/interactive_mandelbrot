#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int manderIter(long double cx, long double cy, int maxIter, long double divRange){
    long double xx = 0;
    long double yy = 0;
    long double xy = 0;
    long double x = 0;
    long double y = 0;
    int iter = maxIter;
    while(iter-- && xx + yy <= divRange){
        x = xx - yy + cx;
        y = 2 * xy + cy;
        xx = pow(x, 2);
        yy = pow(y, 2);
        xy = x * y;
    }
    return maxIter - iter - 1;
}

void mandelbrot(int height, int width, long double xmin, long double xmax, long double ymin, long double ymax, int maxIter, long double divRange, char *fileName){
    long double x_unit = (xmax - xmin) / width;
    long double y_unit = (ymax - ymin) / height;
    int i, j;
    for(i = 0; i < height; ++i){
        printf("%d", manderIter(xmin, ymax - i * y_unit, maxIter, divRange));
        for(j = 1; j < width; ++j){
            printf(",%d", manderIter(xmin + j * x_unit, ymax - i * y_unit, maxIter, divRange));
        }
        printf(";");
    }
}

int main(int argc, char **argv){
    int height = atoi(argv[1]);
    int width = atoi(argv[2]);
    long double xmin, xmax, ymin, ymax, divRange;
    int maxIter;
    xmin = atof(argv[3]);
    xmax = atof(argv[4]);
    ymin = atof(argv[5]);
    ymax = atof(argv[6]);
    maxIter = atoi(argv[7]);
    divRange = atoi(argv[8]);
    mandelbrot(height, width, xmin, xmax, ymin, ymax, maxIter, divRange, argv[9]);
    return 0;
}