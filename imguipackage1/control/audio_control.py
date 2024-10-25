import dearpygui.dearpygui as dpg

class VolumeControl:
    def __init__(self, volume, volume_callback, label):
        self.volume = volume
        self.volume_callback = volume_callback
        self.label = label
        self.volume_id = None

    def create(self):
        with dpg.group(horizontal=True):
            self.volume_id = dpg.add_slider_float(default_value=self.volume, min_value=0.0, max_value=1.0,
                                                  callback=self.volume_callback)
            dpg.add_text(self.label)

class AudioSettings:
    def __init__(self):
        self.master_volume = 0.5
        self.music_volume = 0.5

    def update_master_volume(self, volume):
        self.master_volume = volume
        print(f"Master Volume set to {self.master_volume:.2f}")

    def update_music_volume(self, volume):
        self.music_volume = volume
        print(f"Music Volume set to {self.music_volume:.2f}")

    def reset_audio_settings(self):
        self.master_volume = 0.5
        self.music_volume = 0.5
        print("Audio settings have been reset to default.")
