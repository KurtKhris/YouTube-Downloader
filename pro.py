# # Importing necessary packages
# import tkinter as tk
# from tkinter import *
# from pytube import YouTube
# from tkinter import messagebox, filedialog


# # Creating object of tk class
# window = tk.Tk()

# # Setting the title, icon and size of the tkinter window and disabling the resizing property
# window.geometry("500x150")
# window.resizable(0, 0)
# window.title("YouTube Downloader")
# icon = PhotoImage(file='C:/Users/kurtk/OneDrive/Desktop/DontOpen/Python/Projects/YouTube Downloader/youtube.png')
# window.iconphoto(True,icon)

# # Defining widgets() function to create necessary tkinter widgets
# def widgets():
# 	linkLabel = Label(window,text="YouTube Link",width=11,bg="grey",font=("Comic Sans MS",10,"bold"))
# 	linkLabel.grid(row=1,column=0,pady=5,padx=5)

# 	linkEntry = Entry(window,width=55,textvariable=vidLink)
# 	linkEntry.grid(row=1,column=1,pady=5,padx=5,columnspan = 2)

# 	dirLabel = Label(window,text="Location",width=11,bg="grey",font=("Comic Sans MS",10,"bold"))
# 	dirLabel.grid(row=2,column=0,pady=5,padx=5)

# 	directory = Entry(window,width=43,textvariable=downloadPath)
# 	directory.grid(row=2,column=1,pady=5,padx=5)

# 	dirButton = Button(window,text="Browse",cursor="hand2",command=dirBrowse,width=7,bg="blue",fg="white",font=("Comic Sans MS",10,"bold"))
# 	dirButton.grid(row=2,column=2,pady=1,padx=1)

# 	downloadBtn = Button(window,text="Download",cursor="hand2", command=Download,width=7,bg="blue",fg="white",font=("Comic Sans MS",10,"bold"))
# 	downloadBtn.grid(row=3,column=1,pady=3,padx=3)

# devName = Label(window,text="Copyright © 2021 Edem", font=("Comic Sans MS",13,"bold"))
# devName.grid(row=4,column=1,pady=3,padx=3)

    

# # Defining Browse() to select the directory to save the video
# def dirBrowse():
# 	downloadDir = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    
# 	# Displaying the directory in the directory textbox
     
# 	downloadPath.set(downloadDir)

# # Defining Download() to download the video
# def Download():
	
# 	# getting user input Youtube Link
# 	url = vidLink.get()
	
# 	# selecting file location
# 	downloadFolder = downloadPath.get()

# 	# Creating object of YouTube()
# 	getVideo = YouTube(url)

# 	# Getting all the available streams of the youtube video and selecting the highest resolution
# 	videoStream = getVideo.streams.get_highest_resolution()

# 	# Downloading the video to the directory selected
# 	videoStream.download(downloadFolder)

# 	# Displaying the message
# 	messagebox.showinfo("YouTube Downloader","Video Downloaded Successfully!! and saved to\n"+ downloadFolder)



# # Creating the tkinter Variables
# vidLink = StringVar()
# downloadPath = StringVar()

# # Calling the Widgets() function
# widgets()

# # Defining infinite loop to run application
# window.mainloop()



































from tkinter import *
from tkinter.ttk import *
import time
from pytube import YouTube
import pafy
# import youtube_dl

# #https://www.youtube.com/watch?v=0WRMYdOwHYE
# # url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
# # video = pafy.new(url)

import enum
# Enum for size units
# class SIZE_UNIT(enum.Enum):
#    BYTES = 1
#    KB = 2
#    MB = 3
#    GB = 4
# def convert_unit(size_in_bytes, unit):
#    """ Convert the size from bytes to other units like KB, MB or GB"""
#    if unit == SIZE_UNIT.KB:
#        return size_in_bytes/1024
#    elif unit == SIZE_UNIT.MB:
#        return size_in_bytes/(1024*1024)
#    elif unit == SIZE_UNIT.GB:
#        return size_in_bytes/(1024*1024*1024)
#    else:
#        return size_in_bytes


url = "https://www.youtube.com/watch?v=gnJv0UdOC-Q"
video = pafy.new(url)

streams = video.allstreams

stream = streams[5]

value = stream.get_filesize()


print(str(value))




def start():
    
    download = 0
    speed = 1000
    while(download<int(value)):
        time.sleep(0.05)
        bar['value'] +=(speed/value)*100
        download+=speed
        percent.set(str(int((download/value)*100))+"%")
        workdone.set(str(download)+"/"+ str(value)+" completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()

workdone = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=200)
bar.pack()

percentage = Label(window,textvariable=percent).pack()

work = Label(window,textvariable=workdone).pack()


button = Button(window,text="Download",command=start).pack()

window.mainloop()