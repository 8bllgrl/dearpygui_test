import dearpygui.dearpygui as dpg
from imguipackage1.imgui.tab_manager import TabManager

class ImGuiController:
    def __init__(self):
        self.tab_manager = TabManager()

    def create_main_window(self):
        window_id = "main_window"
        with dpg.window(label="Main Window", width=400, height=300, tag=window_id):
            with dpg.tab_bar(label="Settings"):
                self.tab_manager.draw_tabs()
        return window_id
