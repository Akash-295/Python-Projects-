#tkinter module and library - collection of modules.
#import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox  #submodule of tkinter

root=tk.Tk()
root.title("Simple text Editor")
root.geometry("800x600")

#creating text area
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=("helvetica", 12)
)

text.pack(expand=True, fill=tk.BOTH)

#main logic starts here 

#function 1- to create a new file
def new_file():
    text.delete(1.0, tk.END)
    
#function 2-to open a new file
def open_file():
    #open file dialog
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    
    if file_path:
        #open file
        with open(file_path, "r") as file:
            #clear old text
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
            
#function 3- Save the file 

def save_file():
    #open save file dialog
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
            
    messagebox.showinfo("Info", "File saved Successfully.")
    
#create Menu

menu=tk.Menu(root)
root.config(menu=menu)

file_menu=tk.Menu(menu)

#New, Open File, Save, Exit

#add file menu to menu bar 
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open File",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)


root.mainloop()  #it starts and keeps the window open