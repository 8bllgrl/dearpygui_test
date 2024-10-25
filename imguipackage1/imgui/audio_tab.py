from imguipackage1.control.audio_control import VolumeControl, AudioSettings
import dearpygui.dearpygui as dpg
from imguipackage1.theme.colors import Colors

class AudioTab:
    def __init__(self, audio_manager: AudioSettings):
        self.audio_manager = audio_manager
        self.volume_controls = []

    def create(self):
        with dpg.tab(label="Audio"):
            self.add_audio_settings_text()
            self.add_volume_control("Master Volume", self.audio_manager.master_volume, self.audio_manager.update_master_volume)
            self.add_volume_control("Music Volume", self.audio_manager.music_volume, self.audio_manager.update_music_volume)
            self.add_reset_button()

    def add_audio_settings_text(self):
        dpg.add_text("Audio Settings", color=Colors.BRIGHT_WHITE, bullet=False)
        dpg.add_separator()

    def add_reset_button(self):
        dpg.add_button(label="Reset Audio Settings", callback=self.reset_audio_settings)

    def add_volume_control(self, label, initial_value, update_callback):
        volume_control = VolumeControl(initial_value, lambda sender, app_data: self.update_volume(update_callback, app_data, volume_control), label)
        volume_control.create()
        self.volume_controls.append(volume_control)

    def update_volume(self, update_callback, app_data, volume_control):
        update_callback(app_data)
        dpg.set_value(volume_control.volume_id, app_data)

    def reset_audio_settings(self, sender):
        self.audio_manager.reset_audio_settings()
        for control in self.volume_controls:
            if control.label == "Master Volume":
                dpg.set_value(control.volume_id, self.audio_manager.master_volume)
            elif control.label == "Music Volume":
                dpg.set_value(control.volume_id, self.audio_manager.music_volume)
