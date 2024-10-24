from imguipackage1.imgui.audio_tab import AudioTab
from imguipackage1.imgui.controls_tab import ControlsTab
from imguipackage1.imgui.gameplay_tab import GameplayTab
from imguipackage1.imgui.graphics_tab import GraphicsTab


class TabManager:
    def __init__(self):
        self.tabs = [AudioTab(), ControlsTab(), GameplayTab(),GraphicsTab()]

    def create_tabs(self):
        for tab in self.tabs:
            tab.create()
