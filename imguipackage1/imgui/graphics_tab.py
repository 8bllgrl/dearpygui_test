import dearpygui.dearpygui as dpg

from imguipackage1.imgui.tab_abc import TabInterface


class GraphicsTab(TabInterface):
    def __init__(self):
        self.resolution = (1920, 1080)
        self.fullscreen = False

    def create(self):
        with dpg.tab(label="Graphics"):
            dpg.add_text("Graphics Settings")
            dpg.add_combo(label="Resolution", items=["1920x1080", "1280x720", "800x600"], default_value="1920x1080", callback=self.update_resolution)
            dpg.add_checkbox(label="Fullscreen", default_value=self.fullscreen, callback=self.update_fullscreen)

    def update_resolution(self, sender, app_data):
        self.resolution = tuple(map(int, app_data.split('x')))
        print(f"Resolution set to {self.resolution[0]}x{self.resolution[1]}")

    def update_fullscreen(self, sender, app_data):
        self.fullscreen = app_data
        status = "enabled" if self.fullscreen else "disabled"
        print(f"Fullscreen is now {status}")
