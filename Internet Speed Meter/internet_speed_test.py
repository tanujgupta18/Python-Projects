from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="black")

lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",20,"bold"),bg="black",fg="Blue")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed",font=("Time New Roman",20,"bold"),bg="black",fg="Green")
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="black",fg="White")
lab_down.place(x=60,y=180,height=50,width=380)

lab= Label(sp,text="Upload Speed",font=("Time New Roman",20,"bold"),bg="black",fg="Purple")
lab.place(x=60,y=270,height=50,width=380)

lab_up = Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="black",fg="White")
lab_up.place(x=60,y=320,height=50,width=380)

button = Button(sp,text="Check Speed",font=("Time New Roman",20,"bold"),relief=RAISED,bg="red",command=speedcheck)
button.place(x=60,y=410,height=50,width=380)

sp.mainloop()
