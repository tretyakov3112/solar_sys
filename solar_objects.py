# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self):
        type = "star"
        """Признак объекта звезды"""

        m = 1
        """Масса звезды"""

        x = 0
        """Координата по оси **x**"""

        y = 0
        """Координата по оси **y**"""

        Vx = 0
        """Скорость по оси **x**"""

        Vy = 0
        """Скорость по оси **y**"""

        Fx = 0
        """Сила по оси **x**"""

        Fy = 0
        """Сила по оси **y**"""

        R = 5
        """Радиус звезды"""

        color = "red"
        """Цвет звезды"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self):
        type = "planet"
        """Признак объекта планеты"""

        m = 1
        """Масса планеты"""

        x = 0
        """Координата по оси **x**"""

        y = 0
        """Координата по оси **y**"""

        Vx = 0
        """Скорость по оси **x**"""

        Vy = 0
        """Скорость по оси **y**"""

        Fx = 0
        """Сила по оси **x**"""

        Fy = 0
        """Сила по оси **y**"""

        R = 5
        """Радиус планеты"""

        color = "green"
        """Цвет планеты"""