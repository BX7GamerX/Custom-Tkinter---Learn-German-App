import customtkinter as ctk
from word_library import translate_one as translate

class TranslatorFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.setup_translator_frame()

    def setup_translator_frame(self):
        self.master.change_geometry("400x250")
        self.label = ctk.CTkLabel(self, text="English or German word:")
        self.title_label = ctk.CTkLabel(self, text="Translate Word" ,anchor='w',font=("Old English Text",20,"bold"))
        self.back_main_menu = ctk.CTkLabel(self,text='<--',font=("Old English Text",20,"bold"))
        self.translate_entry = ctk.CTkEntry(self, placeholder_text='word to translate')
        self.translate_button = ctk.CTkButton(self,text="Translate", command=self.Translate , hover_color= 'green')
        self.translation_label = ctk.CTkLabel(self, text="Translation will appear here :", font=("Arial", 15, "italic"))
        
        self.title_label.place(relx=0.3, rely=0.1) 
        self.label.place(relx=0.05, rely=0.3) 
        self.back_main_menu.place(relx=0.2,rely=0.1)
        self.translate_entry.place(relx=0.5, rely=0.3) 
        self.translate_button.place(relx=0.3, rely=0.5) 
        self.translation_label.place(relx=0.25, rely=0.7) 
        self.back_main_menu.bind("<Button-1>", lambda event: self.master.open_main_menu_frame("translator_frame"))
        self.back_main_menu.bind("<Enter>", lambda event: self.back_main_menu.configure(cursor="hand2",
                                                                                        text_color="green",text='Main Menu',font=("Old English Text",10,"bold")))
        self.back_main_menu.bind("<Leave>", lambda event: self.back_main_menu.configure(cursor="arrow",
                                                                                        text_color="white",text='<--',font=("Old English Text",20,"bold")))

    
    def Translate(self):
        word_in = self.translate_entry.get().lower()
        translation = translate(word_in)
        if word_in != "": 
            if translation != "not found":
                   self.translation_label.configure(text=f"Translation : {translation}")
            else:
                self.translation_label.configure(text="Word not found in dictionary.")
        else:
            self.translation_label.configure(text="Invalid Entry Lad")
