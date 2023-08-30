from abc import ABC, abstractmethod


class Screen(ABC):
    def __init__(self, window, change_screen_callback) -> None:
        self.window = window
        self.change_screen_callback = change_screen_callback
        self.input = None

    @abstractmethod
    def update(self, delta_time):
        pass

    @abstractmethod
    def quit(self):
        pass
