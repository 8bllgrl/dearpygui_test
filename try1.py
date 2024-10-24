import dearpygui.dearpygui as dpg
from screeninfo import get_monitors


# Set a dark theme
def setup_theme():
    with dpg.theme() as dark_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 30, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (60, 60, 60, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (80, 80, 80, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (100, 100, 100, 255))

    dpg.bind_theme(dark_theme)


dpg.create_context()
setup_theme()

with dpg.window(label="Themed Window"):
    dpg.add_button(label="Click Me")

# Create the viewport
viewport_width = 800
viewport_height = 600
dpg.create_viewport(title='Dear PyGui Themed Example', width=viewport_width, height=viewport_height)

# Get monitor information
monitors = get_monitors()

# Check if there are at least two monitors
if len(monitors) > 1:
    second_monitor = monitors[2]

    # Calculate center position on the second monitor
    center_x = second_monitor.x + (second_monitor.width - viewport_width) // 2
    center_y = second_monitor.y + (second_monitor.height - viewport_height) // 2

    # Set viewport position to center it on the second monitor
    dpg.set_viewport_pos((center_x, center_y))
else:
    print("Less than two monitors detected. Centering on the primary monitor.")
    # Center on the primary monitor instead
    primary_monitor = monitors[0]
    center_x = primary_monitor.x + (primary_monitor.width - viewport_width) // 2
    center_y = primary_monitor.y + (primary_monitor.height - viewport_height) // 2
    dpg.set_viewport_pos((center_x, center_y))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
