import dearpygui.dearpygui as dpg
from enum import Enum


class AudioSetting(Enum):
    MASTER_VOLUME = 1
    MUSIC_VOLUME = 2
    SFX_VOLUME = 3
    VOICE_VOLUME = 4
    AMBIENCE_VOLUME = 5


class VolumeControl:
    def __init__(self, volume, volume_callback, label, setting_id):
        self.volume = volume
        self.volume_callback = volume_callback
        self.label = label
        self.setting_id = setting_id
        self.volume_id = None
        self.checkbox_id = None
        self.is_enabled = True
        self.last_set_volume = volume

    def create(self):
        with dpg.group(horizontal=True):
            self.volume_id = dpg.add_slider_float(default_value=self.volume, min_value=0.0, max_value=1.0,
                                                  callback=self.volume_change_callback)
            self.checkbox_id = dpg.add_checkbox(label="", callback=self.toggle_volume, default_value=True)
            dpg.add_text(self.label)

    def volume_change_callback(self, sender, app_data):
        if not self.is_enabled:
            # If the control is muted, update last_set_volume but do not change the actual volume
            self.last_set_volume = app_data
            print(f"{self.label} adjusted while muted. New Previous Volume: {self.last_set_volume:.2f}")
        self.volume_callback(sender, app_data)

    def toggle_volume(self, sender, app_data):
        self.is_enabled = app_data
        if self.is_enabled:
            # If unmuted, restore the visual volume.
            dpg.set_value(self.volume_id, self.last_set_volume)
            print(f"{self.label} is unmuted. Previous Volume: {self.last_set_volume:.2f}, "
                  f"New Volume: {self.last_set_volume:.2f}, Enabled: {self.is_enabled}")
        else:
            self.last_set_volume = dpg.get_value(self.volume_id)
            dpg.set_value(self.volume_id, self.last_set_volume)
            print(f"{self.label} is muted. Previous Volume: {self.last_set_volume:.2f}, "
                  f"New Volume: 0.0, Enabled: {self.is_enabled}")



class AudioSettings:
    def __init__(self):
        self.master_volume = 0.5
        self.music_volume = 0.5
        self.sfx_volume = 0.5
        self.voice_volume = 0.5
        self.ambience_volume = 0.5

    def update_volume(self, setting_id, volume):
        if setting_id in AudioSetting:
            if setting_id == AudioSetting.MASTER_VOLUME:
                self.master_volume = volume
            elif setting_id == AudioSetting.MUSIC_VOLUME:
                self.music_volume = volume

            print(f"{setting_id.name.replace('_', ' ').title()} set to {volume:.2f}")

    def reset_audio_settings(self):
        self.master_volume = 0.5
        self.music_volume = 0.5
        print("Audio settings have been reset to default.")
