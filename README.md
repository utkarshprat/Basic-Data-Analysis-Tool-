    Data Analysis and Visualization Tool:-
    This project provides a simple and easy-to-use tool for performing basic data analysis and visualizations on CSV datasets. The tool allows users to:

    •   Load a CSV file.
    •   Calculate basic statistics such as Mean, Median, and Mode for numeric data.
    •   Visualize the data with Histograms for each numeric column.

    Features:-
    •   Data Loading: Import CSV data easily using a graphical user interface (GUI).
    •   Basic Analysis: Calculate and display the mean, median, and mode for all numeric columns in the dataset.
    •   Data Visualization: Generate histograms to visually explore the distribution of the data.

    How to Use:-
    Step 1: Install Dependencies-
        Before you begin, ensure you have the required libraries installed. You can install them using pip:
                     pip install pandas numpy matplotlib
    Step 2: Run the Program-
    •   Launch the Application: Run the program by executing meannn_gui.py.
        o    The GUI window will open, allowing you to select a CSV file for analysis.
    Step 3: Select Your Dataset-
    •   Click on the "Open CSV" button.
    •   Choose a CSV file from your computer that contains numerical data.
    Step 4: View Analysis and Visualizations-
    •   The tool will calculate the Mean, Median, and Mode for each numeric column in   your dataset.
    •   The results will be displayed in the GUI.
    •   Histograms will be plotted for each numeric column, helping you visualize the distribution of data.

    Code Explanation:-
    1.  meannn.py
    This file contains the core functions for loading the CSV, performing basic statistical analysis, and generating visualizations.

    •   load(file): Loads the CSV file into a pandas DataFrame.
    •   analysis(data): Calculates the mean, median, and mode for numeric columns in the data and formats the results into a string.
    •   visualize(data): Generates histograms for each numeric column in the data.
    2. meannn_gui.py
    This file contains the graphical user interface (GUI) built using tkinter.

    •   open_file(): Opens a file dialog for the user to select a CSV file, loads the data, and triggers the analysis and visualization functions.
    •   main_gui(): Sets up the main window, labels, and button in the GUI.
    •   Result Label: Displays the calculated mean, median, and mode for the dataset.
    
    Example:-
    After selecting a dataset, you might see the following results displayed in the GUI:
    Column A:
        Mean: 52.45
        Median: 54.00
        Mode: 50

    Column B:
        Mean: 200.78
        Median: 198.50
        Mode: 210
    Additionally, histograms for Column A and Column B will appear showing the distribution of values in each column.

    Troubleshooting:-
    •   Error: File not found: Make sure the file path is correct and the file exists.
    •   Error while generating histogram: Ensure that the selected CSV file contains numeric data for plotting
    

    Sample Images-
    
![mean (2)](https://github.com/user-attachments/assets/b0f75404-0b60-4266-844a-ca0c9966cfbd)
![mean (3)](https://github.com/user-attachments/assets/4fa8323b-57af-4e11-a6b4-be4ba9664d30)
![mean (4)](https://github.com/user-attachments/assets/dc018d06-4bc6-4fc2-94d9-31c3d7ab2024)
![mean (5)](https://github.com/user-attachments/assets/a76ef187-2deb-412c-bc6e-928f40260d93)
![mean](https://github.com/user-attachments/assets/e2ec8bd7-2446-4257-8aac-dc08a1a389a3)

