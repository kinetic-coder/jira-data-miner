import tkinter as tk
from tkinter import filedialog
import Utilities.FileRepository as fu
import Utilities.DateUtilities as du

from tkcalendar import DateEntry

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

                # Get screen size
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate control size based on screen size
        control_width = int(screen_width * 0.8)
        control_height = int(screen_height * 0.8)

        # Set control size
        self.master.geometry(f"{control_width}x{control_height}")

        self.create_widgets()

    def create_widgets(self):
        
        # Set label and entry width based on control size
        label_width = int(self.master.winfo_width() * 0.8)
        entry_width = int(self.master.winfo_width() * 0.8)

        self.start_date_label = tk.Label(self, text="Sprint start date")
        self.start_date_label.pack()

        self.start_date_entry = DateEntry(self)
        self.start_date_entry.pack()

        self.end_date_label = tk.Label(self, text="Sprint end date")
        self.end_date_label.pack()

        self.end_date_entry = DateEntry(self)
        self.end_date_entry.pack()
    
        self.file_label = tk.Label(self, text="File Path:")
        self.file_label.pack()

        self.file_entry = tk.Entry(self)
        self.file_entry.pack()

        self.browse_button = tk.Button(self)
        self.browse_button["text"] = "Browse"
        self.browse_button["command"] = self.load_file
        self.browse_button.pack()

        self.log_area = tk.Text(self)
        self.log_area.pack()

        self.process_button = tk.Button(self)
        self.process_button["text"] = "Process"
        self.process_button["command"] = self.process_file
        self.process_button.pack()

        self.quit_button = tk.Button(self, text="Exit", command=self.master.destroy)
        self.quit_button.pack()

    def load_file(self):
        filename = filedialog.askopenfilename()
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, filename)

    def process_file(self):
        filename = self.file_entry.get()
        self.log_area.insert(tk.END, f"Processing file: {filename}\n")
        # Add your file processing code here

        sprintDateRange = du.get_date_range(self.start_date_entry.get_date(), self.end_date_entry.get_date())
        
        for sprintDate in sprintDateRange:
            self.log_area.insert(tk.END, f"{sprintDate}\n")

        # sfileContents = fu.read_file_lines(filename)
        # for line in fileContents:
        #     self.log_area.insert(tk.END, f"{line}\n")

        self.log_area.insert(tk.END, "Done!\n") 