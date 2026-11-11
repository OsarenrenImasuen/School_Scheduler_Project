import customtkinter as ctk


class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text="Notifcations", corner_radius=8, border_width=2)
        self.label.grid(row=0, column=0, padx=20)

class notifications(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("CTk example")
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = notifications()
app.mainloop()