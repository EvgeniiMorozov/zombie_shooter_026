from shooter.game_object.horizontal_bar import HorizontalBar
from shooter.config import GREEN
from shooter.config import WHITE


class PlayerHealthBar(HorizontalBar):
    def __init__(self, x, y, parameter, length, height, fill_color=WHITE, outline_color=GREEN):
        super().__init__(x, y, parameter, length, height, fill_color, outline_color)
