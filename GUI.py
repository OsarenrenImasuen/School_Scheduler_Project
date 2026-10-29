from PySide6.QtWidgets import QApplication
from Calendar import CalendarFrame
import customtkinter as ctk
class GUI(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        super().__init__()
        self.title("Main Calendar")
        self.geometry("900x700")
        calend = CalendarFrame(self)
        calend.pack(fill ="both", expand=True)

if __name__ =="__main__":
    app = GUI()
    app.mainloop()
    
