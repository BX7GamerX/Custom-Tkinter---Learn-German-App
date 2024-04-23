import customtkinter as ctk
from assetlib import spielen_pic
class A1DeutschFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.setup_a1_deutsch_frame()

    def setup_a1_deutsch_frame(self):
        self.master.change_geometry("400x600")
        self.a1_deutch_frame = ctk.CTkFrame(self, width=320, height=380)  
        self.a1_deutch_frame.place(relx=0.1,rely=0.25)        
        self.a1_deutch_label = ctk.CTkLabel(self, text="A1 Deutsch" ,
                                               anchor='center',font=("Old English Text",20,"bold"))
        self.a1_deutch_label.place(relx=0.3, rely=0.05)
        self.back_main_menu = ctk.CTkLabel(self,text='<--',font=("Old English Text",20,"bold"))
        self.back_main_menu.place(relx=0.2,rely=0.02)
        self.back_main_menu.bind("<Button-1>", lambda event: self.master.open_main_menu_frame("a1_deutsch_frame"))
        self.back_main_menu.bind("<Enter>", lambda event: self.back_main_menu.configure(cursor="hand2",
                                                                                        text_color="green",text='Main Menu',font=("Old English Text",10,"bold")))
        self.back_main_menu.bind("<Leave>", lambda event: self.back_main_menu.configure(cursor="arrow",
                                                                                        text_color="white",text='<--',font=("Old English Text",20,"bold")))
        


        self.dict_label = ctk.CTkLabel(self.a1_deutch_frame, text="Deutsch Dictionary",
                                                                font=('Century Gothic', 15))
        self.dict_label.place(relx = 0.15 , rely = 0.25)
        self.dict_label.bind("<Button-1>", lambda event: self.master.open_translator_frame())
        self.dict_label.bind("<Enter>", lambda event: self.dict_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))# mainmenu_colour.frame_light))
        self.dict_label.bind("<Leave>", lambda event: self.dict_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        
        self.game_label = ctk.CTkLabel(self.a1_deutch_frame, text="Translation Game",
                                                                font=('Century Gothic', 15))
        self.game_label.place(relx = 0.15 , rely = 0.65)
        self.game_label.bind("<Button-1>", lambda event: self.master.open_translation_game_frame("a1_deutsch_frame"))
        self.game_label.bind("<Enter>", lambda event: self.game_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))# mainmenu_colour.frame_light))
        self.game_label.bind("<Leave>", lambda event: self.game_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        self.game_logo_label = ctk.CTkLabel(self.a1_deutch_frame, image=spielen_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.game_logo_label.place(relx=0.15, rely=0.35 )