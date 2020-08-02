import eel, os, random
import tkinter as tk
from tkinter import filedialog

path_dictionary = dict()

# @eel.expose
# def selectFolder(num):

#     directory_path = filedialog.askdirectory()

#     user_info = "You have selected : "

#     path_dictionary[str(num)] = str(directory_path)

#     eel.modify_p_tag(num,user_info + str(directory_path))

#     root.destroy()

#     return str(directory_path)


@eel.expose
def selectFolder(num):

	root = tk.Tk()
	root.withdraw()

	user_info = "You have selected : "

	directory_path = filedialog.askdirectory()

	path_dictionary[str(num)] = str(directory_path)

	eel.modify_p_tag(num, user_info + str(directory_path))

	root.destroy()

	return str(directory_path)

eel.init('web')
eel.start('main.html')