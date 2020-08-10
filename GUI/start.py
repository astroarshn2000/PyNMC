# Import Libraries
import eel, os, random
import tkinter as tk
from tkinter import filedialog
from converter import converter
import json

# Initialize Dictionaries to store parameters
path_dictionary = dict()
parameter_dict = dict()

#Functions
@eel.expose
def selectFolder(num):
	eel.modify_status()
	root = tk.Tk()
	root.withdraw()
	user_info = "You have selected : "
	directory_path = filedialog.askdirectory()
	path_dictionary[str(num)] = str(directory_path)
	eel.modify_p_tag(num, user_info + str(directory_path))
	eel.modify_status()
	root.destroy()

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

def save_json_file(path_dictionary):
	with open("history.json", "w") as outfile:
		json.dump(path_dictionary, outfile)

@eel.expose
def final(input_filter,input_spectral,input_magnitude,input_photometric,output_filter,output_photometric):
	
	print(path_dictionary)

	save_json_file(path_dictionary)

	print(path_dictionary)
	
	result = converter(path_dictionary[str(1)],path_dictionary[str(2)],path_dictionary[str(3)],input_filter,input_spectral,float(input_magnitude),input_photometric,output_filter,output_photometric)
	# print(result)
	eel.display_final_output(result)

def load_previous_file_path():
	flag = True
	user_info = "You have selected : "
	with open('history.json', 'r') as openfile: 
	    # Reading from json file 
	    path_history_dictionary = json.load(openfile)
	for key in path_history_dictionary.keys():
		if not path_history_dictionary.get(key):
			flag = False
			break
	if flag :
		for key in path_history_dictionary.keys():
			path_dictionary[(key)] = str(path_history_dictionary[key])
			eel.modify_p_tag(int(key), user_info + str(path_dictionary.get(key)))

		return path_dictionary

	else :
		print("No History")
		return dict()

# Run the main.html through eel
eel.init('web')
path_dictionary = load_previous_file_path()
eel.start('main.html')