import dearpygui.dearpygui as dpg

class ControlsTab:
    def __init__(self):
        pass

    def create(self):
        with dpg.tab(label="Controls"):
            dpg.add_text("Control Settings Here")
            dpg.add_input_text(label="Key Bind", default_value="W")
