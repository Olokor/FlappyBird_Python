import pygame as pg
import sys
from PIL import Image

def draw_floor():
    window.blit(floor_surface, (floor_x_pox, 500))
    window.blit(floor_surface, (floor_x_pox + 336, 500))
pg.init()

window = pg.display.set_mode((576,700))
clock = pg.time.Clock()
bg_surface = pg.image.load("assets/background-day.png").convert()
#set default image size
SURFACE_IMAGE_SCALAR = (576, 650)
bg_surface = pg.transform.scale(bg_surface, SURFACE_IMAGE_SCALAR)


#
floor_surface = pg.image.load("assets/base.png").convert()
# floor_surface = pg.transform.scale2x(floor_surface)
#set default size
FLOOR_DEFAULT_SIZE = (336,150)
floor_surface = pg.transform.scale(floor_surface, FLOOR_DEFAULT_SIZE)
floor_x_pox = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    window.blit(bg_surface, (0,0))
    floor_x_pox -= 1
    draw_floor()
    if floor_x_pox <= -50:
        floor_x_pox = 0

    clock.tick(60)
    pg.display.update()
