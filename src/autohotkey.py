import keyboard
import time


class AutoHotkey:
    
    def __init__(self, key: str, toggle_key: str,  speed: str) -> None:
        self.key = key
        self.toggle = toggle_key
        self.speeds = {"Fast": 0.1, "Medium": 0.5, "Slow": 1}
        self.speed = self.speeds[speed]
        self.running = False
        
    def start(self):
        keyboard.add_hotkey(self.toggle, self.toggle_running)
        
        while True:
            if self.running:
                keyboard.press_and_release(self.key)
                time.sleep(self.speed)
            
            
    def toggle_running(self):
        self.running = not self.running