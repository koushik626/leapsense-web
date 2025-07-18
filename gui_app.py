import tkinter as tk
from clock_monitor import get_current_time
from leap_detector import detect_skipped_second
from logger import log_negative_leap
import time
import threading

class LeapSenseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LeapSense GUI")
        self.root.geometry("400x200")

        self.status_label = tk.Label(root, text="Status: Waiting", font=("Arial", 14))
        self.status_label.pack(pady=20)

        self.time_label = tk.Label(root, text="", font=("Courier", 12))
        self.time_label.pack()

        self.running = True
        self.previous_time = get_current_time()

        self.thread = threading.Thread(target=self.monitor_loop)
        self.thread.start()

    def monitor_loop(self):
        while self.running:
            time.sleep(1)
            current_time = get_current_time()
            if detect_skipped_second(self.previous_time, current_time):
                log_negative_leap(current_time)
                self.status_label.config(text="Status: Negative Leap Detected", fg="red")
            else:
                self.status_label.config(text="Status: Normal", fg="green")
            self.time_label.config(text=f"Time: {current_time}")
            self.previous_time = current_time

    def on_close(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LeapSenseGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
