import pygame as pg

KEY_MAP = {
    "a": pg.K_a,
    "b": pg.K_b,
    "c": pg.K_c,
    "d": pg.K_d,
    "e": pg.K_e,
    "f": pg.K_f,
    "g": pg.K_g,
    "h": pg.K_h,
    "i": pg.K_i,
    "j": pg.K_j,
    "k": pg.K_k,
    "l": pg.K_l,
    "m": pg.K_m,
    "n": pg.K_n,
    "o": pg.K_o,
    "p": pg.K_p,
    "q": pg.K_q,
    "r": pg.K_r,
    "s": pg.K_s,
    "t": pg.K_t,
    "u": pg.K_u,
    "v": pg.K_v,
    "w": pg.K_w,
    "x": pg.K_x,
    "y": pg.K_y,
    "z": pg.K_z,
    "up": pg.K_UP,
    "down": pg.K_DOWN,
    "left": pg.K_LEFT,
    "right": pg.K_RIGHT,
    "space": pg.K_SPACE,
    "return": pg.K_RETURN,
    "escape": pg.K_ESCAPE,
    "l_shift": pg.K_LSHIFT,
    "l_ctrl": pg.K_LCTRL,
    "r_shift": pg.K_RSHIFT,
    "r_ctrl": pg.K_RCTRL
}

class Input:
    def __init__(self):
        self.keys = None
        self.previous_keys = None

    def update_keys(self):
        self.previous_keys = self.keys
        self.keys = pg.key.get_pressed()

    def is_key_pressed(self, key):
        return self.keys[KEY_MAP[key]]

    def input_began(self, key):
        if not self.previous_keys: return False
        if self.keys[KEY_MAP[key]] and not self.previous_keys[KEY_MAP[key]]:
            return True
        else: return False

    def input_ended(self, key):
        if not self.previous_keys: return False
        if self.previous_keys[KEY_MAP[key]] and not self.keys[KEY_MAP[key]]:
            return True
        else: return False