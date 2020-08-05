import eel, os, random
import tkinter as tk
from tkinter import filedialog
from converter import converter



# Initialize Dictinofrom nary to store parameters
path_dictionary = dict()
parameter_dict = dict()



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

@eel.expose
def fetch_all_parameters(input_filter,input_spectral,input_magnitude,input_photometric,output_filter,output_photometric):

	# print("RECEIVED ALL PARAMETERS ")

	print(input_filter,input_spectral,input_magnitude,input_photometric,output_filter,output_photometric)

	parameter_dict["input_filter"] = input_filter
	parameter_dict["input_spectral"] = input_spectral
	parameter_dict["input_magnitude"] = input_magnitude
	parameter_dict["input_photometric"] = input_photometric
	parameter_dict["output_filter"] = output_filter
	parameter_dict["output_photometric"] = output_photometric

@eel.expose
def final(input_filter,input_spectral,input_magnitude,input_photometric,output_filter,output_photometric):
	result = converter(path_dictionary[str(1)],path_dictionary[str(2)],path_dictionary[str(3)],input_filter,input_spectral,float(input_magnitude),input_photometric,output_filter,output_photometric)
	print(result)

eel.init('web')
eel.start('main.html')