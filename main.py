from ctypes import alignment
from gettext import translation
from tkinter import font
from turtle import screensize, width
import customtkinter as ctk 
from PIL import Image 
from word_library import Random_word_gen,translate_one as translate 


#internal logo
app_logo = ctk.CTkImage (light_image=Image.open("images/logo.jpg"), size=(150, 150  ))

#default properties
ctk.set_default_color_theme('dark-blue')
ctk.set_appearance_mode('System')

#exit window
class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("360x130")
        self.title("Learn German")
        self.label = ctk.CTkLabel(self, text="Do you want to exit?")
        self.label.pack(padx=20, pady=20)
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.yes_button = ctk.CTkButton(self, text="Yes", command=self.exit_f)
        self.yes_button.grid(row=1, column=0, padx=20, pady=10)

        self.no_button = ctk.CTkButton(self, text="No", command=self.destroy)
        self.no_button.grid(row=1, column=1, padx=20, pady=10)

    def exit_f(self):
        self.destroy()
        exit()

#function to f=set appearance in-app
def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)

cast_word_type_game = 'nouns'
def set_word_type(word_type: str):
        cast_word_type_game = word_type
        return cast_word_type_game

#app class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #app properties
        self.title('Learn Deutsch')
        self.screen_width = '1280'
        self.screen_height = '720'
        self.screen_width_int = int(self.screen_width)
        self.screen_height_int =int(self.screen_height)
        self.geometry(f"{self.screen_width} x {self.screen_height}")
        self.resizable(width=False, height=False)
        self.word_type_game = cast_word_type_game
        self.randy_word = Random_word_gen(self.word_type_game)
        #BAR
        #left bar
        self.leftbar_frame = ctk.CTkFrame(master=self, width= int(self.screen_width_int/5.7),height= int(self.screen_height_int/1), corner_radius=5)
        self.leftbar_frame.grid(row= 0, column=0, rowspan= 4, sticky= 'new')
        self.leftbar_frame.grid_rowconfigure(4, weight=1)
        #mainbar
        self.mainbar_frame = ctk.CTkFrame(self, width= int(self.screen_width_int/5.7), corner_radius=5)
        self.mainbar_frame.grid(row= 0, column=1, rowspan= 4, sticky= 'new')
        self.mainbar_frame.grid_rowconfigure(4, weight=1)
        #main bar A
        self.mainbar_frame_A = ctk.CTkFrame(self.mainbar_frame, width= 140, corner_radius=5)
        self.mainbar_frame_A.grid(row= 0, column=0, sticky= 'new')
        self.mainbar_frame_A.grid_rowconfigure(4, weight=1)

        #main bar B
        self.mainbar_frame_B = ctk.CTkFrame(self.mainbar_frame, width= 140, corner_radius=5 )
        self.mainbar_frame_B.grid(row= 4, column=0, rowspan= 4,pady=10 ,sticky= 'new')
        self.mainbar_frame_B.grid_rowconfigure(4, weight=1)

        #right bar
        self.rightbar_frame = ctk.CTkFrame(self, width= 140, corner_radius=5)
        self.rightbar_frame.grid(row= 0, column=2, rowspan= 4, sticky= 'new')
        self.rightbar_frame.grid_rowconfigure(4, weight=1)
        
        #leftbar butrrons
        #sidebar button 1 -clear image
        self.leftbar_button_1 = ctk.CTkButton(self.leftbar_frame, text="Clear Image")#, command=self.set_before_image)
        self.leftbar_button_1.grid(row=2, column=0, padx=20, pady=10)

        #sidebar button 2 - appearance mode
        self.appearance_mode_label = ctk.CTkLabel(self.leftbar_frame, text="Apperance mode:", anchor="w")
        self.appearance_mode_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_options = ctk.CTkOptionMenu(self.leftbar_frame,
                                                                   values=["Light", "Dark", "System"],
                                                                   command=change_appearance_mode_event)
        self.appearance_mode_options.grid(row=5, column=0, padx=20, pady=(10, 10))

        #sidebar button 3 - exit button 
        self.exit_button = ctk.CTkButton(self.leftbar_frame, text="Exit", hover_color="Red",
                                                   command=self.exit_app)
        self.exit_button.grid(row=6, column=0, padx=20, pady=10)

        #sidebar button 4 - search
        self.entry = ctk.CTkEntry(self.leftbar_frame, placeholder_text="Search for filter")
        self.entry.grid(row=7, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self.leftbar_frame, text="Search", fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"))#, command=self.send_message)
        self.main_button_1.grid(row=8, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # set currently visible tab

        #label
        #side logo label
        self.logo = ctk.CTkLabel(self.leftbar_frame, image=app_logo, text="",
                                           font=ctk.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_label = ctk.CTkLabel(self.leftbar_frame, text="BXG_Him",
                                                 font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20)

        #MAINBAR Widgets
        #widget_on :label name,subheading,entry,button,result
        self.label = ctk.CTkLabel(self.mainbar_frame_A, text="English or German word:")
        self.title_label = ctk.CTkLabel(self.mainbar_frame_A, text="Translate Word" ,anchor='w',font=("Old English Text",20,"bold"))
        self.translate_entry = ctk.CTkEntry(self.mainbar_frame_A , placeholder_text='word to translate')
        self.translate_button = ctk.CTkButton(self.mainbar_frame_A, text="Translate", command=self.Translate , hover_color= 'green')
        self.translation_label = ctk.CTkLabel(self.mainbar_frame_A, text="Translation will appear here :", font=("Arial", 15, "italic"))

        #widget_one layout
        self.title_label.grid(row=0, columnspan=2, padx=10, pady=10)
        self.label.grid(row=1, column=0, padx=10, pady=10)
        self.translate_entry.grid(row=1, column=1, padx=5, pady=10)
        self.translate_button.grid(row=2, columnspan=2, padx=10, pady=10)
        self.translation_label.grid(row=3, columnspan=2, padx=10, pady=10)

        #section B
        #section title
        self.section_B_function = ctk.CTkLabel(self.mainbar_frame_B, text="Translation Game" , anchor='center',font=("Old English Text",20,"bold"))
        self.section_B_function.grid(row=3, columnspan=2, padx=0, pady=10)
        #wordtype widget
        self.word_type_label = ctk.CTkLabel(self.mainbar_frame_B, text="Word Type:", anchor="center")
        self.word_type_label.grid(row=4, columnspan=2, padx=20, pady=(3, 3))
        self.word_type_options = ctk.CTkOptionMenu(self.mainbar_frame_B,
                                                                   values=["nouns", "adjectives", "verbs","adverbs"],
                                                                   command=set_word_type)
        self.word_type_options.grid(row=5, column=0,columnspan=2, padx=10, pady=10)  
        #Question label -what is the english translation of:
        self.Enquiry_Label =ctk.CTkLabel(self.mainbar_frame_B, text= "What is the English Translation of :" ,anchor="center" , font=("Arial",13,"bold"))
        self.Enquiry_Label.grid(row=6,column=0, columnspan=1, padx=20, pady=(3, 3))
        #Random word label -random word
        self.word_entry_name =ctk.CTkLabel(self.mainbar_frame_B, text= self.randy_word,anchor="center",font=("Arial", 13, "italic"))
        self.word_entry_name.grid(row=7, column=0,columnspan=2, padx=10, pady=10)
        #user trial entry - enter trial
        self.user_trial_entry =ctk.CTkEntry(self.mainbar_frame_B , placeholder_text='Enter Trial')
        self.user_trial_entry.grid(row=8, column=0,columnspan=2, padx=10, pady=10)
        #check user trial button -check
        self.check_user_trial_button = ctk.CTkButton(self.mainbar_frame_B, text="Check", command=self.trial_check)
        self.check_user_trial_button.grid(row=9, column=0,columnspan=2, padx=10, pady=10)
        #confirm if correct
        self.confirm_entry_label =ctk.CTkLabel(self.mainbar_frame_B, text= "[Results will appear here]" ,anchor="w",font=("Arial", 13, "italic"))
        self.confirm_entry_label.grid(row=10, column=0,columnspan=2, padx=10, pady=10)

        #set defaults:
        self.toplevel_window = None
        self.user_score = 0
        self.user_trials_left = 10
 
    
    
    #fucntion to check user's trial against the database
    def trial_check(self):
        count = 0
        self.word_entry_name.configure(text=self.randy_word)
        count += 1
        translation = translate(self.randy_word)
        word_in = self.user_trial_entry.get().lower()
        count += 1
        if (word_in == translation ) :
            self.confirm_entry_label.configure(text=f"Correct! Score: {self.user_score}" )
            self.randy_word = Random_word_gen(self.word_type_game)
            self.word_entry_name.configure(text=self.randy_word)
            self.user_score +=1
        elif (word_in != translation )  :
            self.confirm_entry_label.configure(text=f"Wrong! answer was :'{translation}' Trials left : {self.user_trials_left}")
            self.randy_word = Random_word_gen(self.word_type_game)
            self.word_entry_name.configure(text=self.randy_word)
            self.user_trials_left -= 1
    #function to translate word given in section _A
    def Translate(self):
        word_in = self.translate_entry.get().lower()
        
        if not word_in:
            self.translation_label.configure(text="Please enter a word to translate.")
            return
        
        try:
            translation = translate(word_in)
            if translation != "not found":
                self.translation_label.configure(text=f"Translation : {translation}")
                
            else:
                self.translation_label.configure(text="Word not found in dictionary.")
        except Exception as int :
            self.translation_label.configure(text=f"An error occurred: {str(int)}")

        
        
    def exit_app(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()





if __name__=="__main__":
    app = App()
    app.iconbitmap('logo.ico')
    app.update()
    app.mainloop()