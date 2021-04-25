#Importing necessary packages
from tkinter import *
import tkinter
from pytube import YouTube
from tkinter import messagebox,filedialog
from tkinter.ttk import *

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
#https://www.youtube.com/watch?v=gnJv0UdOC-Q

# percent = StringVar()
# workdone = StringVar()

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
    # video = pafy.new(url)
    # streams = video.allstreams
    # stream = streams[5]
    # value = stream.get_filesize()
    # print(str(value))

    # speed = 1000
    # dwnl = 0

    # while(dwnl<int(value)):
    #     time.sleep(0.05)
    #     bar['value'] +=(speed/value)*100
    #     dwnl+=speed
    #     percent.set(str(int((dwnl/value)*100))+"%")
    #     workdone.set(str(dwnl)+"/"+ str(value)+" completed")
    #     window.update_idletasks()

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
    
    linklabel = tkinter. Label(window,text="YouTube Link",width=11,bg="grey",font=("Comic Sans MS",10,"bold"))
    linklabel.grid(row=1,column=0,pady=5,padx=5)

    
    linkEntry = Entry(window,textvariable=vidLink,width=55)
    linkEntry.grid(row=1,column=1,pady=5,padx=5,columnspan=2)

    dirLabel = tkinter. Label(window,text="Location",width=11,bg="grey",font=("Comic Sans MS",10,"bold"))
    dirLabel.grid(row=2,column=0,pady=5,padx=5)

    
    directory = Entry(window,textvariable=downloadPath,width=43)
    directory.grid(row=2,column=1,pady=5,padx=5)

    dirButton = tkinter. Button(window,text="Browse",cursor="hand2",command=dirBrowse,width=7,bg="blue",fg="white",font=("Comic Sans MS",10,"bold"))
    dirButton.grid(row=2,column=2,pady=1,padx=1)

    downloadBtn = tkinter. Button(window,text="Download",cursor="hand2",command=Download,width=7,bg="blue",fg="white",font=("Comic Sans MS",10,"bold"))
    downloadBtn.grid(row=3,column=1,pady=3,padx=3)

    # percentage = tkinter. Label(window,textvariable=percent)
    # percentage.grid(row=5,column=1,pady=3,padx=3)

    # work = tkinter. Label(window,textvariable=workdone)
    # work.grid(row=6,column=1,pady=3,padx=3)

    devName = tkinter. Label(window,text="Copyright © 2021 Edem", font=("Comic Sans MS",13,"bold"))
    devName.grid(row=7,column=1,pady=3,padx=3)

widgets()
# bar = Progressbar(window,orient=HORIZONTAL,length=200)
# bar.grid(row=4,column=1,pady=3,padx=3)

# Defining infinite loop to run application
window.mainloop()