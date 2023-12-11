import os
import shutil
from tkinter import Tk
from tkinter import filedialog

#testing files with a test directory path

def choose_file():
    filename = filedialog.askopenfilename(title="Choose a file",
                                          filetypes=(("All Files", "*.*"), ("Text files", "*.txt")))
    return filename

def choose_directory():
    dirname = filedialog.askdirectory(title="Choose directory.")
    return dirname

def main():
    print("-------------------------")
    print("\t OPERATIONS")
    print("-------------------------")
    print(" 1 - OPEN A EXISTING FILE ")
    print(" 2 - CREATE A NEW FOLDER/DIR")
    print(" 3 - MOVE A FILE ")
    print(" 4 - COPY A FILE ")
    print(" 5 - DELETE A FILE ")
    print(" 6 - RENAME A FILE ")
    print(" 7 - REMOVE A FOLDER ")
    print(" 8 - LIST ALL FILES IN THE DIRECTORY ")
    print("-------------------------")
    choice = int(input("CHOOSE A OPERATION (1-8) : "))

    #open file
    if choice == 1:
        filename = filedialog.askopenfilename(title="Choose a file",filetypes=(("All Files", "*.*"),("Text files", "*.txt")))
        os.startfile(filename)

    #create new file
    elif choice == 2:
        folder = choose_directory()
        name = input("Enter folder name:> ")
        folder_name = folder + "/" + name
        os.mkdir(folder_name)

    #move file
    elif choice == 3:
        file = choose_file()
        to_location = choose_directory()
        shutil.move(file, to_location)

    #copy file
    elif choice == 4:
        to_copy = choose_file()
        to_location = choose_directory()
        shutil.copy(to_copy, to_location)

    #delete file
    elif choice == 5:
        file = choose_file()
        os.remove(file)

    #rename
    elif choice == 6:
        file = choose_file()
        new_name = input("Enter new name:> ")
        ext = os.path.splitext(from_file)[-1]
        dirname = os.path.dirname(from_file)
        new_file = os.path.join(dirname, to_file + ext)
        os.rename(from_file, new_file)

    #remove folder
    elif choice == 7:
        folder = choose_directory()
        shutil.rmtree(folder)

    #list files
    if choice == 8:
        folder = choose_directory()
        items = os.listdir(folder)
        print("These are the folder(s) or file(s) in this directory")
        for item in items:
            print(item)


main()
