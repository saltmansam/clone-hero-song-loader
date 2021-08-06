import webview
import threading
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import extractorMover

root = Tk()

root.title("Chorus Clone Hero Loader")

# Make the window
width = 769
height = 435

root.geometry(str(width) + 'x' + str(height))

directory_to_extract_to = ""
path_to_zip_file = ""

# Create a photoimage object of the image in the path
bckgnd = Image.open("./background.jpg")
bg = ImageTk.PhotoImage(bckgnd)
background = tkinter.Label(image=bg)
background.image = bg

background.place(x= 0, y= 0)

searchBar = Entry(root)

def openPage(query = ""):
    webview.create_window(title = 'Chorus Viewer', url = 'https://chorus.fightthe.pw/search?query=' + query, on_top = True)
    webview.start() # this will open the webpage in a new window

def songFolderFnc():
    global directory_to_extract_to, songFolderEntry
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    directory_to_extract_to = filedialog.askdirectory() # show an "Open" dialog box and return the path to the selected file
    
    f = open("./songs location folder.txt", "w")
    f.write(directory_to_extract_to)
    f.close()
    
    # change the text in the entry field
    songFolderEntry.delete(0, "end")
    songFolderEntry.insert(0, directory_to_extract_to)

def songFileFnc():
    global path_to_zip_file, songFileEntry
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    path_to_zip_file = askopenfilename(filetypes = (("Zip files", "*.zip")
                                        ,("7zip files", "*.7z")
                                        ,("Rar files", "*.rar") )) # show an "Open" dialog box and return the path to the selected file
    
    # change the text in the entry field
    songFileEntry.delete(0, "end")
    songFileEntry.insert(0, path_to_zip_file)

def extractAndMove():
    global path_to_zip_file, directory_to_extract_to
    # extract the song from the folder with either 7z, or windows extractor and then put in the song folder
    extractorMover.extractFiles(path_to_zip_file, directory_to_extract_to)

def autofill():
    global directory_to_extract_to
    # auto-fill song folder location
    f = open("./songs location folder.txt", "r")
    line = f.readline()
    if line != "": # if no song folder is remembered it remains blank
        songFolderEntry.delete(0, "end")
        songFolderEntry.insert(0, line)
    f.close()
    directory_to_extract_to = line

# ask for clone hero song folder location
songFolderButton = Button(root, text = 'Select Clone Hero Songs Folder', command = songFolderFnc)
songFolderButton.place(x = 50, y = 50)

songFolderEntry = Entry(root, text = 'path to song folder')
songFolderEntry.place(x = 50, y = 75)

songFolderEntry.delete(0, "end")
songFolderEntry.insert(0, directory_to_extract_to)

# ask for song file location
songFileButton = Button(root, text = 'Select Song Zip', command = songFileFnc)
songFileButton.place(x = 50, y = 125)

songFileEntry = Entry(root, text = 'path to song zip file')
songFileEntry.place(x = 50, y = 150)

# extract button
extractButton = Button(root, text = 'Extract and Move', command = extractAndMove)
extractButton.place(x = 50, y = 200)

# autofill button
autofillButton = Button(root, text = 'autofill path', command = autofill)
autofillButton.place(x = 175, y = 75)



# open webpage
#openPage()

def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()