class Tile:
    def __init__(self):
        pass

    def get_data_for_draw(self, camera):
        """Должна возвращать все актуальные для отрисовки спрайты
        для тайла"""
        pass


class Chunk:
    def __init__(self):
        pass

    def get_data_for_draw(self, camera):
        """Должна возвращать все актуальные для отрисовки спрайты
        для всего чанка"""
        pass


class Map:
    def __init__(self):
        pass

    def get_object_by_coord(self):
        """
        Возвращает полностью объект из тайла
        в чанке и тайле реализовать соотв методы, которые будет вызывать этот метод
        """

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


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.width = 0
        self.height = 0

        self.zoom = None

    def replace(self, dx, dy):
        """Перемещает камеру на сколько-то пикселей во все стороны"""
        pass

    def replace_teleport(self, new_x, new_y):
        """Перемещает камеру на любое положение"""
        pass

    def replace_elastic(self, x, y, link):
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
