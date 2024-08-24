import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageSequence
import requests
from io import BytesIO
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
import playsound

root = Tk()
root.title("|JARVIS| ---> Jarvis to Speech Converter")
root.geometry("1000x580+200+80")  # Corrected geometry syntax
root.resizable(True, True)
root.config(bg="#000435")

url ="https://media3.giphy.com/media/wkSyGueYTnk40/giphy.webp?cid=790b7611bpqk0l5jswt0ca4ebvow1c2ab2v6phaymg09fbux&ep=v1_gifs_search&rid=giphy.webp&ct=g"
response = requests.get(url)
image_data = response.content

# Load the image
image = Image.open(BytesIO(image_data))
frames = [frame.copy() for frame in ImageSequence.Iterator(image)]
photo = [ImageTk.PhotoImage(frame) for frame in frames]

# Create a label to display the image
jarvis_logo_label = tk.Label(root, bg="#000000", borderwidth=0)
jarvis_logo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the image at the bottom right corner

def update(ind):
    frame = photo[ind]
    jarvis_logo_label.config(image=frame)
    ind += 1
    if ind == len(photo):
       ind = 0
    root.after(100, update, ind)

update(0)

font = ('TimesNewroman', 16, 'bold')
title = Label(root, text='|JARVIS| TEXT TO SPEECH CONVERTER')
title.config(bg='dark goldenrod', fg='Red')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)


tts = pyttsx3.init()

def speaknow():
    text = text_box.get(1.0, END)
    gen = genbox.get()
    speed = speedbox.get()
    voices = tts.getProperty('voices')

    def setvoice():
        if(gen == 'MALE'):
            tts.setProperty('voice', voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else:
            tts.setProperty('voice', voices[1].id)
            tts.say(text)
            tts.runAndWait()

    if(text):
        if(speed == 'TURBO'):
            tts.setProperty('rate', 250)
            setvoice()
        elif(speed == 'AVERAGE'):
            tts.setProperty('rate', 150)
            setvoice()
        else:
            tts.setProperty('rate', 60)
            setvoice()  

logimage = PhotoImage(file = "E:/iRON JARVIS.png")
root.iconphoto(False, logimage)
#root.mainloop()

text_box = Text(root, font="TimesNewroman 15" , bg="#000435", fg="white", relief= GROOVE, wrap=WORD, bd=5)
text_box.place(x=10, y=100, width=370, height=140)

genbox = Combobox(root, values=['MALE','FEMALE'], font="TimesNewroman 10", state='r', width=12)
genbox.place(x=240, y=400)
genbox.set('MALE')  # Set the default value

speedbox=Combobox(root, values=['TURBO', 'AVERAGE', 'UNRUSHED'], font="TimesNewroman 10", state='r', width=12)
speedbox.place(x=931, y=400)
speedbox.set('AVERAGE')

Label(root, text="Select Voice", font="TimesNewroman 12 bold", bg="#F7AC40", fg="#111").place(x=245, y=370)
Label(root, text="Select Speed", font="TimesNewroman 12 bold", bg="#F7AC40", fg="#111").place(x=931, y=370)

playbutton=PhotoImage(file="E:/icons8-play-button-48.png")
playbtn=Button(root, text="Play", fg='white', compound=LEFT, image=playbutton, bg="#000435", height=36, width=90, font="TimesNewroman", borderwidth="0.1c", command=speaknow)
playbtn.place(x=600, y=580)

root.mainloop()