import dearpygui.dearpygui as dpg
from imguipackage1.imgui.tab_manager import TabManager


class ImGuiController:
    def __init__(self):
        self.tab_manager = TabManager()

    def create_main_window(self):
        with dpg.window(label="Main Window", width=400, height=300):

            with dpg.tab_bar(label="Settings"):
                self.tab_manager.create_tabs()

