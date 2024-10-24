import dearpygui.dearpygui as dpg
class AudioTab:
    def __init__(self):
        self.volume = 0.5
        self.music_enabled = True

    def create(self):
        with dpg.tab(label="Audio"):
            dpg.add_text("Audio Settings")
            dpg.add_slider_float(label="Volume", default_value=self.volume, min_value=0.0, max_value=1.0, callback=self.update_volume)
            dpg.add_checkbox(label="Enable Music", default_value=self.music_enabled, callback=self.update_music)

    def update_volume(self, sender, app_data):
        self.volume = app_data
        print(f"Volume set to {self.volume:.2f}")

    def update_music(self, sender, app_data):
        self.music_enabled = app_data
        status = "enabled" if self.music_enabled else "disabled"
        print(f"Music is now {status}")