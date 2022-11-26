import pygame
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys

TILE_SIZE = 128


class Level():
    pass


class Chunk():

    def __init__(self):
        self.tiles = []


class Tile():
    """def __init__(self): #,image,length, width,
        #self.length = length
        #self.width = width
        #self.image = image
        #self.TTL = 10"""
    pass


class Slime(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        self.step = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename)
        self.sub = self.image.subsurface((0, 0, TILE_SIZE, TILE_SIZE))
        self.rect = self.sub.get_rect(
            center=(x, 64))

    def frame(self, step):
        self.sub = self.image.subsurface((step * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE))
        self.rect = self.sub.get_rect(
            center=(64, 64))
        return self.sub, self.rect

    def __iter__(self):
        self.step = 0
        return self

    def __next__(self):
        if self.step <= 9:
            pass
        else:
            self.step = 0
        current_frame = self.step
        self.step += 1
        return current_frame


"""chunk = []
for i in range(4):
    chunk.append([]*4)
    for j in range(4):
        current_tile = Tile()
        current_slime = Slime(64, r'Slime.png')
        current_tile.slime = current_slime
        chunk.append(current_tile)"""

chunk = [[Tile() for t in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        current_slime = Slime(64, r'Slime.png')
        chunk[i][j].slime = current_slime


"""slime = Slime(64, r'Slime.png')

tile1 = Tile()
tile1.slime = slime
"""
pygame.init()
surf = pygame.Surface((200, 150))
surf.fill((255, 255, 255))
screen = pygame.display.set_mode((128 * 4, 128 * 4))
screen.fill((0, 0, 0))
pygame.display.flip()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    for i in range(4):
        for j in range(4):
            var1 = chunk[i][j].slime.frame(next(chunk[i][j].slime))

            screen.blit(var1[0], dest=(TILE_SIZE * i, TILE_SIZE * j, TILE_SIZE, TILE_SIZE))  # var1[1],

    """var1 = tile1.slime.frame(next(slime))
    screen.blit(var1[0], var1[1])  #screen.blit(tile1.slime.sub, tile1.slime.rect)"""
    pygame.display.update()
    pygame.time.delay(20)

"""img = Image.open(r'slime.png')

def show(image):
    plt.figure(figsize=(6,6))
    image = image.crop((0,0,128,128))
    plt.imshow(image)
    plt.axis('off')
    plt.show()


show(img)"""

"""sc = pygame.display.set_mode((1024, 1024))
sc.fill((100, 150, 200))

slime_surf = pygame.image.load(r'slime.png').convert()
slime_surf_t = pygame.transform.(slime_surf,(0,0,128,128))
slime_rect = slime_surf_t.get_rect()
sc.blit(slime_surf_t, slime_rect)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()"""

"""img = pygame.image.load(r'grass.png')
sc = pygame.display.set_mode((1280, 1280))
sc.fill((100, 150, 200))

pygame.display.update()
for j in range(360):
    img = pygame.transform.rotate(img, 1)
    img_rect = img.get_rect()
    sc.blit(img, img_rect)
    #pygame.display.update()
    pygame.display.flip()


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()"""
