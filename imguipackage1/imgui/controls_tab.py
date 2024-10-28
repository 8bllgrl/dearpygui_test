from imguipackage1.utils.keys import KeyboardKeys
import dearpygui.dearpygui as dpg
from imguipackage1.control.controls_control import ControlsSettings
from imguipackage1.imgui.tab_abc import TabInterface
from imguipackage1.theme.colors import Colors
from imguipackage1.theme.colorutils import ColorUtils


class ControlsTab(TabInterface):
    def __init__(self, controls_settings: ControlsSettings):
        self.controls_settings = controls_settings
        self.default_keybinds = {
            "Move Forward": dpg.mvKey_W,
            "Move Backward": dpg.mvKey_S,
            "Turn Left": dpg.mvKey_A,
            "Turn Right": dpg.mvKey_D,
            "Jump": dpg.mvKey_Spacebar,
            "Crouch": dpg.mvKey_C,
            "Attack": dpg.mvKey_F,
            "Open Inventory": dpg.mvKey_I,
            "Use Item": dpg.mvKey_E
        }
        self.current_keybinds = self.default_keybinds.copy()

        self.keybind_categories = {
            "Movement": ["Move Forward", "Move Backward", "Turn Left", "Turn Right"],
            "Actions": ["Jump", "Crouch", "Attack"],
            "Inventory": ["Open Inventory", "Use Item"]
        }

    def add_key_bind_pair(self, label, key_options):
        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_text(label)
            with dpg.table_cell():
                combo_id = f"combo_{label.replace(' ', '_')}"
                dpg.add_combo(key_options,
                              default_value=KeyboardKeys.get_key_string(self.current_keybinds[label]),
                              callback=lambda sender, app_data: self.key_changed(sender, app_data, label),
                              width=100,
                              tag=combo_id)

    def draw(self):
        with dpg.tab(label="Controls"):
            dpg.add_text("Control Settings Here")
            key_options = [KeyboardKeys.get_key_string(k) for k in KeyboardKeys.key_mapping]

            for category, labels in self.keybind_categories.items():
                dpg.add_text(category, color=ColorUtils.hex_to_rgba(Colors.SALMON.value), wrap=-1)
                dpg.add_separator()

                with dpg.table(header_row=False, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                               borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
                    dpg.add_table_column(init_width_or_weight=2)
                    dpg.add_table_column(init_width_or_weight=1)

                    for label in labels:
                        self.add_key_bind_pair(label, key_options)

    def key_changed(self, sender, app_data, label):
        selected_key_str = app_data
        selected_key = [k for k, v in KeyboardKeys.key_mapping.items() if v == selected_key_str][0]
        self.current_keybinds[label] = selected_key
        print(f"Updated Keybind for '{label}': {selected_key_str}, Key Code: {selected_key}")


