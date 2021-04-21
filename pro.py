from tkinter import *
from tkinter.ttk import *
import time
import pafy
import youtube_dl

#https://www.youtube.com/watch?v=0WRMYdOwHYE
# url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
# video = pafy.new(url)

url = "https://www.youtube.com/watch?v=0WRMYdOwHYE"
video = pafy.new(url)

dur = video.length
# print(video.duration)




def start():
    
    download = 0
    speed = 1
    while(download<int(dur)):
        time.sleep(0.05)
        bar['value'] +=(speed/dur)*100
        download+=speed
        percent.set(str(int((download/dur)*100))+"%")
        workdone.set(str(download)+"/"+ str(dur)+"dur completed")
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