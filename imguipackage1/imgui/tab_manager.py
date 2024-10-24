from imguipackage1.imgui.audio_tab import AudioTab
from imguipackage1.imgui.controls_tab import ControlsTab


class TabManager:
    def __init__(self):
        self.audio_tab = AudioTab()
        self.controls_tab = ControlsTab()

    def create_tabs(self):
        self.audio_tab.create()
        self.controls_tab.create()
