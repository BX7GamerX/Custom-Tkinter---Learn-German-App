import customtkinter as ctk
from assetlib import game_dev_pic


class LearnDeutschFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super(self.__init__)
        self.setup_learn_deutsch_frame()

    def setup_learn_deutsch_frame(self):
        self.Deutsch_label = ctk.CTkLabel(self, text="Learn Deutsch",
                                           font=('Century Gothic', 25))
        self.Deutsch_label.place(x=75, rely=0.05)

        self.Learn_Deutsch_logo_label = ctk.CTkLabel(self, image=Learn_Deutsch_logo, text="",
                                                     font=ctk.CTkFont(size=20, weight="bold"))
        self.Learn_Deutsch_logo_label.place(relx=0.35, y=60)

        # Add labels for A1, A2, B1, B2 levels with functionality here
        # ...

        self.Cant_decide_label = ctk.CTkLabel(self, text="Can't Decide?",
                                               font=('Century Gothic', 10))
        self.Cant_decide_label.place(relx=0.38, rely=0.85)
        # ... bind button functionality here ...


class CodingFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super(self.__init__, master, **kwargs)
        self.setup_coding_frame()

    def setup_coding_frame(self):
        self.coding_label = ctk.CTkLabel(self, text="Coding",
                                         font=('Century Gothic', 25))
        self.coding_label.place(relx=0.35, rely=0.05)

        self.Coding_logo_label = ctk.CTkLabel(self, image=Coding_logo, text="",
                                             font=ctk.CTkFont(size=20, weight="bold"))
        self.Coding_logo_label.place(relx=0.35, y=50)

        # Add additional labels or functionalities for CodingFrame here
        # ...


class GameDevFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super(self.__init__, master, **kwargs)
        self.setup_game_dev_frame()

    def setup_game_dev_frame(self):
        self.Game_Dev_label = ctk.CTkLabel(self, text="Game Dev",
                                           font=('Century Gothic', 25))
        self.Game_Dev_label.place(relx=0.3, rely=0.05)

        self.Game_Dev_logo_label = ctk.CTkLabel(self, image=game_dev_pic, text="",
                                                font=ctk.CTkFont(size=20, weight="bold"))
        self.Game_Dev_logo_label.place(relx=0.35, y=60)

        # Add additional labels or functionalities for GameDevFrame here
        # ...


class MainMenuFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.setup_main_menu_frame()

    def setup_main_menu_frame(self):
        self.geometry('600x462')
       

        self.Learn_Deutch_frame = LearnDeutschFrame(self, width=320, height=380, corner_radius=25)
        self.Learn_Deutch_frame.place(relx=0.1, rely=0.25)

        self.coding_frame = CodingFrame(self, width=320, height=380, corner_radius=25)
        self.coding_frame.place(relx=0.4, rely=0.25)

        self.Game_Dev_frame = GameDevFrame(self, width=320, height=380)


if __name__=="__main__":
	app = MainMenuFrame()
	app.iconbitmap('logo.ico')
	app.update()
	app.mainloop()