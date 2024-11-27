import tkinter as tk
from tkinter import filedialog
from basic_data_analysis import load, analysis, visualize

# Open file dialog and load dataset
def open_file():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file:
        data = load(file)
        analysis_results = analysis(data)
        visualize(data)
        
        # Display results in the label
        result_label.config(text=analysis_results)

# Set up the main window
def main_gui():
    global result_label  # Declare result_label as global here
    
    root = tk.Tk()
    root.title("Dat Analyzer")
    root.geometry("600x400")

    # Label to display results
    result_label = tk.Label(root, text="Select a CSVto analyze", justify='left', anchor="nw")
    result_label.pack(pady=20)

    # Button to open file dialog
    button = tk.Button(root, text="Open CSV", command=open_file)
    button.pack(pady=10)

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    main_gui()
