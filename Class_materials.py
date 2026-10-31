
import customtkinter as ctk

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class class_materials(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x700")
        self.title("Resources for classes")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.button = ctk.CTkButton(self,text="Class resources", command=self.open_toplevel)
        self.button.pack(side="top", padx=20, pady=10)

        self.toplevel_window = None


    # add methods to app
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            ctk.CTkInputDialog(text="Resources for Math: Pen, Notebooks, Pencil", title="Test")
        else:
            self.toplevel_window.focus()


app = class_materials()
app.mainloop()

    