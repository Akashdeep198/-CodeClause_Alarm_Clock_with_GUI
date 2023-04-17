from threading import Thread
from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk,Image
from pygame import mixer

from datetime import datetime

from time import sleep

bg_color ='blue'
color='black'
color_2='pink'

window =Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)

frame_line =Frame(window,width=400,height=5,bg=color)
frame_line.grid(row=0,column=0)

frame_body =Frame(window,width=400,height=290,bg=color_2)
frame_body.grid(row=1,column=0)

img=Image.open('icons8-alarmclock-100 (1).png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)

app_image =Label(frame_body,height=100,image=img,bg=color_2)
app_image.place(x=10,y=10)

name=Label(frame_body,text="Alarm",height=1,font=('Ivy 18 bold'),bg=color_2)
name.place(x=125,y=10)

hour=Label(frame_body,text="Hour",height=1,font=('Ivy 11 bold'),bg=color_2,fg="blue")
hour.place(x=125,y=40)

c_hour=Combobox(frame_body,width=2,font=('arial 15'))
c_hour['values']=("00","01","02","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=130,y=58)

minute=Label(frame_body,text="Minute",height=1,font=('Ivy 11 bold'),bg=color_2,fg="blue")
minute.place(x=175,y=40)

c_minute=Combobox(frame_body,width=2,font=('arial 15'))
c_minute['values']=("00","01","02","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","40","51","52","53","54","55","56","57","58","59","60")
c_minute.current(0)
c_minute.place(x=180,y=58)

second=Label(frame_body,text="Sec",height=1,font=('Ivy 11 bold'),bg=color_2,fg="blue")
second.place(x=235,y=40)

c_second=Combobox(frame_body,width=2,font=('arial 15'))
c_second['values']=("00","01","02","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","40","51","52","53","54","55","56","57","58","59","60")
c_second.current(0)
c_second.place(x=238,y=58)

period=Label(frame_body,text="Period",height=1,font=('Ivy 11 bold'),bg=color_2,fg="blue")
period.place(x=285,y=40)

c_period=Combobox(frame_body,width=3,font=('arial 15'))
c_period['values']=("AM","PM")
c_period.current(0)
c_period.place(x=290,y=58)

def activate_alarm():
    t=Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivate Alarm:',selected.get())
    mixer.music.stop()
    

selected =IntVar()

rad1=Radiobutton(frame_body,font=('arial 10 bold'), value=1, text="Activate",bg=color_2,command=activate_alarm,variable=selected)
rad1.place(x=125,y=95)

def sound_alarm():
    mixer.music.load('alarm2.mp3')
    mixer.music.play()
    selected.set(0)
    
    rad2=Radiobutton(frame_body,font=('arial 10 bold'), value=2, text="deactivate",bg=color_2,command=deactivate_alarm,variable=selected)
    rad2.place(x=187,y=95)
    
def alarm():
    while True:
        control=selected.get()
        print(control)
        alarm_hour=c_hour.get()
        alarm_minute=c_minute.get()
        alarm_sec=c_second.get()
        alarm_period=c_period.get()
        alarm_period=str(alarm_period).upper()
        
        now =datetime.now()
        
        hour =now.strftime("%I")
        minute=now.strftime("%M")
        second =now.strftime("%S")
        peroid=now.strftime("%p")
        
        if control==1:
            if alarm_period==peroid:
                if alarm_hour == hour:
                    if alarm_minute==minute:
                        if alarm_sec==second:
                            print("Time to take a break!")
                            sound_alarm()
        sleep(1)

mixer.init()

window.mainloop()