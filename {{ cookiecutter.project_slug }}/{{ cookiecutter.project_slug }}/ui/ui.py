from {{ cookiecutter.project_slug }}.ui.ui_item import UIItem

class UI:
    def __init__(self, window, input) -> None:
        self.window = window
        self.input = input
        self.items = []

    def register(self, item: UIItem):
        self.items.append(item)
        return self

    def update(self):
        for item in self.items:
            if item.visible:
                item.update(self.input)
                item.draw(self.window)
