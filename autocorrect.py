import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

class AutoCorrectEntry:
    def __init__(self, root):
        self.root = root
        self.current_timer = None

        # Create a frame to hold the widgets
        frame = ttk.Frame(root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create an input entry widget
        self.input_entry = ttk.Entry(frame, width=50)
        self.input_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.input_entry.bind("<Key>", self.on_key_press)
        self.input_entry.bind("<space>", self.on_space_press)

        # Set the focus to the input entry
        self.input_entry.focus()

    def autocorrect(self):
        content = self.input_entry.get()
        corrected_content = str(TextBlob(content).correct())
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, corrected_content)

    def on_key_press(self, event):
        if self.current_timer is not None:
            self.root.after_cancel(self.current_timer)
        self.current_timer = self.root.after(3000, self.autocorrect)

    def on_space_press(self, event):
        self.autocorrect()

# Create the main window
root = tk.Tk()
root.title("Python GUI with Advanced Autocorrect")

# Initialize the autocorrect entry system
auto_correct_entry = AutoCorrectEntry(root)

# Start the application
root.mainloop()
