import dearpygui.dearpygui as dpg
from imguipackage1.theme.theme import Theme
from viewport import Viewport
from imguipackage1.imgui.imgui_controller import ImGuiController

class Application:
    def __init__(self):
        self.theme = Theme()
        self.viewport = Viewport(800, 600)
        self.imgui_controller = ImGuiController()

    def run(self):
        dpg.create_context()
        self.theme.setup_theme()

        self.imgui_controller.create_main_window()

        self.viewport.create_viewport()
        self.viewport.center_on_monitor()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
