import customtkinter as ctk
import tkinter
from PIL import Image
from assetlib import learn_deutsch_pic,coding_pic,game_dev_pic,mainmenu_colour
from assetlib import python_pic,java_pic,csharp_pic,cplus_pic
from assetlib import unity_pic, blender_pic


Learn_Deutsch_logo =learn_deutsch_pic
Coding_logo = coding_pic
Game_dev = game_dev_pic



# class CodingFrame(ctk.CTkFrame):
#     def __int__(self,master,**kwargs):
#         super(self).__init__(master,**kwargs)
        
#         self.setup_coding_frame()
        
#         def setup_coding_frame(self):
                    
#             self.coding_label = ctk.CTkLabel(self, text="Coding",
#                                                                     font=('Century Gothic', 25))
#             self.coding_label.place(relx = 0.35 , rely = 0.05)
        
#             self.Coding_logo_label = ctk.CTkLabel(self, image=Coding_logo, text="",
# 										                     font=ctk.CTkFont(size=20, weight="bold"))
#             self.Coding_logo_label.place(relx=0.35, y=50 )
        
#         self.A1_label = ctk.CTkLabel(self.Learn_Deutch_frame, text="A1 - Deutsch",
#                                                                 font=('Century Gothic', 15))
#         self.A1_label.place(relx = 0.35 , rely = 0.45)
#         self.A1_label.bind("<Button-1>", lambda event: self.master.open_a1_deutsch_frame())
#         self.A1_label.bind("<Enter>", lambda event: self.A1_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))# mainmenu_colour.frame_light))
#         self.A1_label.bind("<Leave>", lambda event: self.A1_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.setup_main_menu_frame()
        
       


    def setup_main_menu_frame(self):
        self.master.change_geometry("1280x720")
        
        self.Learn_Deutch_frame = ctk.CTkFrame(self, width=320, height=380,fg_color=mainmenu_colour.frame_dark,corner_radius=25)
        self.Learn_Deutch_frame.bind("<Enter>", lambda event: self.Learn_Deutch_frame.configure(fg_color = mainmenu_colour.frame_light))
        self.Learn_Deutch_frame.bind("<Leave>", lambda event: self.Learn_Deutch_frame.configure(fg_color = mainmenu_colour.frame_dark))
        self.Learn_Deutch_frame.place(relx=0.1,rely=0.25)#relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.Deutsch_label = ctk.CTkLabel(self.Learn_Deutch_frame, text="Learn Deutsch",
                                                                font=('Century Gothic', 25))
        self.Deutsch_label.place(x = 75 , rely = 0.05)
        
        self.Learn_Deutsch_logo_label = ctk.CTkLabel(self.Learn_Deutch_frame, image=Learn_Deutsch_logo, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.Learn_Deutsch_logo_label.place(relx=0.18, y=60 )
        
        self.A1_label = ctk.CTkLabel(self.Learn_Deutch_frame, text="A1 - Deutsch",
                                                                font=('Century Gothic', 15))
        self.A1_label.place(relx = 0.35 , rely = 0.45)
        self.A1_label.bind("<Button-1>", lambda event: self.master.open_a1_deutsch_frame('mainmenuframe'))
        self.A1_label.bind("<Enter>", lambda event: self.A1_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))# mainmenu_colour.frame_light))
        self.A1_label.bind("<Leave>", lambda event: self.A1_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))#mainmenu_colour.frame_dark))
        
        self.A2_label = ctk.CTkLabel(self.Learn_Deutch_frame, text="A2 - Deutsch",
                                                                font=('Century Gothic', 15))
        self.A2_label.place(relx = 0.35 , rely = 0.55)
        self.A2_label.bind("<Button-1>", lambda event: self.master.open_forgot_password_frame())
        self.A2_label.bind("<Enter>", lambda event: self.A2_label.configure(cursor="hand2",text_color="green",fg_color = 'transparent'))#mainmenu_colour.frame_light))
        self.A2_label.bind("<Leave>", lambda event: self.A2_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))#mainmenu_colour.frame_dark))
        
        self.B1_label = ctk.CTkLabel(self.Learn_Deutch_frame, text="B1 - Deutsch",
                                                                font=('Century Gothic', 15))
        self.B1_label.place(relx = 0.35 , rely = 0.65)
        self.B1_label.bind("<Button-1>", lambda event: self.master.open_forgot_password_frame())
        self.B1_label.bind("<Enter>", lambda event: self.B1_label.configure(cursor="hand2",text_color="green",fg_color = 'transparent'))#mainmenu_colour.frame_light))
        self.B1_label.bind("<Leave>", lambda event: self.B1_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))#mainmenu_colour.frame_dark))
        
        self.B2_label = ctk.CTkLabel(self.Learn_Deutch_frame, text="B2 - Deutsch",
                                                                font=('Century Gothic', 15))
        self.B2_label.place(relx = 0.35 , rely = 0.75)
        self.B2_label.bind("<Button-1>", lambda event: self.master.open_forgot_password_frame())
        self.B2_label.bind("<Enter>", lambda event: self.B2_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))# mainmenu_colour.frame_light))
        self.B2_label.bind("<Leave>", lambda event: self.B2_label.configure(cursor="arrow",text_color="white",fg_color ='transparent'))# mainmenu_colour.frame_dark))
        
        self.Cant_decide_label = ctk.CTkLabel(self.Learn_Deutch_frame, text="Can't Decide?",
                                                                font=('Century Gothic', 10))
        self.Cant_decide_label.place(relx = 0.38 , rely = 0.85)
        self.Cant_decide_label.bind("<Button-1>", lambda event: self.master.open_translation_game_frame("mainmenuframe"))
        self.Cant_decide_label.bind("<Enter>", lambda event: self.Cant_decide_label.configure(cursor="hand2",text_color="blue",fg_color ='transparent'))# mainmenu_colour.frame_light))
        self.Cant_decide_label.bind("<Leave>", lambda event: self.Cant_decide_label.configure(cursor="arrow",text_color="white",fg_color ='transparent'))# mainmenu_colour.frame_dark))




        # self.coding_frame = CodingFrame(self,width=320, height=380,corner_radius=25)
        # self.coding_frame.place(relx=0.4,rely=0.25)
        self.coding_frame = ctk.CTkFrame(self, width=320, height=380,fg_color=mainmenu_colour.frame_dark,corner_radius=25)  
        self.coding_frame.bind("<Enter>", lambda event: self.coding_frame.configure(fg_color = mainmenu_colour.frame_light))
        self.coding_frame.bind("<Leave>", lambda event: self.coding_frame.configure(fg_color = mainmenu_colour.frame_dark))
        self.coding_frame.place(relx=0.4,rely=0.25)#relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.coding_label = ctk.CTkLabel(self.coding_frame, text="Coding",
                                                                font=('Century Gothic', 25))
        self.coding_label.place(relx = 0.35 , rely = 0.05)
        
        self.Coding_logo_label = ctk.CTkLabel(self.coding_frame, image=Coding_logo, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.Coding_logo_label.place(relx=0.35, y=50 )
        
        self.python_label = ctk.CTkLabel(self.coding_frame, text="Python",
                                                                font=('Century Gothic', 15))
        self.python_label.place(relx = 0.23 , rely = 0.60)
        self.python_label.bind("<Button-1>", lambda event: self.master.open_python_frame('mainmenuframe'))
        self.python_label.bind("<Enter>", lambda event: self.python_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))
        self.python_label.bind("<Leave>", lambda event: self.python_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        self.python_logo_label = ctk.CTkLabel(self.coding_frame, image=python_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.python_logo_label.place(relx = 0.23 , rely = 0.45 )
        
        self.cplus_label = ctk.CTkLabel(self.coding_frame, text="C ++",
                                                                font=('Century Gothic', 15))
        self.cplus_label.place(relx = 0.65 , rely = 0.60)
        self.cplus_label.bind("<Button-1>", lambda event: self.master.open_cplus_frame('mainmenuframe'))
        self.cplus_label.bind("<Enter>", lambda event: self.cplus_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))
        self.cplus_label.bind("<Leave>", lambda event: self.cplus_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        self.cplus_logo_label = ctk.CTkLabel(self.coding_frame, image=cplus_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.cplus_logo_label.place(relx = 0.65 , rely = 0.45 )
        
        self.java_label = ctk.CTkLabel(self.coding_frame, text="Java",
                                                                font=('Century Gothic', 15))
        self.java_label.place(relx = 0.23 , rely = 0.85)
        self.java_label.bind("<Button-1>", lambda event: self.master.open_java_frame('mainmenuframe'))
        self.java_label.bind("<Enter>", lambda event: self.java_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))
        self.java_label.bind("<Leave>", lambda event: self.java_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        self.java_logo_label = ctk.CTkLabel(self.coding_frame, image=java_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.java_logo_label.place(relx = 0.23 , rely = 0.70)
        
        self.csharp_label = ctk.CTkLabel(self.coding_frame, text="C#",
                                                                font=('Century Gothic', 15))
        self.csharp_label.place(relx = 0.65 , rely = 0.85)
        self.csharp_label.bind("<Button-1>", lambda event: self.master.open_csharp_frame('mainmenuframe'))
        self.csharp_label.bind("<Enter>", lambda event: self.csharp_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))
        self.csharp_label.bind("<Leave>", lambda event: self.csharp_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        self.csharp_logo_label = ctk.CTkLabel(self.coding_frame, image=csharp_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.csharp_logo_label.place(relx=0.68, rely=0.70 )
        
        
        
        
        



        self.Game_Dev_frame = ctk.CTkFrame(self, width=320, height=380,fg_color=mainmenu_colour.frame_dark,corner_radius=25)  
        self.Game_Dev_frame.bind("<Enter>", lambda event: self.Game_Dev_frame.configure(fg_color = mainmenu_colour.frame_light))
        self.Game_Dev_frame.bind("<Leave>", lambda event: self.Game_Dev_frame.configure(fg_color = mainmenu_colour.frame_dark))
        self.Game_Dev_frame.place(relx=0.7,rely=0.25)#relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.Game_Dev_label = ctk.CTkLabel(self.Game_Dev_frame, text="Game Dev",
                                                                font=('Century Gothic', 25))
        self.Game_Dev_label.place(relx = 0.3 , rely = 0.05)
        self.Game_Dev_logo_label = ctk.CTkLabel(self.Game_Dev_frame, image=game_dev_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.Game_Dev_logo_label.place(relx=0.35, y=60 )
        
        self.unity_label = ctk.CTkLabel(self.Game_Dev_frame, text="Unity",
                                                                font=('Century Gothic', 15))
        self.unity_label.place(relx = 0.22 , rely = 0.85)
        self.unity_label.bind("<Button-1>", lambda event: self.master.open_unity_frame('mainmenuframe'))
        self.unity_label.bind("<Enter>", lambda event: self.unity_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))
        self.unity_label.bind("<Leave>", lambda event: self.unity_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        self.unity_logo_label = ctk.CTkLabel(self.Game_Dev_frame, image=unity_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.unity_logo_label.place(relx = 0.1 , rely = 0.50)
        
        self.blender_label = ctk.CTkLabel(self.Game_Dev_frame, text="Blender",
                                                                font=('Century Gothic', 15))
        self.blender_label.place(relx = 0.63 , rely = 0.85)
        self.blender_label.bind("<Button-1>", lambda event: self.master.open_blender_frame('mainmenuframe'))
        self.blender_label.bind("<Enter>", lambda event: self.blender_label.configure(cursor="hand2",text_color="green",fg_color ='transparent'))
        self.blender_label.bind("<Leave>", lambda event: self.blender_label.configure(cursor="arrow",text_color="white",fg_color = 'transparent'))
        self.blender_logo_label = ctk.CTkLabel(self.Game_Dev_frame, image=blender_pic, text="",
										                 font=ctk.CTkFont(size=20, weight="bold"))
        self.blender_logo_label.place(relx = 0.5 , rely = 0.50)
        pass
    

    

