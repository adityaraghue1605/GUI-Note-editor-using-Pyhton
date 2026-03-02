# tkinter for creating Gui app 

import tkinter as tk 

from tkinter import filedialog, messagebox

# Main window code 

root = tk.Tk()
root.title("Simple text Editor")
root.geometry("800x600")
 
# code for text area 

text = tk.Text(
    root,
    wrap= tk.WORD,
    font=("Helvetica", 12)
)
text.pack(expand=True, fill=tk.BOTH)

# main logic

# Function to create new file 

def new_file():
    text.delete(1.0, tk.END)

# open new file 

def open_file():
    # open filedialogue 
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "+.txt")]
    )
    if file_path:
        # open file 
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# save the file 

def save_file():
    # open save file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "+.txt")]
    )
    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0, tk.END))
    messagebox.showinfo("info", "File saved successfully")

# Menu 

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)

#  New, opne file, save, exit

menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command= save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# starts and keep the window open 

root.mainloop()
