import dearpygui.dearpygui as dpg
from screeninfo import get_monitors

# Window.
class Viewport:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_viewport(self):
        dpg.create_viewport(title='Dear PyGui Themed Example', width=self.width, height=self.height)

    def center_on_monitor(self):
        monitors = get_monitors()

        if len(monitors) > 2:
            second_monitor = monitors[2]
            center_x = second_monitor.x + (second_monitor.width - self.width) // 2
            center_y = second_monitor.y + (second_monitor.height - self.height) // 2
        else:
            print("Less than two monitors detected. Centering on the primary monitor.")
            primary_monitor = monitors[0]
            center_x = primary_monitor.x + (primary_monitor.width - self.width) // 2
            center_y = primary_monitor.y + (primary_monitor.height - self.height) // 2

        dpg.set_viewport_pos((center_x, center_y))
