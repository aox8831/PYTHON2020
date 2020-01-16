import time
from tkinter import *

root = Tk()
root.title("Začetek")
root.geometry("300x100+400+400")
label = Label(root, text = "Ali je temno zunaj?",width=20,font=("arial",10,"bold"))
label.pack()


def alijetemno():
    root.destroy()
    odgovor1 = Tk()
    odgovor1.title("Odgovor")
    odgovor1.geometry("300x100+400+400")
    label2 = Label(odgovor1,width=20,font=("arial",10,"bold")) 
    label2.pack()
    dark = {

    1: 16,
    2: 17,
    3: 18,
    4: 19,
    5: 19,
    6: 20,
    7: 20,
    8: 19,
    9: 18,
    10: 17,
    11: 16,
    12: 16
        }

    light = {

    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 4,
    7: 4,
    8: 5,
    9: 6,
    10: 6,
    11: 7,
    12: 8
      }

   
    time_now = time.localtime()

    if time_now.tm_hour >=dark[time_now.tm_mon] or time_now.tm_hour < light[time_now.tm_mon]:
     print("Ja")
     label2.configure(width=20,font=("arial",10,"bold"),fg="white",bg="black",text="Ja")

    else:
     print("Ne")
     label2.configure(width=20,font=("arial",10,"bold"),text="Ne")
   

button = Button(root, text="Odgovor",width=15,bg="black",fg="white",command = alijetemno)
button.pack()


mainloop()
