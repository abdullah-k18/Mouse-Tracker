import tkinter as tk
from pynput import mouse
import threading

class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Tracker")
        self.label = tk.Label(root, text="Your Mouse has traveled \n 0 pixels", font=("Impact", 16))
        self.label.pack(padx=20, pady=20)

        self.total_distance = 0
        self.last_position = None

        self.listener = mouse.Listener(on_move=self.on_move)
        self.listener.start()

    def on_move(self, x, y):
        if self.last_position is not None:
            dx = x - self.last_position[0]
            dy = y - self.last_position[1]
            distance = (dx**2 + dy**2) ** 0.5
            self.total_distance += distance
            self.update_label()
        self.last_position = (x, y)

    def update_label(self):
        self.label.config(text=f"Your Mouse has traveled \n {int(self.total_distance)} pixels")

    def on_closing(self):
        self.listener.stop()
        self.root.destroy()


root = tk.Tk()
app = MouseTrackerApp(root)
root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()