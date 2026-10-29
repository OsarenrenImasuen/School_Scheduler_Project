
import customtkinter as ctk
class class_materials(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x700")
        self.title("Resources for classes")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")



app = class_materials()
app.mainloop()

    