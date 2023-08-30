import pygame

from {{ cookiecutter.project_slug }}.ui.items.label import Label
import {{ cookiecutter.project_slug }}.ui.utils as utils

class LabelWithBackground(Label):
    def __init__(self, text, x, y, width, height, color) -> None:
        super().__init__(text, x, y, color)
        self.rect = pygame.Rect(x, y, width, height)
    
    def update(self, input):
        pass

    def draw(self, window):
        pygame.draw.rect(window, self.color[0], self.rect)
        utils.draw_text_with_center_at(self.text, None, self.color[1], window,
                                       self.rect.centerx, self.rect.centery)