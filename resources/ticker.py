import raylib
import pygame
import resources.button


FONT = raylib.LoadFont(b"assets/Arimo-VariableFont_wght.ttf")


class Ticker:
    def __init__(self, x, y, width, height, border_radius, font_size, init_value):
        self.position = pygame.Vector2(x, y)
        self.dimensions = pygame.Vector2(width, height)
        self.border_radius = border_radius
        self.font_size = font_size
        self.value = init_value

    def update(self):
        raylib.DrawRectangleRounded((self.position.x, self.position.y, self.dimensions.x, self.dimensions.y), self.border_radius, 1, raylib.WHITE)
        raylib.DrawRectangleRoundedLines((self.position.x, self.position.y, self.dimensions.x, self.dimensions.y), self.border_radius, 1, 2, raylib.BLACK)

        text_size = raylib.MeasureTextEx(FONT, str(self.value).encode("ascii"), self.font_size, 3)
        raylib.DrawTextEx(FONT, str(self.value).encode("ascii"), (self.position.x + self.dimensions.x / 2 - text_size.x / 2, self.position.y + self.dimensions.y / 2 - text_size.y / 2), self.font_size, 3, raylib.BLACK)

        button_up_size = raylib.MeasureTextEx(FONT, ">".encode("ascii"), self.font_size, 3)
        button_up = resources.button.Button(self.position.x + self.dimensions.x - button_up_size.x - 5, self.position.y, button_up_size.x + 5, self.dimensions.y, 1, 0.1, raylib.BLACK, raylib.WHITE, ">", raylib.BLACK, "rowar", self.font_size)
        
        button_down_size = raylib.MeasureTextEx(FONT, "<".encode("ascii"), self.font_size, 3)
        button_down = resources.button.Button(self.position.x + self.dimensions.x - button_up_size.x - button_down_size.x - 10, self.position.y, button_up_size.x + 5, self.dimensions.y, 1, 0.1, raylib.BLACK, raylib.WHITE, "<", raylib.BLACK, "rowar", self.font_size)

        if button_up.update():
            self.value += 1
        if button_down.update():
            self.value -= 1