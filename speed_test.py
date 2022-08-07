from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3))+ "Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet speed")
sp.geometry("500x650")

lab = Label(sp,text="Internet speed test", font=("Time New Roman",30,"bold"))
lab.place(x=70, y=40, height=30, width=380)

lab = Label(sp,text="Download Speed", font=("Time New Roman",30,"bold"))
lab.place(x=70, y=130, height=30, width=380)

lab_down = Label(sp,text="00", font=("Time New Roman",30,"bold"))
lab_down.place(x=70, y=200, height=30, width=380)

lab = Label(sp,text="Upload Speed", font=("Time New Roman",30,"bold"))
lab.place(x=70, y=290, height=30, width=380)

lab_up = Label(sp,text="00", font=("Time New Roman",30,"bold"))
lab_up.place(x=70, y=360, height=30, width=380)

button = Button(sp, text="Check Speed", font=("Time New Roman",25,"bold"),relief=RAISED,bg="red", command=speedcheck)
button.place(x=70, y=460, height=30, width=380)

sp.mainloop()