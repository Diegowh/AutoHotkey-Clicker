from gui import Gui


class AutoHotkeyClicker:
    def __init__(self) -> None:
        self.gui = Gui()
        
    def run(self):
        self.gui.mainloop()
        
        
if __name__ == "__main__":
    app = AutoHotkeyClicker()
    app.run()