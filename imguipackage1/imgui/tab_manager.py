from imguipackage1.control.audio_control import AudioSettings
from imguipackage1.imgui.audio_tab import AudioTab
from imguipackage1.imgui.controls_tab import ControlsTab
from imguipackage1.imgui.gameplay_tab import GameplayTab
from imguipackage1.imgui.graphics_tab import GraphicsTab

class TabManager:
    def __init__(self):
        self.audio_manager = AudioSettings()
        self.tabs = [
            AudioTab(self.audio_manager),
            ControlsTab(),
            GameplayTab(),
            GraphicsTab()
        ]

    def create_tabs(self):
        for tab in self.tabs:
            tab.create()
