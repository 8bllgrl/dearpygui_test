import dearpygui.dearpygui as dpg

class AudioTab:
    def __init__(self):
        pass

    def create(self):
        with dpg.tab(label="Audio"):
            dpg.add_text("Audio Settings Here")
            dpg.add_slider_float(label="Volume", default_value=0.5, min_value=0.0, max_value=1.0)
