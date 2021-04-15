from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#Variable declarations
folderName = ""

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
    url = linkEntry.get()

    if(len(url) > 1):
       linkError.config(text="")
       ytLink = YouTube(url)

       if(opts == opt[0]):
           select = ytLink.streams.filter(progressive=True).first()
       elif(opts == opt[1]):
           select = ytLink.streams.filter(progressive=True,file_extension='mp4').last()
       elif(opts == opt[2]):
           select = ytLink.streams.filter(only_audio=True).first()
       else:
           linkError.config(text="Select video quality",fg="red")
    else:
        linkError.config(text="Paste link!!",fg="red")

#Download function
    select.download(folderName)
    linkError.config(text="Download Completed!!",fg="green")


#Window Display
window = Tk()
window.title("YouTube Downloader")
window.geometry("350x250")

#set all contents to center
window.columnconfigure(0,weight=1) 

#Link label
linkLabel = Label(window,text="Paste Link Here", font=("Sans Serif", 15))
linkLabel.grid()

#Link Entry Field
linkEntry = StringVar()
linkEntry = Entry(window,width=50,textvariable=linkEntry)
linkEntry.grid()

#Link error label
linkError = Label(window,text="",fg="red",font=("Sans Serif",10))
linkError.grid()

#File directory
dirLabel = Label(window,text="Select file location", font=("Sans Serif",10,"bold"))
dirLabel.grid()
dirButton = Button(window,width=10,bg="green",fg="white",cursor="hand2",text="Select folder",command=directory)
dirButton.grid()

#Link error label
dirError = Label(window,text="",fg="red",font=("Sans Serif",10))
dirError.grid()

#Video file quality
quaLabel = Label(window,text="Select video quality", font=("Sans Serif",10,"bold"))
quaLabel.grid()
opt = ["720p","480p","Audio Only"]
dwlOpt = ttk.Combobox(window,values=opt)
dwlOpt.grid()

#Download button
downloadBtn = Button(window,text="Download",width=10,bg="blue",fg="white",cursor="hand2",command=downloadvid)
downloadBtn.grid()

window.mainloop()