import pygame
from pygame.locals import DOUBLEBUF
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import matplotlib.backends.backend_agg as agg
import sys, os
from os import listdir
from os.path import isfile, join
import subprocess

pygame.init()
pygame.display.set_caption("Interactive Mandelbrot")

size = width, height = 1000, 1000
window = pygame.display.set_mode(size, DOUBLEBUF)
screen = pygame.display.get_surface()

cmaps = ["hot", "copper", "cubehelix", "CMRmap", "BuPu", "YlOrBr", "inferno"]
colormap = cmaps[4]

center = (0, 0)
mandel_range = 2
div_range = 4
dpi = 80
max_iter = 50 + np.log10( 2 / mandel_range ) ** 3

pygame.display.flip()
calculating = True

mandel = None

while(True):

    if calculating:
        p = subprocess.Popen("./mandelbrot" + " " + str(height) + " "
                                             + str(width) + " "
                                             + str(center[0] - mandel_range) + " "
                                             + str(center[0] + mandel_range) + " "
                                             + str(center[1] - mandel_range) + " "
                                             + str(center[1] + mandel_range) + " "
                                             + str(max_iter) + " " + str(div_range)
                                             + " mandelbrot.txt", stdout=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        output = str(output)[2:-2]
        mandel = np.array( [ line.split(",") for line in output.split(";") ], dtype="uint8" )
        fig = plt.figure(figsize=(height/dpi, width/dpi), dpi=dpi)
        fig.figimage(mandel, cmap=colormap)
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        s = canvas.get_width_height()
        man = pygame.image.fromstring(raw_data, s, "RGB")
        screen.blit(man, (0, 0))
        pygame.display.flip()
        plt.close("all")
        calculating = False


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            center = ( center[0] - mandel_range + (pos[0] / width) * 2 * mandel_range, center[1] - mandel_range + (1 - pos[1] / height) * 2 * mandel_range )
            mandel_range *= 0.1
            max_iter = 50 + np.log10( 2 / mandel_range ) ** 2
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            mandel_range = 2
            center = (0, 0)
            max_iter = 50 + np.log10( 2 / mandel_range ) ** 3
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            files = [f for f in listdir(".") if isfile(join(".", f))]
            max_ss_num = 0
            for f in files:
                if "interactive_mandelbrot_ss" in f:
                    if int(f[25:-4]) > max_ss_num:
                        max_ss_num = int(f[25:-4])
            plt.imsave("interactive_mandelbrot_ss%d.png" % (max_ss_num + 1), mandel, cmap=colormap)
            print("Screenshot saved...")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            max_iter = 50 + np.log10( 2 / mandel_range ) ** 3
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            max_iter -= 20
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            max_iter += 20
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            center = (center[0] - mandel_range / 10, center[1])
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            center = (center[0], center[1] - mandel_range / 10)
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            center = (center[0] + mandel_range / 10, center[1])
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            center = (center[0], center[1] + mandel_range / 10)
            print("Max iterations: " + str(max_iter), "Mandel Range: " + str(mandel_range), "Coordinates: (", center[0], ",", center[1], ")")
            calculating = True
        if event.type == pygame.QUIT:
            sys.exit()
