import random
import pygame
import pandas as pd


def scale(local_min, local_max, num, desired_min, desired_max):
    return ((num - local_min) / (local_max - local_min)) * (desired_max - desired_min) + desired_min


def mandelbrot(xarray, max_iter):
    colors = []
    for j in range(max_iter + 1):
        colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    for x in range(xarray.shape[0]):
        for y in range(xarray.shape[1]):
            a = scale(0, xarray.shape[0], x, -2, .47)
            b = scale(0, xarray.shape[1], y, -1.12, 1.12)
            xn = 0
            yn = 0
            i = 0
            while i < max_iter and abs(xn + yn) < 16:
                x_temp = (xn * xn - yn * yn) + a
                yn = (2 * xn * yn) + b
                xn = x_temp
                i += 1

            xarray[x, y] = colors[i]
            if i == max_iter:
                xarray[x, y] = (0, 0, 0)
    return xarray


pygame.init()
size = (248*3, 224*3)
screen = pygame.display.set_mode(size)
finish = True
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
px_array = pygame.PixelArray(screen)
pd.DataFrame(px_array).to_csv('file.csv')
n = 0
while finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False
    px_array[:] = mandelbrot(px_array, n)
    pygame.display.flip()
    pygame.image.save(screen, f'pics/iteration{n}.jpeg')
    n += 1
pygame.quit()
