from imguipackage1.control.audio_control import VolumeControl, AudioSettings
import dearpygui.dearpygui as dpg
from imguipackage1.theme.colors import Colors

class AudioTab:
    def __init__(self, audio_manager: AudioSettings):
        self.audio_manager = audio_manager

        self.master_volume_control = VolumeControl(
            self.audio_manager.master_volume,
            self.update_master_volume,
            "Master Volume"
        )
        self.music_volume_control = VolumeControl(
            self.audio_manager.music_volume,
            self.update_music_volume,
            "Music Volume"
        )

    def create(self):
        with dpg.tab(label="Audio"):
            self.add_audio_settings_text()
            self.master_volume_control.create()
            self.music_volume_control.create()
            self.add_reset_button()

    def add_audio_settings_text(self):
        dpg.add_text("Audio Settings", color=Colors.BRIGHT_WHITE, bullet=False)
        dpg.add_separator()

    def add_reset_button(self):
        dpg.add_button(label="Reset Audio Settings", callback=self.reset_audio_settings)

    def update_master_volume(self, sender, app_data):
        self.audio_manager.update_master_volume(app_data)
        dpg.set_value(self.master_volume_control.volume_id, self.audio_manager.master_volume)

    def update_music_volume(self, sender, app_data):
        self.audio_manager.update_music_volume(app_data)
        dpg.set_value(self.music_volume_control.volume_id, self.audio_manager.music_volume)

    def reset_audio_settings(self, sender):
        self.audio_manager.reset_audio_settings()
        dpg.set_value(self.master_volume_control.volume_id, self.audio_manager.master_volume)
        dpg.set_value(self.music_volume_control.volume_id, self.audio_manager.music_volume)
