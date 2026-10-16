import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=time_string)
    label.after(1000, update_time)  # Update time every 1 second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.configure(bg='black')

# Create and configure the label
label = tk.Label(root, font=('italic', 50, 'bold'), background='black', foreground='pink')
label.pack(anchor='center')

update_time()  # Start updating time

root.mainloop()  # Run the Tkinter event loop