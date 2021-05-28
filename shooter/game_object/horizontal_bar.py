import pygame


class HorizontalBar:
    def __init__(self, x, y, parameter, length, height, fill_color, outline_color):
        """
        x - координата х
        н - координата y
        parameter - параметр, который будет визуализирован
        length - длина прямоугольника
        height - высота прямоугольника
        fill_color - цвет внутреннего прямоугольника
        outline_color - цвет внешного (нижнего) прямоугольника
        """
        self.x = x
        self.y = y
        self.parameter = parameter
        self.length = length
        self.height = height
        self.fill = (self.parameter / 100) * self.length
        self.outline_color = outline_color
        self.fill_color = fill_color
        self.outline_rect = pygame.Rect(self.x, self.y, self.length, self.height)
        self.fill_rect = pygame.Rect(self.x, self.y, self.fill, self.height)

    def parameter_scaling(self):
        pass

    def blit(self, surface):
        pygame.draw.rect(surface, self.outline_color, self.outline_rect, 2)
        pygame.draw.rect(surface, self.fill_color, self.fill_rect)
