import customtkinter as ctk
class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text="Sign up", corner_radius=8, border_width=2)
        self.entry1 = ctk.CTkEntry(self, placeholder_text="Username")
        self.entry1.grid(row=10, column=10, padx=30)
        self.entry2 = ctk.CTkEntry(self, placeholder_text="Password")
        self.entry2.grid(row=30, column=10, padx=10)
        self.label.grid(row=0, column=0, padx=20)

class Sign_up(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Sign up page")

        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1)
        
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.button = ctk.CTkButton(self, text="Sign up", command=self.button_event)
        self.button.grid(row=40,column=40, padx=20, pady=10)

    def button_event(self):
        print("button pressed")

app = Sign_up()
app.mainloop()