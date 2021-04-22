#Importing necessary packages
# import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog

#Creating an object of Tk()
window = Tk()

# Setting the title, icon and size of the tkinter window and disabling the resizing property
window.geometry("500x150")
window.resizable(0, 0)
window.title("YouTube Downloader")
icon = PhotoImage(file='C:/Users/kurtk/OneDrive/Desktop/DontOpen/Python/Projects/YouTube Downloader/youtube.png')
window.iconphoto(True,icon)

#Variables
downloadPath = StringVar()
vidLink = StringVar()


# Defining Browse() to select the directory to save the video
def dirBrowse():
    downloadDir = filedialog.askdirectory()
    if (len(downloadDir) > 1):
        downloadPath.set(downloadDir)
    else:
        messagebox.showwarning("YouTube Downloader", "Please select directory")



# Defining Download() to download the video
def Download():
    # getting user input Youtube Link
    url = vidLink.get()

    if(len(url) > 1):

        #Selecting file location
        downloadFolder = downloadPath.get()

        # Creating an object of YouTube()
        getVideo = YouTube(url)

        # Getting all the available streams of the youtube video and selecting the highest resolution
        videoStream = getVideo.streams.get_highest_resolution()

        # Downloading the video to the directory selected
        videoStream.download(downloadFolder)

        # Displaying success message after downloading video
        messagebox.showinfo("YouTube Downloader","Video Downloaded Successfully!! and saved to\n"+ downloadFolder)

    else:
        messagebox.showwarning("YouTube Downloader", "Please Enter YouTube link and Select Directory.")

# Defining widgets() function to create necessary tkinter widgets
def widgets():
    linklabel = Label(window,text="YouTube Link",width=11,bg="grey",font=("Comic Sans MS",10,"bold"))
    linklabel.grid(row=1,column=0,pady=5,padx=5)

    
    linkEntry = Entry(window,textvariable=vidLink,width=55)
    linkEntry.grid(row=1,column=1,pady=5,padx=5,columnspan=2)

    dirLabel = Label(window,text="Location",width=11,bg="grey",font=("Comic Sans MS",10,"bold"))
    dirLabel.grid(row=2,column=0,pady=5,padx=5)

    
    directory = Entry(window,textvariable=downloadPath,width=43)
    directory.grid(row=2,column=1,pady=5,padx=5)

    dirButton = Button(window,text="Browse",cursor="hand2",command=dirBrowse,width=7,bg="blue",fg="white",font=("Comic Sans MS",10,"bold"))
    dirButton.grid(row=2,column=2,pady=1,padx=1)

    downloadBtn = Button(window,text="Download",cursor="hand2",command=Download,width=7,bg="blue",fg="white",font=("Comic Sans MS",10,"bold"))
    downloadBtn.grid(row=3,column=1,pady=3,padx=3)

    devName = Label(window,text="Copyright © 2021 Edem", font=("Comic Sans MS",13,"bold"))
    devName.grid(row=4,column=1,pady=3,padx=3)

widgets()

# Defining infinite loop to run application
window.mainloop()