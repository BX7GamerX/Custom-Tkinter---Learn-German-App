import customtkinter as ctk  # for the entire GUI and it'sfunctionalities
from PIL import Image  # for the logo and images to be used handling
import tkinter  # for center orientation
from functions import confirm_passcode, toggle_password  #functions module import
from assetlib import welcome_screen_pic
from assetlib import resource_path

# user_logo = ctk.CTkImage (dark_image=Image.open("images/logo.jpg"),
#                           light_image=Image.open("images/logo.png") ,size=(150, 150  ))#the welcome frme logo
user_logo = welcome_screen_pic
#hfile = open("neccessities\\handlling.txt","+r")
app_version = 0.5  #(hfile.readlines()[3])
#hfile.close
#vfile = open('neccessities\\version_doc.txt','+r')
passcode = 'him'  #(vfile.readlines()[0])


#vfile.close
#The WelcomeFrame

class WelcomeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #self.master = master

        self.setup_welcome_frame()  #main function to setup up the frame and its widgets

    def setup_welcome_frame(self):
        #the Welcome frame
        self.welcome_frame = ctk.CTkFrame(self, width=320, height=380)  #Frame n it's attributes
        self.welcome_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)  #frame position relative to the window
        #The frame label/Name
        self.welcome_label = ctk.CTkLabel(self.welcome_frame, text="Welcome",
                                          font=('Century Gothic', 25))  #,text_color='')
        self.welcome_label.place(x=100, y=5)  #position of the label
        self.welcome_label.bind("<Enter>",
                                lambda event: self.welcome_label.configure(cursor="hand2", text_color="green"))
        self.welcome_label.bind("<Leave>",
                                lambda event: self.welcome_label.configure(cursor="arrow", text_color="#92c3c9"))
        self.welcome_label.bind("<Button-1>", lambda event: self.master.change_apperance_mode())
        #Logo label impimentation
        self.logo_label = ctk.CTkLabel(self.welcome_frame, image=user_logo, text="",
                                       font=ctk.CTkFont(size=20, weight="bold"), corner_radius=25)
        self.logo_label.place(x=80, y=55)  #position
        #password
        self.show_password_var = ctk.BooleanVar()  #bool to check wheither or not the show passcode was pressed
        self.pass_code_entry = ctk.CTkEntry(master=self.welcome_frame, width=220,
                                            placeholder_text="Password", show="*")
        self.pass_code_entry.place(x=50, y=210)
        self.pass_code_entry.focus()

        self.show_password = ctk.CTkCheckBox(master=self.welcome_frame,
                                             text="Show Password", font=('Century Gothic', 12),
                                             command=lambda: toggle_password(self.pass_code_entry,
                                                                             self.show_password_var),
                                             variable=self.show_password_var)
        self.show_password.place(x=85, y=245)
        #forgot password label
        self.forgot_label = ctk.CTkLabel(master=self.welcome_frame, text="Forgot password/New?",
                                         font=('Century Gothic', 10))
        self.forgot_label.place(x=90, y=280)
        self.forgot_label.bind("<Enter>", lambda event: self.forgot_label.configure(cursor="hand2",
                                                                                    text_color="green"))  #binds the label to the lambda func that changes the cursor
        # Change cursor back to the default arrow when mouse leaves the widget
        self.forgot_label.bind("<Leave>", lambda event: self.forgot_label.configure(cursor="arrow", text_color="white"))
        # Bind the click event to open the Forgot Password frame
        #self.label3.bind("<Button-1>", lambda event: self.master.open_forgot_password_frame())
        self.error_label = ctk.CTkLabel(master=self.welcome_frame, text="",
                                        font=('Century Gothic', 15), text_color="#ff0004")
        self.error_label.place(x=105, y=300)
        #Login button
        self.login_button = ctk.CTkButton(master=self.welcome_frame, width=100, text="Login",
                                          corner_radius=6, fg_color="#3498db", text_color="#ffffff",
                                          hover_color="green", command=self.check_passcode)
        self.login_button.place(x=100, y=325)

        self.app_version_label = ctk.CTkLabel(self.welcome_frame, text=app_version,
                                              font=('Century Gothic', 10))
        self.app_version_label.bind("<Enter>",
                                    lambda event: self.app_version_label.configure(cursor="hand2", text_color="blue"))
        self.app_version_label.bind("<Leave>",
                                    lambda event: self.app_version_label.configure(cursor="arrow", text_color="white"))
        self.app_version_label.place(x=250, y=335)  #position of the label

        #me Him Work

    def check_passcode(self):

        # try:
        if self.pass_code_entry.get() != "":
            if confirm_passcode(self.pass_code_entry.get(),
                                passcode):  # confirm_passcode(self.pass_code_entry.get(),cfille.readlines()[2]):# or
                self.master.open_main_menu_frame("welcomeframe")
            else:
                self.error_label.configure(text="Invalid Password")
        else:
            self.error_label.configure(text="Invalid Entry")

            # except Exception as e:

    #     self.error_label.configure(text=e)


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("360x130")  #dimensions of the window
        self.title("Learn German")  #title of the window
        self.label = ctk.CTkLabel(self, text="Do you want to exit?")  #exit prompt
        self.label.pack(padx=20, pady=20)  # spacing of the prompt
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)  # position of the prompt

        self.yes_button = ctk.CTkButton(self, text="Yes", command=self.exit_f)  # the yes button
        self.yes_button.grid(row=1, column=0, padx=20, pady=10)

        self.no_button = ctk.CTkButton(self, text="No", command=self.destroy)  # the no button
        self.no_button.grid(row=1, column=1, padx=20, pady=10)

    def exit_f(self):
        self.destroy()
        exit()
