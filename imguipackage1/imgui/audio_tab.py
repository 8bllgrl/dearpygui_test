import dearpygui.dearpygui as dpg


class AudioTab:
    def __init__(self):
        self.master_volume = 0.5
        self.master_enabled = True
        self.audio_quality = "High"

        self.audio_controls = {
            "BGM": AudioControl("BGM", True, 0.5,
                                lambda s, a: self.update_control_enabled("BGM", a),
                                lambda s, a: self.update_control_volume("BGM", a)),
            "Performance": AudioControl("Performance", True, 0.5,
                                        lambda s, a: self.update_control_enabled("Performance", a),
                                        lambda s, a: self.update_control_volume("Performance", a)),
            "SFX": AudioControl("SFX", True, 0.5,
                                lambda s, a: self.update_control_enabled("SFX", a),
                                lambda s, a: self.update_control_volume("SFX", a)),
            "Voice": AudioControl("Voice", True, 0.5,
                                  lambda s, a: self.update_control_enabled("Voice", a),
                                  lambda s, a: self.update_control_volume("Voice", a)),
            "Ambient": AudioControl("Ambient", True, 0.5,
                                    lambda s, a: self.update_control_enabled("Ambient", a),
                                    lambda s, a: self.update_control_volume("Ambient", a))
        }

    def create(self):
        with dpg.tab(label="Audio"):
            dpg.add_text("Audio Settings", color=(255, 255, 255))

            self.master_control = AudioControl("Master Volume", self.master_enabled, self.master_volume,
                                               self.update_master_enabled, self.update_master_volume)
            self.master_control.create()

            dpg.add_text("Channel Volumes", bullet=True)
            for control in self.audio_controls.values():
                control.create()

            self.audio_quality_id = dpg.add_combo(label="Audio Quality", items=["Low", "Medium", "High"],
                                                  default_value=self.audio_quality, callback=self.update_audio_quality)
            dpg.add_button(label="Reset Audio Settings", callback=self.reset_audio_settings)

    def update_master_enabled(self, sender, app_data):
        self.master_enabled = app_data
        volume = self.master_volume if self.master_enabled else 0.0
        dpg.set_value(self.master_control.volume_id, volume)

    def update_master_volume(self, sender, app_data):
        self.master_volume = app_data

    def update_control_enabled(self, label, enabled):
        self.audio_controls[label].enabled = enabled

    def update_control_volume(self, label, volume):
        print(f"Updating volume for label: {label}")  # Debug print
        if label in self.audio_controls:
            self.audio_controls[label].volume = volume
        else:
            print(f"Error: {label} not found in audio_controls")  # More debugging

    def update_audio_quality(self, sender, app_data):
        self.audio_quality = app_data

    def reset_audio_settings(self, sender):
        self.master_volume = 0.5
        self.master_enabled = True
        self.audio_quality = "High"

        dpg.set_value(self.master_control.volume_id, self.master_volume)
        dpg.set_value(self.master_control.checkbox_id, self.master_enabled)

        for control in self.audio_controls.values():
            control.volume = 0.5
            control.enabled = True
            dpg.set_value(control.volume_id, control.volume)
            dpg.set_value(control.checkbox_id, control.enabled)

        dpg.set_value(self.audio_quality_id, self.audio_quality)


class AudioControl:
    def __init__(self, label, enabled, volume, enabled_callback, volume_callback):
        self.label = label
        self.enabled = enabled
        self.volume = volume
        self.enabled_callback = enabled_callback
        self.volume_callback = volume_callback
        self.checkbox_id = None
        self.volume_id = None

    def create(self):
        with dpg.group(horizontal=True):
            self.volume_id = dpg.add_slider_float(default_value=self.volume, min_value=0.0, max_value=1.0,
                                                  callback=self.volume_callback)
            self.checkbox_id = dpg.add_checkbox(default_value=self.enabled, callback=self.enabled_callback)
            dpg.add_text(self.label)
