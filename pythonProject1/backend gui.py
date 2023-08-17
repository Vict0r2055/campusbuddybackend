import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import examtimetableupdater
import moduleupdater
import uploader

url = 'http://127.0.0.1:5000/upload'  # Replace with the actual server URL
folder_path = 'C:\\Users\\luyas\\Documents\\Campus'  # Replace with the actual folder path


def upload_file():
    file_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    print("Selected file:", file_path)
    file_loc = examtimetableupdater.open_file(file_path)
    print(file_loc)
    examtimetableupdater.process_output(file_loc)


def upload_file2():
    file_path2 = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    print("Selected file:", file_path2)


# Create the main window
window = tk.Tk()
window.title("Campus Buddy Backend")

# Create a Tab Control
tab_control = ttk.Notebook(window)

# Create the first tab for uploading PDF file
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Upload Examination Timetable')

# Create a button to upload file
button1 = ttk.Button(tab1, text="Upload Examination Timetable", command=upload_file)
button1.pack(pady=50)

# Create the second tab for uploading PDF file
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Upload Seating plan')

# Create a button to upload file
button4 = ttk.Button(tab2, text="Upload Seating plan", command=upload_file2)
button4.pack(pady=50)

# Create the third tab with a button
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Upload class schedule')

# Create a button in the third tab
button3 = ttk.Button(tab3, text="Update", command=moduleupdater.scrape_website)
button3.pack(pady=50)
# Create the second tab for uploading PDF file
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='Upload Server')

# Create a button to upload file
button4 = ttk.Button(tab4, text="Upload files to server", command=uploader.upload_files)
button4.pack(pady=50)

# Pack the Tab Control to the main window
tab_control.pack(expand=1, fill='both')

# Run the main event loop
window.mainloop()
