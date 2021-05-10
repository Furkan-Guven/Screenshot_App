# -*- coding: utf-8 -*-
"""
VS CODE 
@FURKAN_GÜVEN
This is a temporary script file.
"""
from PIL import Image, ImageGrab
from tkinter import*


i = 0

def ekrangoruntu():
    global i
    c = str(i)
    a = c + ".jpg"
    EkranGoruntusu = ImageGrab.grab()
    EkranGoruntusu.save(a,"JPEG")
    i += 1
    



pencere = Tk()
pencere.title("Ekran Görüntüsü Alma Programı")
pencere.geometry("200x80")
button = Button(text="SS AL", font="Verdana 32 bold italic",bg= "lightyellow", height = 80, width = 350, command = ekrangoruntu)
button.pack()
mainloop()
