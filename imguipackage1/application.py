import dearpygui.dearpygui as dpg
from imguipackage1.theme.theme import Theme
from viewport import Viewport
from imguipackage1.imgui.imgui_controller import ImGuiController

class Application:
    def __init__(self):
        self.theme = Theme()
        self.viewport = Viewport(800, 600)
        self.imgui_controller = ImGuiController()
        self.ui_visible = True
        self.main_window_id = None

    def run(self):
        dpg.create_context()
        self.theme.setup_theme()

        self.main_window_id = self.imgui_controller.create_main_window()
        print(f"Main window ID: {self.main_window_id}")

        self.viewport.create_viewport()
        self.viewport.center_on_monitor()

        with dpg.handler_registry():
            dpg.add_key_press_handler(dpg.mvKey_A, callback=self.on_a_press)
            dpg.add_key_press_handler(dpg.mvKey_Escape, callback=self.on_escape_press)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def on_a_press(self, sender, app_data):
        print("A pressed")

    def on_escape_press(self, sender, app_data):
        self.ui_visible = not self.ui_visible
        if self.ui_visible:
            dpg.show_item(self.main_window_id)
        else:
            dpg.hide_item(self.main_window_id)

