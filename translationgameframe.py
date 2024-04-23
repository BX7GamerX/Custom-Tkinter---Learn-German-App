import customtkinter as ctk
from word_library import Random_word_gen, translate_one as translate

class GameConstants():
    def __init__(self,Word_type,Score,Trials_left):
       self.word_type = Word_type
       self.score =Score
       self.trials_left = Trials_left
    
       
game_properties = GameConstants('nouns',0,20)
game_properties.word_type ='nouns'
	

class TranslationGameFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.setup_translation_game_frame()

    def setup_translation_game_frame(self):
        self.master.change_geometry("400x600")
 
        self.randy_word = Random_word_gen(game_properties.word_type)
        
        self.section_B_function = ctk.CTkLabel(self, text="Translation Game" ,
                                               anchor='center',font=("Old English Text",20,"bold"))
        self.section_B_function.place(relx=0.3, rely=0.05) 
        self.word_type_label = ctk.CTkLabel(self, text="Word Type:", anchor="center")
        self.word_type_label.place(relx=0.4, rely=0.1) 
        self.word_type_options = ctk.CTkOptionMenu(self,values=["nouns", "adjectives", "verbs","adverbs"],
																   command=self.set_word_type)
        self.word_type_options.place(relx=0.3, rely=0.15) 
        self.Enquiry_Label =ctk.CTkLabel(self, text= "What is the English Translation of :" ,anchor="center" , font=("Arial",13,"bold"))
        self.Enquiry_Label.place(relx=0.2, rely=0.25) 
        self.word_entry_name =ctk.CTkLabel(self, text= self.randy_word,anchor="center",font=("Arial", 13, "italic"))
        self.word_entry_name.place(relx=0.4, rely=0.35) 
        self.user_trial_entry =ctk.CTkEntry(self, placeholder_text='Enter Trial')
        self.user_trial_entry.place(relx=0.3, rely=0.45) 
        self.check_user_trial_button = ctk.CTkButton(self, text="Check", command=self.trial_check, hover_color='green')
        self.check_user_trial_button.place(relx=0.3, rely=0.55) 
        
        self.confirm_entry_label =ctk.CTkLabel(self, text= "[Results will appear here]" ,anchor="w",font=("Arial", 13, "italic"))
        self.confirm_entry_label.place(relx=0.3, rely=0.65)
        
        self.score_label =ctk.CTkLabel(self, text= f"Score :{game_properties.score}    " ,anchor="w",font=("Arial", 17, "bold"))
        self.score_label.place(relx=0.35, rely=0.75) 
        self.score_label.bind("<Enter>", lambda event: self.score_label.configure(text_color="green"))
        self.score_label.bind("<Leave>", lambda event: self.score_label.configure(text_color="white"))
        
        self.trials_left_label =ctk.CTkLabel(self, text= f" Trials Left :{game_properties.trials_left}" ,anchor="w",font=("Arial", 17, "bold"),text_color='white')
        self.trials_left_label.place(relx=0.32, rely=0.85) 
        self.user_score = 0
        self.user_trials_left = 10
        
    def set_word_type(self,word_type):
        game_properties.word_type = word_type
        self.randy_word = Random_word_gen(game_properties.word_type)
        self.word_entry_name.configure(text=self.randy_word)
          
    def trial_check(self):
        
        self.word_entry_name.configure(text=self.randy_word)
        
        translation = translate(self.randy_word)
        word_in = self.user_trial_entry.get().lower()
        if game_properties.trials_left  >0:

             if game_properties.trials_left <= 5:
                self.trials_left_label.configure(text_color='red')
            
             else:
                   self.trials_left_label.configure(text_color ='white')
             if (word_in == translation ) :
                self.confirm_entry_label.configure(text=f"Correct! " )
                self.randy_word = Random_word_gen(game_properties.word_type)
                self.word_entry_name.configure(text=self.randy_word)
                self.score_label.configure(text= f"Score :{game_properties.score}  ")
                self.trials_left_label.configure(text=f" Trials Left :{game_properties.trials_left}")
            
                game_properties.score += 3
             elif (word_in != translation )  :
                self.confirm_entry_label.configure(text=f"Wrong! answer was :'{translation}'  ")
                self.randy_word = Random_word_gen(game_properties.word_type)
                self.word_entry_name.configure(text=self.randy_word)
                self.score_label.configure(text= f"Score :{game_properties.score}  ")
                self.trials_left_label.configure(text= f" Trials Left :{game_properties.trials_left}")
            
                game_properties.trials_left -=1
        else:
            self.master.open_game_over_frame()
                        
class GameOverFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.setup_game_over_frame()

    def setup_game_over_frame(self):  
       self.master.change_geometry("400x600")
       self.game_over_Label = ctk.CTkLabel(self,text= " GAME OVER",font=("Old English Text",35,"bold"),text_color= '#0890ff')
       self.game_over_Label.place(relx=0.2, rely=0.25)
       self.score_label = ctk.CTkLabel(self,text=f" Score:{game_properties.score}",font=("Old English Text",30,"bold"),text_color= '#00ff76')
       self.score_label.place(relx=0.3, rely=0.35) 
       self.out_of_trials_label = ctk.CTkLabel (self,text= "Out of Trials",anchor="w",font=("Arial", 17, "bold"),text_color='white')
       self.out_of_trials_label.place(relx=0.32, rely=0.85) 
       self.restart_button =  ctk.CTkButton(self, text="Restart",  hover_color='green',command=self.restart_game)
       self.restart_button.place(relx=0.3, rely=0.45) 
       self.main_menu_button = ctk.CTkButton(self,text= "Main menu",command = self.back_to_main_menu)
       self.main_menu_button.place(relx=0.3, rely=0.55) 
       game_properties.score = 0
       game_properties.trials_left =20
       
    def restart_game(self):
       self.master.open_translation_game_frame("game_over_frame")
       
    def back_to_main_menu(self):
         self.master.open_main_menu_frame("game_over_frame")
       
           
            
            
           
            
