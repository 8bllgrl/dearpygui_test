class ColorUtils:
    @staticmethod
    def hex_to_rgba(hex_color):
        # Convert hex to RGBA
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)
