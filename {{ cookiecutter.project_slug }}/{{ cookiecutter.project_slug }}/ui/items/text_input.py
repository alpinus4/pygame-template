import pygame

from {{ cookiecutter.project_slug }}.ui.ui_item import UIItem
import {{ cookiecutter.project_slug }}.ui.utils as utils

class TextInput(UIItem):
    def __init__(self, x, y, width, height, submit_handler) -> None:
        super().__init__()
        self.handler = submit_handler
        self.value = ""
        self.rect = pygame.Rect(x, y, width, height)
        self.color = utils.WHITE , utils.GRAY
        self.active_color = utils.GRAY, utils.BLACK
        self.active = False
    
    def update(self, input):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if input.click:
                self.active = not self.active
        elif input.click:
            self.active = False
        
        if self.active:
            if input.backspace:
                self.value = self.value[:-1]
            elif input.enter:
                self.handler()
            elif input.unicode != "":
                self.value += input.unicode
            
    def draw(self, window):
        color = self.active_color if self.active else self.color
        pygame.draw.rect(window, color[0], self.rect)
        utils.draw_text_with_center_at(self.value, None, color[1], window,
                                       self.rect.centerx, self.rect.centery)