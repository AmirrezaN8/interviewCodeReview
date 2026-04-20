import tkinter as tk
from tkinter import filedialog
from extractor import process_resumes

#function for prompting the user to select a folder and processing the resumes in that folder
def prompt_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select the folder containing resumes")
    return folder_path


#main function to run the program, prompting the user to select a folder and processing the resumes in that folder, then printing the results in JSON format
if __name__ == "__main__":

    print("Waiting for folder selection...")
    folder_path = prompt_folder()
    
    if not folder_path:
        print("No folder selected. Exiting.")
    else:
        print(f"Folder selected: {folder_path}")
        print("Processing resumes...\n")

        json_results = process_resumes(folder_path)

        print("Results in JSON format:")
        print(json_results)

