import pygame
import numpy as np
import sys

TILE_SIZE = 128
CHUNK_SIZE = 16


class Map:
    def __init__(self):
        self.chunks = []
        pass

    def get_object_by_coord(self, x, y):
        """
        Возвращает полностью объект из тайла
        в чанке и тайле реализовать соотв методы, которые будет вызывать этот метод
        """
        self.chunks[int(x/CHUNK_SIZE)][int(y/CHUNK_SIZE)].get_object_by_coord(x, y)

    def add_object_to_map(self):
        """Реализовать добавление объекта в карту"""
        pass

    def remove_object_from_map(self):
        """Реализовать удаление объекта с карты по x, y и по самому объекту"""
        pass

    def replace_object_to_near_tile(self):
        """Реализовать перемещение объекта из тайла в один из соседних тайлов"""
        pass

    def replace_object_to_any_tile(self):
        """Реализовать перемещение объекта из тайла в один из любых тайлов чанка тайлов"""
        pass

    def replace_object_to_any_chunk(self):
        """Реализовать перемещение объекта из тайла в один из любых чанков и тайлов"""
        pass

    def get_data_for_draw(self, camera):
        """Должна возвращать все актуальные для отрисовки спрайты,
        для конкретных координат, которые будут храниться в 'камере'
        для всей карты
        сделать поправку спрайтов на зум камеры
        """
        pass

    def get_data_for_draw_2(self, start_x, start_y, w, h, zoom):
        """
        То же самое что прошлое, но пока не известно будет ли разумно передавать камеру в функцию поэтому пусть будет
        """
        pass


class Link:
    def __init__(self, max_dist: int, max_speed: int):
        self.max_dist = max_dist
        self.max_speed = max_speed


class Chunk:

    def __init__(self):
        self.tiles = []

    def get_data_for_draw(self, camera):
        """Должна возвращать все актуальные для отрисовки спрайты
        для всего чанка"""
        pass

    def get_object_by_coord(self, x, y):
        self.tiles[int((x - int(x/CHUNK_SIZE)*CHUNK_SIZE)/TILE_SIZE)] \
            [int((y - int(y/CHUNK_SIZE)*CHUNK_SIZE)/TILE_SIZE)].get_object()


class Tile:
    def __init__(self):
        self.object = None
        pass

    def get_data_for_draw(self, camera):
        """Должна возвращать все актуальные для отрисовки спрайты
        для тайла"""
        pass

    def get_object(self):
        return self.object


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


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.width = 0
        self.height = 0

        self.zoom = None

    def move(self, dx, dy):
        """Перемещает камеру на сколько-то пикселей во все стороны"""
        self.x += dx
        self.y += dy
        pass

    def move_teleport(self, new_x, new_y):
        """Перемещает камеру на любое положение"""
        self.x = new_x
        self.y = new_y

    def move_elastic(self, x, y, link):
        """
        link - объект, связывающий типа как веревкой камеру и точку, за которой та следит
        dist = [x - camera.x, y - camera.y]
        можно сделать с поправкой на угол а не только по x и y
        понадобятся cos, sin
        dx = link.max_speed * (dist[0] / link.max_dist)
        dx = link.max_speed * (dist[1] / link.max_dist)
        next_dot.x += dx
        """

    def zoom(self, zoom_state: int):
        """Зум камеры либо в 2 раза больше либо в 2 раза меньше
        придумай более удачное имя для zoom_state
        """
        pass

    def zoom_with_step(self, step: int):
        """Зум камеры с шагом, равным степеням двойки 2, 4, 8..."""
        pass

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
