import dearpygui.dearpygui as dpg

from imguipackage1.control.controls_control import ControlsSettings
from imguipackage1.imgui.tab_abc import TabInterface


class ControlsTab(TabInterface):
    def __init__(self, controls_settings: ControlsSettings):
        self.controls_settings = controls_settings
        pass

    def draw(self):
        with dpg.tab(label="Controls"):
            dpg.add_text("Control Settings Here")
            dpg.add_input_text(label="Key Bind", default_value="W")
