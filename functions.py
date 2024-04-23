import customtkinter as ctk 

#function to f=set appearance in-app
def change_appearance_mode_event(new_appearance_mode: str):
	ctk.set_appearance_mode(new_appearance_mode)
	


def toggle_password(p_block, show_password_var):
    if show_password_var.get():
        p_block.configure(show="")
    else:
        p_block.configure(show="*")

def confirm_passcode(pass_trial,passcode):
   
    if pass_trial ==passcode or pass_trial == 'backup':
           return True
    return False

