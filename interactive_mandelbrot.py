import sys

# C calling utilities
from ctypes import cdll, c_longdouble, c_uint, c_uint32
import ctypes

from os.path import isfile, join
from os import listdir

import pygame
from pygame.locals import DOUBLEBUF

from matplotlib import pyplot as plt
import matplotlib.backends.backend_agg as agg
import matplotlib
matplotlib.use("Agg")

import numpy as np

# C compilation
# > gcc -shared -fpic -o mandelbrot.so mandelbrot.c
lib = cdll.LoadLibrary("./mandelbrot.so")


pygame.init()
pygame.display.set_caption("Interactive Mandelbrot")

size = width, height = 500, 500
window = pygame.display.set_mode(size, DOUBLEBUF)
screen = pygame.display.get_surface()

cmaps = ["hot", "copper", "cubehelix", "CMRmap", "BuPu", "YlOrBr", "inferno"]
cmap_sel_ind = 4

center = (0, 0)
mandel_range = 2
div_range = 2
max_iter = 50 + np.log10(2 / mandel_range) ** 3

pygame.display.flip()
calculating = True

mandel = None

arrlen = width * height
cwidth = c_uint(int(width))
cheight = c_uint(int(height))
lib.mandelbrot.restype = ctypes.POINTER(c_uint32 * arrlen)

while True:

    if calculating:
        cresult = lib.mandelbrot(
            cwidth,
            cheight,
            c_longdouble(center[0] - mandel_range),
            c_longdouble(center[0] + mandel_range),
            c_longdouble(center[1] - mandel_range),
            c_longdouble(center[1] + mandel_range),
            c_uint32(int(max_iter)),
            c_longdouble(div_range),
        )

        mandel = np.array(cresult.contents).reshape((width, height))
        cmap = matplotlib.cm.get_cmap(cmaps[cmap_sel_ind], lut=max_iter)
        canvas = (cmap(mandel)[..., :3] * 255).astype("uint8")
        man = pygame.image.frombuffer(canvas.tobytes(), size, "RGB")
        screen.blit(man, (0, 0))
        pygame.display.flip()
        calculating = False

    for event in pygame.event.get():

        keys_pressed = pygame.key.get_pressed()
        step_ratio = 1 / 100

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            center = (
                center[0] - mandel_range + (pos[0] / width) * 2 * mandel_range,
                center[1] - mandel_range + (1 - pos[1] / height) * 2 * mandel_range,
            )
            mandel_range *= 0.1
            max_iter = 50 + np.log10(2 / mandel_range) ** 2
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            mandel_range = 2
            center = (0, 0)
            max_iter = 50 + np.log10(2 / mandel_range) ** 3
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            files = [f for f in listdir(".") if isfile(join(".", f))]
            max_ss_num = 0
            for f in files:
                if "interactive_mandelbrot_ss" in f:
                    if int(f[25:-4]) > max_ss_num:
                        max_ss_num = int(f[25:-4])
            plt.imsave(
                "interactive_mandelbrot_ss%d.png" % (max_ss_num + 1),
                mandel,
                cmap=colormap,
            )
            print("Screenshot saved...")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            max_iter = 50 + np.log10(2 / mandel_range) ** 3
            calculating = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if max_iter > 20:
                max_iter -= 20
            calculating = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            max_iter += 20
            calculating = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            center = (center[0] - mandel_range * step_ratio, center[1])
            calculating = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            center = (center[0], center[1] - mandel_range * step_ratio)
            calculating = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            center = (center[0] + mandel_range * step_ratio, center[1])
            calculating = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            center = (center[0], center[1] + mandel_range * step_ratio)
            calculating = True

        if event.type == pygame.QUIT:
            sys.exit()
