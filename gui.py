import tkinter as tk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoHotkey WH")
        self.geometry("400x300+300+150")
        self.resizable(False, False)

        self.key_var = tk.StringVar()
        self.speed_var = tk.StringVar(value="Slow")
        self.toggle_key_var = tk.StringVar()

        self.key_label = tk.Label(self, text="HotKey")
        self.key_label.grid(row=0, column=0)

        self.key_entry = tk.Entry(self, textvariable=self.key_var)
        self.key_entry.grid(row=0, column=1)

        self.speed_label = tk.Label(self, text="Speed")
        self.speed_label.grid(row=1, column=0)

        self.speed_options = ["Slow", "Medium", "Fast"]
        for i, option in enumerate(self.speed_options):
            rb = tk.Radiobutton(self, text=option, variable=self.speed_var, value=option)
            rb.grid(row=1, column=i+1)

        self.toggle_key_label = tk.Label(self, text="Toggle Key")
        self.toggle_key_label.grid(row=2, column=0)

        self.toggle_key_entry = tk.Entry(self, textvariable=self.toggle_key_var)
        self.toggle_key_entry.grid(row=2, column=1)

        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.grid(row=3, column=0, columnspan=4)

        self.bind('<Key>', self.key_pressed)

    def key_pressed(self, event):
        focused_widget = self.focus_get()
        if focused_widget == self.key_entry:
            self.key_var.set(event.keysym)
        elif focused_widget == self.toggle_key_entry:
            self.toggle_key_var.set(event.keysym)

    def save(self):
        self.saved_key = self.key_var.get()
        self.saved_speed = self.speed_var.get()
        self.saved_toggle_key = self.toggle_key_var.get()
        print(f"Key saved: {self.saved_key}, Speed: {self.saved_speed}, Toggle Key: {self.saved_toggle_key}")

app = Gui()
app.mainloop()