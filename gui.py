import tkinter as tk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoHotkey WH")
        self.geometry("400x300+300+150")
        self.resizable(False, False)

        self.key_var = tk.StringVar()

        self.key_label = tk.Label(self, text="HotKey")
        self.key_label.grid(row=0, column=0)

        self.key_entry = tk.Entry(self, textvariable=self.key_var)
        self.key_entry.grid(row=0, column=1)

        self.save_button = tk.Button(self, text="Save", command=self.save_key)
        self.save_button.grid(row=1, column=0, columnspan=2)

        self.bind('<Key>', self.key_pressed)

    def key_pressed(self, event):
        self.key_var.set(event.keysym)

    def save_key(self):
        self.saved_key = self.key_var.get()
        print(f"Key saved: {self.saved_key}")

app = Gui()
app.mainloop()