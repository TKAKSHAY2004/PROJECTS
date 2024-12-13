import os
import shutil
from tkinter import Tk, filedialog, Button, Label, Entry, Listbox, Scrollbar, END

# Functions for file and folder operations
def choose_file():
    return filedialog.askopenfilename(title="Choose a File")

def choose_directory():
    return filedialog.askdirectory(title="Choose a Directory")

def open_file():
    file = choose_file()
    if file:
        os.startfile(file)

def create_folder():
    folder = choose_directory()
    name = folder_entry.get()
    if name and folder:
        os.mkdir(os.path.join(folder, name))

def move_file():
    file = choose_file()
    folder = choose_directory()
    if file and folder:
        shutil.move(file, folder)

def copy_file():
    file = choose_file()
    folder = choose_directory()
    if file and folder:
        shutil.copy(file, folder)

def delete_file():
    file = choose_file()
    if file:
        os.remove(file)

def rename_file():
    file = choose_file()
    new_name = rename_entry.get()
    if file and new_name:
        folder = os.path.dirname(file)
        ext = os.path.splitext(file)[-1]
        os.rename(file, os.path.join(folder, new_name + ext))

def delete_folder():
    folder = choose_directory()
    if folder:
        shutil.rmtree(folder)

def list_files():
    folder = choose_directory()
    if folder:
        listbox.delete(0, END)
        for file in os.listdir(folder):
            listbox.insert(END, file)

# GUI Configuration
root = Tk()
root.title("File Operations")
root.geometry("400x600")
root.configure(bg="lightblue")

# Folder Name Input
Label(root, text="Enter folder name:", bg="lightblue").pack(pady=5)
folder_entry = Entry(root)
folder_entry.pack(pady=5)

# Buttons for operations
Button(root, text="Open File", command=open_file, bg="green", fg="white").pack(pady=5)
Button(root, text="Create Folder", command=create_folder, bg="blue", fg="white").pack(pady=5)
Button(root, text="Move File", command=move_file, bg="orange", fg="white").pack(pady=5)
Button(root, text="Copy File", command=copy_file, bg="yellow").pack(pady=5)
Button(root, text="Delete File", command=delete_file, bg="red", fg="white").pack(pady=5)

# Rename File Input
Label(root, text="Enter new name:", bg="lightblue").pack(pady=5)
rename_entry = Entry(root)
rename_entry.pack(pady=5)

Button(root, text="Rename File", command=rename_file, bg="purple", fg="white").pack(pady=5)
Button(root, text="Remove Folder", command=delete_folder, bg="magenta", fg="white").pack(pady=5)
Button(root, text="List Files", command=list_files, bg="cyan").pack(pady=5)

# Listbox for displaying files
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(root, yscrollcommand=scrollbar.set, width=40, height=10)
listbox.pack(pady=10)
scrollbar.config(command=listbox.yview)

root.mainloop()
