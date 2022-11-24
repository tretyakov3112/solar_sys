# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self):
        self.type = "star"
        """Признак объекта звезды"""

        self.m = 1
        """Масса звезды"""

        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.Vx = 0
        """Скорость по оси **x**"""

        self.Vy = 0
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = 5
        """Радиус звезды"""

        self.color = "red"
        """Цвет звезды"""




class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self):
        self.type = "planet"
        """Признак объекта планеты"""

        self.m = 1
        """Масса планеты"""

        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.Vx = 0
        """Скорость по оси **x**"""

        self.Vy = 0
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = 5
        """Радиус планеты"""

        self.color = "green"
        """Цвет планеты"""