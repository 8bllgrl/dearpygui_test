import dearpygui.dearpygui as dpg


class KeyboardKeys:
    key_mapping = {
        dpg.mvKey_0: "0", dpg.mvKey_1: "1", dpg.mvKey_2: "2", dpg.mvKey_3: "3",
        dpg.mvKey_4: "4", dpg.mvKey_5: "5", dpg.mvKey_6: "6", dpg.mvKey_7: "7",
        dpg.mvKey_8: "8", dpg.mvKey_9: "9",
        dpg.mvKey_A: "A", dpg.mvKey_B: "B", dpg.mvKey_C: "C", dpg.mvKey_D: "D",
        dpg.mvKey_E: "E", dpg.mvKey_F: "F", dpg.mvKey_G: "G", dpg.mvKey_H: "H",
        dpg.mvKey_I: "I", dpg.mvKey_J: "J", dpg.mvKey_K: "K", dpg.mvKey_L: "L",
        dpg.mvKey_M: "M", dpg.mvKey_N: "N", dpg.mvKey_O: "O", dpg.mvKey_P: "P",
        dpg.mvKey_Q: "Q", dpg.mvKey_R: "R", dpg.mvKey_S: "S", dpg.mvKey_T: "T",
        dpg.mvKey_U: "U", dpg.mvKey_V: "V", dpg.mvKey_W: "W", dpg.mvKey_X: "X",
        dpg.mvKey_Y: "Y", dpg.mvKey_Z: "Z",
        dpg.mvKey_Spacebar: "Space", dpg.mvKey_Escape: "Escape", dpg.mvKey_Tab: "Tab",
        dpg.mvKey_Return: "Return", dpg.mvKey_Back: "Backspace", dpg.mvKey_Delete: "Delete",
        dpg.mvKey_Left: "Left Arrow", dpg.mvKey_Right: "Right Arrow", dpg.mvKey_Up: "Up Arrow",
        dpg.mvKey_Down: "Down Arrow", dpg.mvKey_Home: "Home", dpg.mvKey_End: "End",
        dpg.mvKey_Insert: "Insert", dpg.mvKey_F1: "F1", dpg.mvKey_F2: "F2",
        dpg.mvKey_F3: "F3", dpg.mvKey_F4: "F4", dpg.mvKey_F5: "F5", dpg.mvKey_F6: "F6",
        dpg.mvKey_F7: "F7", dpg.mvKey_F8: "F8", dpg.mvKey_F9: "F9", dpg.mvKey_F10: "F10",
        dpg.mvKey_F11: "F11", dpg.mvKey_F12: "F12",
        dpg.mvKey_NumPad0: "Numpad 0", dpg.mvKey_NumPad1: "Numpad 1", dpg.mvKey_NumPad2: "Numpad 2",
        dpg.mvKey_NumPad3: "Numpad 3", dpg.mvKey_NumPad4: "Numpad 4", dpg.mvKey_NumPad5: "Numpad 5",
        dpg.mvKey_NumPad6: "Numpad 6", dpg.mvKey_NumPad7: "Numpad 7", dpg.mvKey_NumPad8: "Numpad 8",
        dpg.mvKey_NumPad9: "Numpad 9",
        dpg.mvKey_Period: ".", dpg.mvKey_Comma: ",", dpg.mvKey_Minus: "-", dpg.mvKey_Plus: "+",
        dpg.mvKey_Slash: "/", dpg.mvKey_Backslash: "\\", dpg.mvKey_Quote: "'",
        dpg.mvKey_Colon: ":", dpg.mvKey_Open_Brace: "[", dpg.mvKey_Close_Brace: "]", dpg.mvKey_Tilde: "~",
    }

    modifier_mapping = {
        dpg.mvKey_LShift: "Shift",
        dpg.mvKey_RShift: "Shift",
        dpg.mvKey_LControl: "Control",
        dpg.mvKey_RControl: "Control",
        dpg.mvKey_LAlt: "Alt",
        dpg.mvKey_RAlt: "Alt",
    }

    @classmethod
    def get_key_string(cls, key_code):
        return cls.key_mapping.get(key_code, str(key_code))
