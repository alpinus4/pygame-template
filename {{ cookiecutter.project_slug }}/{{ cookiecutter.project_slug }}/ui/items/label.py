from {{ cookiecutter.project_slug }}.ui.ui_item import UIItem
import {{ cookiecutter.project_slug }}.ui.utils as utils

class Label(UIItem):
    def __init__(self, text, x, y, color) -> None:
        super().__init__()
        self.text = text
        self.color = color
        self.x = x
        self.y = y
    
    def update(self, input):
        pass

    def draw(self, window):
        utils.draw_text(self.text, None, self.color, window, self.x, self.y)