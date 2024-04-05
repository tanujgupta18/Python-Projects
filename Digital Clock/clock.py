from tkinter import *
import datetime

def digital_clock():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,digital_clock)

clock=Tk()
clock.title("Digital Clock")
clock.config(bg="Black")
clock.geometry("1000x400")

lab = Label(clock,text="DIGITAL CLOCK",font=("Time New Roman",40,"bold"),bg="black",fg="Blue")
lab.place(x=250,y=290,height=50,width=500)

lab_hr = Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_hr.place(x=120,y=45,height=110,width=100)

lab_hr_txt = Label(clock,text="Hrs",font=("Time New Roman",30,"bold"),bg="black",fg="red")
lab_hr_txt.place(x=120,y=190,height=40,width=100)

lab_min = Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_min.place(x=340,y=45,height=110,width=100)

lab_min_txt = Label(clock,text="Mins",font=("Time New Roman",30,"bold"),bg="black",fg="red")
lab_min_txt.place(x=340,y=190,height=40,width=100)

lab_sec = Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_sec.place(x=560,y=45,height=110,width=100)

lab_sec_txt = Label(clock,text="Sec",font=("Time New Roman",30,"bold"),bg="black",fg="red")
lab_sec_txt.place(x=560,y=190,height=40,width=100)

lab_am = Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_am.place(x=780,y=45,height=110,width=100)

lab_am_txt = Label(clock,text="AM/PM",font=("Time New Roman",20,"bold"),bg="black",fg="red")
lab_am_txt.place(x=780,y=190,height=40,width=100)

digital_clock()

clock.mainloop()