import dearpygui.dearpygui as dpg


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


class AudioTab:
    def __init__(self):
        self.master_volume = 0.5
        self.audio_quality = "High"

        # Audio controls
        self.audio_controls = {
            "BGM": AudioControl("BGM", True, 0.5, lambda s, a: self.update_control_enabled("BGM", a),
                                lambda s, a: self.update_control_volume("BGM", a)),
            "Performance": AudioControl("Performance", True, 0.5,
                                        lambda s, a: self.update_control_enabled("Performance", a),
                                        lambda s, a: self.update_control_volume("Performance", a)),
            "SFX": AudioControl("SFX", True, 0.5, lambda s, a: self.update_control_enabled("SFX", a),
                                lambda s, a: self.update_control_volume("SFX", a)),
            "Voice": AudioControl("Voice", True, 0.5, lambda s, a: self.update_control_enabled("Voice", a),
                                  lambda s, a: self.update_control_volume("Voice", a)),
            "Ambient": AudioControl("Ambient", True, 0.5, lambda s, a: self.update_control_enabled("Ambient", a),
                                    lambda s, a: self.update_control_volume("Ambient", a))
        }

    def create(self):
        with dpg.tab(label="Audio"):
            dpg.add_text("Audio Settings", color=(255, 255, 255))
            dpg.add_slider_float(label="Master Volume", default_value=self.master_volume, min_value=0.0, max_value=1.0,
                                 callback=self.update_master_volume)

            dpg.add_text("Channel Volumes", bullet=True)
            for control in self.audio_controls.values():
                control.create()

            self.audio_quality_id = dpg.add_combo(label="Audio Quality", items=["Low", "Medium", "High"],
                                                  default_value=self.audio_quality, callback=self.update_audio_quality)
            dpg.add_button(label="Reset Audio Settings", callback=self.reset_audio_settings)

    def update_master_volume(self, sender, app_data):
        self.master_volume = app_data
        print(f"Master Volume set to {self.master_volume:.2f}")

    def update_control_enabled(self, label, enabled):
        print(f"{label} is now {'enabled' if enabled else 'disabled'}")
        self.audio_controls[label].enabled = enabled

    def update_control_volume(self, label, volume):
        print(f"{label} Volume set to {volume:.2f}")
        self.audio_controls[label].volume = volume

    def update_audio_quality(self, sender, app_data):
        self.audio_quality = app_data
        print(f"Audio Quality set to {self.audio_quality}")

    def reset_audio_settings(self, sender):
        self.master_volume = 0.5
        self.audio_quality = "High"

        dpg.set_value(self.audio_quality_id, self.audio_quality)
        for control in self.audio_controls.values():
            control.volume = 0.5
            control.enabled = True
            dpg.set_value(control.volume_id, control.volume)
            dpg.set_value(control.checkbox_id, control.enabled)

        dpg.set_value(self.master_volume_id, self.master_volume)
        print("Audio settings have been reset to default.")

