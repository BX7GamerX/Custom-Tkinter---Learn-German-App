from mainapplication import MainApp
#from assetlib import resource_path
	
if __name__=="__main__":
	app = MainApp()
	#app.iconbitmap(resource_path("logo.ico"))
	app.update()
	app.mainloop()