import tkinter as tk
from gesture_detector import GestureController
import threading

def launch_gui():
    root = tk.Tk()
    root.title("Gesture-Controlled YouTube Navigator")

    label = tk.Label(root, text="Click 'Start' to begin gesture detection.", font=("Arial", 12))
    label.pack(pady=10)

    def start_detection():
        label.config(text="Gesture detection started... Press 'q' in webcam window to stop.")
        threading.Thread(target=GestureController().run, daemon=True).start()

    start_button = tk.Button(root, text="Start", command=start_detection)
    start_button.pack(pady=5)

    root.mainloop()
