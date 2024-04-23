#from doctest import master
import customtkinter as ctk # for the entire GUI and it'sfunctionalities 
from mainframes import WelcomeFrame
import tkinter
from transitionalframe import LoggedInFrame
from translatorframe import TranslatorFrame
from translationgameframe import TranslationGameFrame

ctk.set_default_color_theme('dark-blue') #default color of different widgets
ctk.set_appearance_mode('System') #default color scheme/ theme


class MainFrame(ctk.CTk):
		def __init__(self):
			super().__init__()
			self.title('BX7 Gamer')
			self.geometry('600x462')
			self.frames = {}
			self.main_frame =WelcomeFrame(master=self)#LoggedInFrame(self)  TranslationGameFrame(self)
	
			self.main_frame.pack(expand=True, fill="both") # Expand to fill the main app window
		def change_geometry(self, new_geometry):
        # Change the window geometry
			self.geometry(new_geometry)	

		def open_loggedin_frame(self):
        # Destroy the Main frame and open the LoggedIn frame
			self.main_frame.destroy()
			# Start logged in frame
			self.loggedin_frame = LoggedInFrame(self)
			self.frames["loggedin_frame"] = self.loggedin_frame
			self.loggedin_frame.pack(expand=True, fill="both") # Expand to fill the main app window
			
		def open_translation_game_frame(self):
			 # Destroy the Main frame and open the LoggedIn frame
			self.main_frame.destroy()
			self.frames["loggedin_frame"].destroy()
			# Start logged in frame
			self.translation_game_frame = TranslationGameFrame(self)
			self.frames["translation_game_frame"] = self.translation_game_frame
			self.translation_game_frame.pack(expand=True, fill="both") # Expand to fill the main app window
			
		def open_translation_game_frame_two(self):
			 # Destroy the Main frame and open the LoggedIn frame
			self.main_frame.destroy()
			
			# Start logged in frame
			self.translation_game_frame = TranslationGameFrame(self)
			self.frames["translation_game_frame"] = self.translation_game_frame
			self.translation_game_frame.pack(expand=True, fill="both") # Expand to fill the main app window
			
			
			
		def open_translator_frame(self):
        # Destroy the Main frame and open the LoggedIn frame
			self.main_frame.destroy()
			self.frames["loggedin_frame"].destroy()
			# Start logged in frame
			self.translator_frame = TranslatorFrame(self)
			self.frames["translator_frame"] = self.translator_frame
			self.translator_frame.pack(expand=True, fill="both") # Expand to fill the main app window
if __name__=="__main__":
	app = MainFrame()
	app.mainloop()
	



