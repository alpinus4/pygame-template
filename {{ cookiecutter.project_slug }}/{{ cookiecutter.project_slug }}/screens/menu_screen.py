import pygame

import {{ cookiecutter.project_slug }}.config as c
from {{ cookiecutter.project_slug }}.screens.screen import Screen
from {{ cookiecutter.project_slug }}.input import Input
from {{ cookiecutter.project_slug }}.ui.ui import UI
from {{ cookiecutter.project_slug }}.ui.items.label import Label
from {{ cookiecutter.project_slug }}.ui.items.button import Button
import {{ cookiecutter.project_slug }}.ui.utils as ui_utils


class MenuScreen(Screen):
    def __init__(self, window, change_screen_callback) -> None:
        super().__init__(window, change_screen_callback)
        self.input = Input()
        self.UI = UI(window, self.input)
        self.title = Label("{{ cookiecutter.project_name }}", 10, c.WINDOW_HEIGHT / 2 - 100, ui_utils.WHITE)
        self.play_button = Button("Play", c.WINDOW_WIDTH/2 - 50, c.WINDOW_HEIGHT / 2 - 100, 100, 50)
        self.UI.register(self.title).register(self.play_button)

    def update(self, delta_time):
        self.window.fill(ui_utils.BLACK)
        self.input.handle()
        self.UI.update()

    def quit(self):
        pass
