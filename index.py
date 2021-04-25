from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import pafy
import time

folderName = ""
#https://www.youtube.com/watch?v=gnJv0UdOC-Q

#File directory function
def directory():
    global folderName
    folderName = filedialog.askdirectory()
    if(len(folderName) > 1):
        dirError.config(text=folderName,fg="green")
    else:
        dirError.config(text="Please select file location",fg="red")

#Video download function
def downloadvid():
    
    opts = dwlOpt.get()
    url = linkEntrys.get()
    video = pafy.new(url)
    linkDuration = video.length
    
    download = 0
    speed = 1
    while(download<linkDuration):
        time.sleep(1)
        bar['value'] +=(speed/linkDuration)*100
        download+=speed
        percent.set(str(int((download/linkDuration)*100))+"%")
        workdone.set(str(download)+"/"+ str(linkDuration)+" completed")
        window.update_idletasks()

    if(len(url) > 1):
       linkError.config(text="")
       ytLink = YouTube(url)

       if(opts == opt[0]):
           select = ytLink.streams.filter(progressive=True).first()
       elif(opts == opt[1]):
           select = ytLink.streams.filter(progressive=True,file_extension='mkv').first()
       elif(opts == opt[2]):
           select = ytLink.streams.filter(progressive=True,file_extension='mkv').first()
       elif(opts == opt[3]):
           select = ytLink.streams.filter(progressive=True,file_extension='mp4').last()
       elif(opts == opt[4]):
           select = ytLink.streams.filter(progressive=True,file_extension='mp4').last()
       elif(opts == opt[5]):
           select = ytLink.streams.filter(only_audio=True).first()
       else:
           linkError.config(text="Select video quality",fg="red")
    else:
        linkError.config(text="Paste link!!",fg="red")

#Download function
    select.download(folderName)
    linkError.config(text="Download Completed!!",fg="green")

#Function to Reset  
def Reset():
    linkEntry.set(" ")
    dwlOpt.set(" ")
    linkError.config(text=" ")
    percentage.config(text=" ")
    work.config(" ")
    dirLabel.config(" ")    
    


#Window Display
window = Tk()
window.title("YouTube Downloader")
window.geometry("350x360")
window.resizable(0,0)
icon = PhotoImage(file='C:/Users/kurtk/OneDrive/Desktop/DontOpen/Python/Projects/YouTube Downloader/youtube.png')
window.iconphoto(True,icon)

#set all contents to center
window.columnconfigure(0,weight=1) 

#Link label
linkLabel = Label(window,text="Paste Link Here", font=("Comic Sans MS", 15))
linkLabel.grid()

#Link Entry Field
linkEntry = StringVar()
linkEntrys = Entry(window,width=50,textvariable=linkEntry)
linkEntrys.grid()

space = Label(window,text="", font=("Comic Sans MS",2,"bold"))
space.grid()

#Progress bar
percent = StringVar()
workdone = StringVar()
bar = ttk.Progressbar(window,orient=HORIZONTAL,length=300)
bar.grid()

percentage = Label(window,textvariable=percent)
percentage.grid()
work = Label(window,textvariable=workdone)
work.grid()


#Link error label
linkError = Label(window,text="",fg="red",font=("Comic Sans MS",10))
linkError.grid()

#File directory
dirLabel = Label(window,text="Select file location", font=("Comic Sans MS",10,"bold"))
dirLabel.grid()
dirButton = Button(window,width=10,bg="green",fg="white",cursor="hand2",text="Select folder",command=directory)
dirButton.grid()

#Link error label
dirError = Label(window,text="",fg="red",font=("Sans Serif",10))
dirError.grid()

#Video file quality
quaLabel = Label(window,text="Select video quality", font=("Comic Sans MS",10,"bold"))
quaLabel.grid()
opt = ["1080p","720p","480p","360p","240p","Audio Only"]
dwlOpt = ttk.Combobox(window,values=opt)
dwlOpt.grid()

space = Label(window,text="", font=("Comic Sans MS",2,"bold"))
space.grid()

#Download button
downloadBtn = Button(window,text="Download",width=7,bg="blue",fg="white",cursor="hand2",command=downloadvid)
downloadBtn.place(x=105 , y =275)

resetBtn = Button(window,text="Reset",width=7,bg="grey",fg="white",cursor="hand2",command=Reset)
resetBtn.place(x=183 , y =275)

space = Label(window,text="", font=("Comic Sans MS",10,"bold"))
space.grid()


devName = Label(window,text="Copyright © 2021 Edem", font=("Comic Sans MS",13,"bold"))
devName.grid()

window.mainloop()