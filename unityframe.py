import customtkinter as ctk

from assetlib import unity_pic
class UnityFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.setup_unity_frame()

    def setup_unity_frame(self):
        self.master.change_geometry("400x600")

        self.unity_label = ctk.CTkLabel(self, text="Unity" ,
                                               anchor='center',font=("Old English Text",40,"bold"))
        self.unity_label.place(relx=0.35, rely=0.25)
        self.unity_logo_label = ctk.CTkLabel(self, image=unity_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.unity_logo_label.place(relx = 0.32 , rely = 0.013 )
        
        self.back_main_menu = ctk.CTkLabel(self,text='<--',font=("Old English Text",20,"bold"))
        self.back_main_menu.place(relx=0.2,rely=0.02)
        self.back_main_menu.bind("<Button-1>", lambda event: self.master.open_main_menu_frame("unity_frame"))
        self.back_main_menu.bind("<Enter>", lambda event: self.back_main_menu.configure(cursor="hand2",
                                                                                        text_color="green",text='Main Menu',font=("Old English Text",10,"bold")))
        self.back_main_menu.bind("<Leave>", lambda event: self.back_main_menu.configure(cursor="arrow",
                                                                                        text_color="white",text='<--',font=("Old English Text",20,"bold")))
        
     
