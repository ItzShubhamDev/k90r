import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner

from kmk.modules.layers import Layers
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
i2c = busio.I2C(board.SCL, board.SDA)

class Display(SSD1306_I2C):
    def on_layer_change(self, layer: int):
        self.fill(0)
        self.text(f'K90R - {layer}', 0, 0, 1)
        self.show()

display = Display(128, 32, i2c)  
keyboard.extensions.append(display)  

keyboard.row_pins = (board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0)
keyboard.col_pins = (
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
    board.GP27, board.GP26, board.GP22, board.GP21, board.GP20
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
macros = Macros()
encoder_handler.pins = ((board.GP19, board.GP18, None))

keyboard.modules.append(macros)
keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

rgb = RGB(pixel_pin=board.GP28, num_pixels=90)
keyboard.extensions.append(rgb)

keyboard.keymap = [
  # Layer 0: Default Layer
  [
    KC.ESC, KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, KC.PSCR, KC.PAUS, KC.DEL, KC.MUTE,
    KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.HOME, KC.MPLY,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.PGUP, KC.END, KC.MNXT,
    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGDN, KC.MPRV,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.MSTP,
    KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.MO(1), KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.LT(2, KC.RGB_TOG)
  ],
  # Layer 1: Function layer - Yet to be defined
  [
    KC.ESC, KC.F1, KC.F2, KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, KC.PSCR, KC.PAUS, KC.DEL, KC.MUTE,
    KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.HOME, KC.MPLY,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.PGUP, KC.END, KC.MNXT,
    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGDN, KC.MPRV,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.MSTP,
    KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.MO(1), KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.LT(2, KC.RGB_TOG)
  ],
  # Layer 2: LED Control Layer
  [
    KC.ESC, KC.F1, KC.F2, KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, KC.PSCR, KC.PAUS, KC.DEL, KC.RGB_MODE_PLAIN,
    KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.HOME, KC.RGB_HUI,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.PGUP, KC.END, KC.RGB_HUD,
    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGDN, KC.RGB_SAI,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.RGB_SAD,
    KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.MO(1), KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.LT(2, KC.RGB_TOG)
  ]
]

rgb_modes = [
    KC.RGB_MODE_BREATHE,
    KC.RGB_MODE_RAINBOW,
    KC.RGB_MODE_BREATHE_RAINBOW,
    KC.RGB_MODE_KNIGHT,
    KC.RGB_MODE_SWIRL,
]

current_mode = 0

def rgb_mode_change(clockwise=False):
    global current_mode
    
    if clockwise:
      current_mode = current_mode + 1 if current_mode < len(rgb_modes) - 1 else 0
    else:
      current_mode = current_mode - 1 if current_mode > 0 else len(rgb_modes) - 1

    return Tap(rgb_modes[current_mode])

encoder_handler.map = [
  [
    KC.VOLD, KC.VOLU
  ],
  [
    KC.VOLD, KC.VOLU
  ],
  [
    rgb_mode_change(True), rgb_mode_change()
  ]
]

display.fill(0)
display.text('K7R', 0, 0, 1)
display.show()

if __name__ == '__main__':
    keyboard.go()