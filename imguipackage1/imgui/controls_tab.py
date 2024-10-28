import dearpygui.dearpygui as dpg
from imguipackage1.control.controls_control import ControlsSettings
from imguipackage1.imgui.tab_abc import TabInterface
from imguipackage1.utils.keys import KeyboardKeys
class ControlsTab(TabInterface):
    def __init__(self, controls_settings: ControlsSettings):
        self.controls_settings = controls_settings
        self.selected_key = dpg.mvKey_W
        # Define a list of keybind labels to be used dynamically
        self.keybind_labels = ["Key Bind 1", "Key Bind 2", "Key Bind 3"]  # Add or remove labels as needed

    def add_key_bind_pair(self, label, key_options):
        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_text(label)
            with dpg.table_cell():
                dpg.add_combo(key_options, default_value=KeyboardKeys.get_key_string(self.selected_key),
                              callback=self.key_changed, width=100)

    def draw(self):
        with dpg.tab(label="Controls"):
            dpg.add_text("Control Settings Here")
            key_options = [KeyboardKeys.get_key_string(k) for k in KeyboardKeys.key_mapping]

            with dpg.table(header_row=False, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                           borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
                dpg.add_table_column(init_width_or_weight=2)  # Make first column wider
                dpg.add_table_column(init_width_or_weight=1)  # Make second column narrower

                # Dynamically create rows based on keybind_labels
                for label in self.keybind_labels:
                    self.add_key_bind_pair(label, key_options)

    def key_changed(self, sender, app_data):
        selected_key_str = app_data
        self.selected_key = [k for k, v in KeyboardKeys.key_mapping.items() if v == selected_key_str][0]
        print(f"Selected Key: {selected_key_str}, Key Code: {self.selected_key}")
