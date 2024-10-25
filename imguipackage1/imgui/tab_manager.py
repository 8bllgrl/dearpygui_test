from imguipackage1.control.audio_control import AudioSettings
from imguipackage1.control.controls_control import ControlsSettings
from imguipackage1.control.gameplay_control import GameplaySettings
from imguipackage1.control.graphics_control import GraphicsSettings
from imguipackage1.imgui.audio_tab import AudioTab
from imguipackage1.imgui.controls_tab import ControlsTab
from imguipackage1.imgui.gameplay_tab import GameplayTab
from imguipackage1.imgui.graphics_tab import GraphicsTab


class TabManager:
    def __init__(self):
        self.audio_manager = AudioSettings()
        self.controls_manager = ControlsSettings()
        self.gameplay_manager = GameplaySettings()
        self.graphics_manager = GraphicsSettings()

        self.tabs = [
            AudioTab(self.audio_manager),
            ControlsTab(self.controls_manager),
            # GameplayTab(self.gameplay_manager),
            # GraphicsTab(self.graphics_manager)
        ]

    def draw_tabs(self):
        for tab in self.tabs:
            tab.create()
