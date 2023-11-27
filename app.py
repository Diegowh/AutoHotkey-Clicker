import keyboard
import time

key = "a"
frequency = 1

class AutoHotkeyClicker:
    
    def __init__(self, key: str, key_bind: str,  delay: int) -> None:
        self.key = key
        self.delay = delay
        
    def start(self):
        for _ in range(5):
            keyboard.press_and_release(self.key)
            time.sleep(self.frequency)
            
            


if __name__ == "__main__":
    clicker = AutoHotkeyClicker(key, frequency, 1)
    clicker.start()