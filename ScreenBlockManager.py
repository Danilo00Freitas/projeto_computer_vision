import tkinter as tk
from PIL import Image, ImageTk

class ScreenBlockManager:
    def __init__(self, webcam_manager):
        self.webcam_manager = webcam_manager
        self.window = tk.Tk()
        self.window.wm_attributes('-fullscreen', True)
        self.window.configure(bg='black')
        self.window.bind('<Escape>', lambda e: self.close_window())
        self.label = None

    def update_frame(self):
        frame = self.webcam_manager.process_frame()

        if frame is None:
            self.window.after(10, self.update_frame)  # Retry if no frame
            return

        if frame is True:
            self.close_window()  # Close screen if both face and cup detected
            return

        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        if self.label is None:
            self.label = tk.Label(self.window, bg='black')
            self.label.place(relx=0.5, rely=0.5, anchor="center")

        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

        # Update the frame every 10 ms
        self.window.after(10, self.update_frame)

    def create_black_screen(self):
        self.update_frame()
        self.window.mainloop()

    def close_window(self):
        self.webcam_manager.release()
        self.window.destroy()