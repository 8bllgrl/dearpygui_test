import dearpygui.dearpygui as dpg

from imguipackage1.imgui.tab_abc import TabInterface


class GameplayTab(TabInterface):
    def __init__(self):
        self.difficulty = "Normal"
        self.show_hints = True

    def draw(self):
        with dpg.tab(label="Gameplay"):
            dpg.add_text("Gameplay Settings")
            dpg.add_combo(label="Difficulty", items=["Easy", "Normal", "Hard"], default_value=self.difficulty, callback=self.update_difficulty)
            dpg.add_checkbox(label="Show Hints", default_value=self.show_hints, callback=self.update_show_hints)

    def update_difficulty(self, sender, app_data):
        self.difficulty = app_data
        print(f"Difficulty set to {self.difficulty}")

    def update_show_hints(self, sender, app_data):
        self.show_hints = app_data
        status = "enabled" if self.show_hints else "disabled"
        print(f"Hints are now {status}")