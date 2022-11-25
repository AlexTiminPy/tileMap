import pygame
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys

class Level():
    pass

class chunk():

    def __init__(self):
        self.tiles = []

    pass

class tile():

    """def __init__(self): #,image,length, width,
        #self.length = length
        #self.width = width
        #self.image = image
        #self.TTL = 10"""

    def __iter__(self):
        self.frame = 0
        return self

    def __next__(self):
        if self.frame <= 9:
           pass
        else:
            self.frame = 0
        current_frame = self.frame
        self.frame += 1
        return current_frame


class Slime(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            filename)
        self.sub = self.image.subsurface((0,0,128,128))
        self.rect = self.sub.get_rect(
            center=(x, 64))
    #дописать суда логику переключения чере сабсерфис, попробовать передавать суда либо гену, либо некст


slime = Slime(64,r'Slime.png')

tile1 = tile()
tile1.slime = slime

pygame.init()

screen = pygame.display.set_mode((128*4,128*4))
screen.fill((0, 0, 0))
pygame.display.flip()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(tile1.slime.sub, tile1.slime.rect)
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