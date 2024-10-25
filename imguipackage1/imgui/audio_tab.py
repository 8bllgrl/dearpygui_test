from imguipackage1.control.audio_control import VolumeControl, AudioSettings, AudioSetting
import dearpygui.dearpygui as dpg

from imguipackage1.imgui.tab_abc import TabInterface
from imguipackage1.theme.colors import Colors


class AudioTab(TabInterface):
    def __init__(self, audio_settings: AudioSettings):
        self.audio_settings = audio_settings
        self.volume_controls = []

    def create(self):
        with dpg.tab(label="Audio"):
            self.add_audio_settings_text()
            self.add_volume_control("Master Volume", self.audio_settings.master_volume, AudioSetting.MASTER_VOLUME)
            dpg.add_spacer(width=0, height=3)  # This is weird to be here but dealing with it.
            self.add_volume_control("Music", self.audio_settings.music_volume, AudioSetting.MUSIC_VOLUME)
            self.add_volume_control("Sound Effects", self.audio_settings.sfx_volume, AudioSetting.SFX_VOLUME)
            self.add_volume_control("Voice", self.audio_settings.voice_volume, AudioSetting.VOICE_VOLUME)
            self.add_volume_control("Ambience", self.audio_settings.ambience_volume, AudioSetting.AMBIENCE_VOLUME)
            self.add_reset_button()

    def add_audio_settings_text(self):
        dpg.add_text("Audio Settings", color=Colors.BRIGHT_WHITE, bullet=False)
        dpg.add_separator()

    def add_reset_button(self):
        dpg.add_button(label="Reset Audio Settings", callback=self.reset_audio_settings)

    def add_volume_control(self, label, initial_value, setting_id):
        volume_control = VolumeControl(
            initial_value,
            lambda sender, app_data: self.update_volume(setting_id, app_data),
            label,
            setting_id
        )
        volume_control.create()
        self.volume_controls.append(volume_control)

    def update_volume(self, setting_id, app_data):
        self.audio_settings.update_volume(setting_id, app_data)
        for control in self.volume_controls:
            if control.setting_id == setting_id:
                dpg.set_value(control.volume_id, app_data)

    def reset_audio_settings(self, sender):
        self.audio_settings.reset_audio_settings()
        for control in self.volume_controls:
            dpg.set_value(control.volume_id,
                          self.audio_settings.master_volume if control.setting_id == AudioSetting.MASTER_VOLUME else self.audio_settings.music_volume)
