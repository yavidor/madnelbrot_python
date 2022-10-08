import pygame
import pandas as pd
import colorsys


def scale(local_min, local_max, num, desired_min, desired_max):
    return ((num - local_min) / (local_max - local_min)) * (desired_max - desired_min) + desired_min


def mandelbrot(xarray, max_iter):
    # colors = []
    # for j in range(max_iter + 1):
    #     colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    width = xarray.shape[0]
    height = xarray.shape[1]
    for x in range(width):
        for y in range(height):
            a = scale(0, width, x, -2, .47)
            b = scale(0, height, y, -1.12, 1.12)
            xn = 0
            yn = 0
            i = 0
            while i < max_iter and xn * xn + yn * yn <= 4:
                x_temp = (xn * xn - yn * yn) + a
                yn = (2 * xn * yn) + b
                xn = x_temp
                i += 1
            # Grayscale coloring
            # xarray[x, y] = (255 - int(i * 255 / n), 255 - int(i * 255 / n), 255 - int(i * 255 / n))
            # HSV coloring
            v = 1 if i < n else 0.0
            hsvv = tuple(val * 255 for val in colorsys.hsv_to_rgb((i / n), 1.0, abs(v)))
            xarray[x, y] = hsvv
            # xarray[x, y] = colors[i]

    return xarray


pygame.init()
size = (248 * 2, 224 * 2)
screen = pygame.display.set_mode(size)
finish = True
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
px_array = pygame.PixelArray(screen)
n = 1
# px_array[:] = mandelbrot(px_array, n)
# pygame.display.flip()
# pygame.image.save(screen, f'./pics/iteration{n}.jpeg')
while finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False
    px_array[:] = mandelbrot(px_array, n)
    pygame.display.flip()
    pygame.image.save(screen, f'./pics/iteration{n}.jpeg')
    n += 1
pygame.quit()
