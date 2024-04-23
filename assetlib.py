from PIL import Image
import customtkinter as ctk
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)

class image_class :
    def __init__(self,Location_dark,Location_light):
        
        self.location_dark = Location_dark
        self.location_light = Location_light
        
course_material_logo =  image_class(resource_path("images\\Deutsch\\A1\\course_materials_dark.png"),resource_path("images\\Deutsch\\A1\\course_materials_dark.png"))
course_guide_logo =  image_class(resource_path("images\\Deutsch\\A1\\course_guide_dark.png"),resource_path("images\\Deutsch\\A1\\course_guide_dark.png"))
revision_material_logo =  image_class(resource_path("images\\Deutsch\\A1\\course_materials_dark.png"),resource_path("images\\Deutsch\\A1\\course_materials_dark.png"))
welcome_screen_logo = image_class(resource_path("images\\logo.jpg"),resource_path("images\\logo.png"))
learn_duetsch_logo = image_class(resource_path("images\\Deutsch\\logp.jpg"),resource_path("images\\Deutsch\\logp.jpg"))
coding_logo = image_class(resource_path("images\\Coding\\coding_dark.png"),resource_path("images\\Coding\\coding_light.png"))
game_dev_logo = image_class(resource_path("images\\GameDev\\game_dev_dark.jpg"),resource_path("images\\GameDev\\game_dev_light.png"))
cplus_logo = image_class(resource_path("images\\Coding\\cplus\\cplus.png"),resource_path("images\\Coding/cplus\\cplus.png"))
csharp_logo = image_class(resource_path("images\\Coding\\csharp\\csharp.png"),resource_path("images\\Coding\\csharp\\csharp.png"))
java_logo = image_class(resource_path("images\\Coding/java\\java.png"),resource_path("images\\Coding\\java\\java.png"))
python_logo = image_class(resource_path("images\\Coding\\python\\python.png"),resource_path("images\\Coding\\python\\python.png"))
spielen_logo = image_class(resource_path("images\\Deutsch\\A1\\spielen.jpg"),resource_path("images\\Deutsch\\A1\\spielen.jpg"))
blender_logo = image_class(resource_path("images\\GameDev\\blender\\blender.png"),resource_path("images\\GameDev\\blender\\blender.png"))
unity_logo = image_class(resource_path("images\\GameDev\\unity\\unity.png"),resource_path("images\\GameDev\\unity\\unity.png"))
blender_pic = ctk.CTkImage(dark_image=Image.open(blender_logo.location_dark),light_image=Image.open(blender_logo.location_light),size=(125,125))
unity_pic = ctk.CTkImage(dark_image=Image.open(unity_logo.location_dark),light_image=Image.open(unity_logo.location_light),size=(125,125))

spielen_pic = ctk.CTkImage(dark_image=Image.open(spielen_logo.location_dark),light_image=Image.open(spielen_logo.location_light),size=(100,100))

cplus_pic = ctk.CTkImage(dark_image=Image.open(cplus_logo.location_dark),
                         light_image=Image.open(cplus_logo.location_light),size=(50,50))
csharp_pic = ctk.CTkImage(dark_image=Image.open(csharp_logo.location_dark),
                         light_image=Image.open(csharp_logo.location_light),size=(50,50))
java_pic = ctk.CTkImage(dark_image=Image.open(java_logo.location_dark),
                         light_image=Image.open(java_logo.location_light),size=(50,50))
python_pic = ctk.CTkImage(dark_image=Image.open(python_logo.location_dark),
                         light_image=Image.open(python_logo.location_light),size=(50,50))
#
welcome_screen_pic = ctk.CTkImage(dark_image=Image.open(welcome_screen_logo.location_light),
                                  light_image=Image.open(welcome_screen_logo.location_dark),size=(150,150))
learn_deutsch_pic = ctk.CTkImage(dark_image=Image.open(learn_duetsch_logo.location_dark),
                                 light_image=Image.open(learn_duetsch_logo.location_light),size=(200,100))
coding_pic = ctk.CTkImage(dark_image=Image.open(coding_logo.location_light),
                          light_image=Image.open(coding_logo.location_light),size=(125,125))
game_dev_pic = ctk.CTkImage(dark_image=Image.open(game_dev_logo.location_light),
                            light_image=Image.open(game_dev_logo.location_light),size=(100,100))


class properties_set :
	def __init__(self,Apperance_mode,Default_theme) :
		self.apperance_mode = Apperance_mode
		self.default_theme = Default_theme
Myapp = properties_set('Dark','dark-blue')

class colour_used :
    def __init__(self,Cyan_colour,blue_colour,greenish) :
          self.frame_light = Cyan_colour
          self.frame_dark = blue_colour
          self.frame_darker = greenish
mainmenu_colour = colour_used("#03404d","#2a3342","#424242")#"#011636"#046073

      