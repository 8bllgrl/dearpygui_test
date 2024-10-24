import dearpygui.dearpygui as dpg
from imguipackage1.theme.colors import Colors
from imguipackage1.theme.colorutils import ColorUtils

class Theme:
    def __init__(self):
        self.dark_theme = None

    def setup_theme(self):
        with dpg.theme() as self.dark_theme:
            with dpg.theme_component(dpg.mvAll):
                self.setup_text_and_background_colors()
                self.setup_tab_colors()
                self.setup_button_and_slider_colors()
                self.setup_plot_and_graph_colors()
                self.setup_border_and_separator_colors()
                self.setup_frame_and_header_colors()
                self.setup_scrollbar_colors()
                self.setup_miscellaneous_colors()

        dpg.bind_theme(self.dark_theme)

    def setup_text_and_background_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_Text, ColorUtils.hex_to_rgba(Colors.BRIGHT_WHITE.value))
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, ColorUtils.hex_to_rgba(Colors.DARK_GRAY.value))

    def setup_tab_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, ColorUtils.hex_to_rgba(Colors.LIGHT_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, ColorUtils.hex_to_rgba(Colors.LIGHT_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_Header, ColorUtils.hex_to_rgba(Colors.DARK_GRAY.value))

    def setup_button_and_slider_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_Button, ColorUtils.hex_to_rgba(Colors.DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, ColorUtils.hex_to_rgba(Colors.DARK_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, ColorUtils.hex_to_rgba(Colors.LIGHT_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, ColorUtils.hex_to_rgba(Colors.LIGHT_RED.value))

    def setup_plot_and_graph_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_PlotLines, ColorUtils.hex_to_rgba(Colors.LIGHT_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered, ColorUtils.hex_to_rgba(Colors.BRIGHT_WHITE.value))
        dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, ColorUtils.hex_to_rgba(Colors.DARK_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered, ColorUtils.hex_to_rgba(Colors.BRIGHT_WHITE.value))

    def setup_border_and_separator_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_Border, ColorUtils.hex_to_rgba(Colors.GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, ColorUtils.hex_to_rgba(Colors.BLACK.value))
        dpg.add_theme_color(dpg.mvThemeCol_Separator, ColorUtils.hex_to_rgba(Colors.GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, ColorUtils.hex_to_rgba(Colors.LIGHT_GRAY.value))

    def setup_frame_and_header_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, ColorUtils.hex_to_rgba(Colors.DARKER_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, ColorUtils.hex_to_rgba(Colors.GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, ColorUtils.hex_to_rgba(Colors.LIGHT_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, ColorUtils.hex_to_rgba(Colors.DARK_GRAY.value))

    def setup_scrollbar_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, ColorUtils.hex_to_rgba(Colors.DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, ColorUtils.hex_to_rgba(Colors.LIGHT_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))

    def setup_miscellaneous_colors(self):
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, ColorUtils.hex_to_rgba(Colors.BRIGHT_WHITE.value))
        dpg.add_theme_color(dpg.mvThemeCol_NavHighlight, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg, ColorUtils.hex_to_rgba(Colors.VERY_DARK_GRAY.value))
        dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget, ColorUtils.hex_to_rgba(Colors.CRISPY_RED.value))
        dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, ColorUtils.hex_to_rgba(Colors.BLACK.value))
