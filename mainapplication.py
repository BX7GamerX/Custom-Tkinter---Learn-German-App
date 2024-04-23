import customtkinter as ctk
 
from welcomeframes import WelcomeFrame
#import tkinter
from mainmenuframes import MainMenuFrame
from translatorframe import TranslatorFrame
from translationgameframe import TranslationGameFrame,GameOverFrame
from a1deutschframe import A1DeutschFrame
from assetlib import Myapp
from assetlib import mainmenu_colour
from pythonframe import PythonFrame
from blenderframe import BlenderFrame
from unityframe import UnityFrame
from csharpframe import CsharpFrame
from javaframe import JavaFrame
from cplusframe import CplusFrame



ctk.set_default_color_theme(Myapp.default_theme) #default color of different widgets
ctk.set_appearance_mode(Myapp.apperance_mode) #default color scheme/ theme

frame_list = ["mainmenuframe","a1_deutsch_frame","translation_game_frame","game_over_frame","python_frame","blender_frame","unity_frame","cplus_frame","csharp_frame","java_frame","unity_frame","blender_frame","translator_frame"]



class MainApp(ctk.CTk):
		def __init__(self):
			super().__init__()
			self.title('BX7 Gamer')
			self.geometry('600x462')
			self.frames = {}
			self.main_frame =WelcomeFrame(master=self )#MainMenuFrame(self)#LoggedInFrame(self)  TranslationGameFrame(self)GameOverFrame(self)#
	
			self.main_frame.pack(expand=True, fill="both") # Expand to fill the main app window
		def change_geometry(self, new_geometry):
        # Change the window geometry
			self.geometry(new_geometry)	
		def change_title(self,new_title):
			self.title(new_title)
		def change_apperance_mode(self):
			if Myapp.apperance_mode == 'Dark':
				ctk.set_appearance_mode('Light')
				Myapp.apperance_mode = 'Light'
			elif Myapp.apperance_mode == 'Light':
				ctk.set_appearance_mode('Dark')
				Myapp.apperance_mode = 'Dark'
			else:
				ctk.set_appearance_mode('System')
		# self.frame_window=[MainMenuFrame(fg_color =mainmenu_colour.frame_darker),A1DeutschFrame()]
		# def get_destination_frame_index(frame_name):
		# 	if frame_name in frame_list:
		# 		return self.frame_window[frame_list.index(frame_name)]
		# 	return 0
		def open_main_menu_frame(self,origin_frame):
			if origin_frame == 'welcomeframe':
				self.main_frame.destroy()
				# Start logged in frame
				self.mainmenuframe = MainMenuFrame(self,fg_color =mainmenu_colour.frame_darker)
				self.frames["mainmenuframe"] = self.mainmenuframe
				self.mainmenuframe.pack(expand=True, fill="both") # Expand to fill the main app window
			else:
				self.frames[origin_frame].destroy()
				self.main_frame.destroy()
				# Start logged in frame
				self.mainmenuframe = MainMenuFrame(self,fg_color =mainmenu_colour.frame_darker)
				self.frames["mainmenuframe"] = self.mainmenuframe
				self.mainmenuframe.pack(expand=True, fill="both") # Expand to fill the main app window
				
		def open_translation_game_frame(self,origin_frame):
			
				self.main_frame.destroy()
				self.frames[origin_frame].destroy()
				self.translation_game_frame = TranslationGameFrame(self)
				self.frames["translation_game_frame"] = self.translation_game_frame
				self.translation_game_frame.pack(expand=True, fill="both") # Expand to fill the main app window
			
		def open_game_over_frame(self):
			self.main_frame.destroy()
			self.frames["translation_game_frame"].destroy()
			self.game_over_frame =GameOverFrame(self)
			self.frames["game_over_frame"] = self.game_over_frame
			self.game_over_frame.pack(expand=True, fill="both") # Expand to fill the main app window
		# def open_frame(self,origin_frame,destination_frame):
		# 	self.main_frame.destroy()
		# 	self.frames[origin_frame].destroy()
		# 	self.destinationframe = get_destination_frame_index(destination_frame)
		# 	self.frames[destination_frame] = self.destinationframe
		# 	self.destinationframe.pack(expand=True,fill='both')
		def open_a1_deutsch_frame(self,origin_frame):
			self.main_frame.destroy()
			self.frames[origin_frame].destroy()
			self.a1_deutsch_frame = A1DeutschFrame(self)
			self.frames["a1_deutsch_frame"] = self.a1_deutsch_frame
			self.a1_deutsch_frame.pack(expand=True,fill='both')
		def open_python_frame(self,origin_frame):
			self.main_frame.destroy()
			self.frames[origin_frame].destroy()
			self.python_frame = PythonFrame(self)
			self.frames["python_frame"] = self.python_frame
			self.python_frame.pack(expand=True,fill='both')
		def open_blender_frame(self,origin_frame):
			self.main_frame.destroy()
			self.frames[origin_frame].destroy()
			self.blender_frame = BlenderFrame(self)
			self.frames["blender_frame"] = self.blender_frame
			self.blender_frame.pack(expand=True,fill='both')
		def open_unity_frame(self,origin_frame):
			self.main_frame.destroy()
			self.frames[origin_frame].destroy()
			self.unity_frame = UnityFrame(self)
			self.frames["unity_frame"] = self.unity_frame
			self.unity_frame.pack(expand=True,fill='both')
		def open_cplus_frame(self,origin_frame):
			self.main_frame.destroy()
			self.frames[origin_frame].destroy()
			self.cplus_frame = CplusFrame(self)
			self.frames["cplus_frame"] = self.cplus_frame
			self.cplus_frame.pack(expand=True,fill='both')
		def open_csharp_frame(self,origin_frame):
			self.main_frame.destroy()
			self.frames[origin_frame].destroy()
			self.csharp_frame = CsharpFrame(self)
			self.frames["csharp_frame"] = self.csharp_frame
			self.csharp_frame.pack(expand=True,fill='both')
		def open_java_frame(self,origin_frame):
			self.main_frame.destroy()
			self.frames[origin_frame].destroy()
			self.java_frame = JavaFrame(self)
			self.frames["java_frame"] = self.java_frame
			self.java_frame.pack(expand=True,fill='both')
		def open_translator_frame(self):
        # Destroy the Main frame and open the LoggedIn frame
			self.main_frame.destroy()
			self.frames["mainmenuframe"].destroy()
			self.frames["a1_deutsch_frame"].destroy()
			# Start logged in frame
			self.translator_frame = TranslatorFrame(self)
			self.frames["translator_frame"] = self.translator_frame
			self.translator_frame.pack(expand=True, fill="both") # Expand to fill the main app window
