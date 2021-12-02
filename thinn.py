from tkinter import * 
# from tkinter.ttk import *
#Write a GUI program to will help users find pet sitters 
# import tkinter
# from breezypythongui import EasyFrame 
from tkinter import PhotoImage
import tkinter
from tkinter.font import *

#   class ImageDemo(EasyFrame):
#       def __init__(self):
#           EasyFrame.__init__(self, title='Image Demo')
#           self.__setResizable(False);
#           imageLabel= self.addLabel  
# Creating Main window of  the application 


root = Tk()
  
# giving title to the main window
root.title("Petsitter")
Canvas= tkinter.Canvas(root, width = 400, height = 350)
Canvas.pack()

  
entry = tkinter.Entry (root) 
Canvas.create_window(200, 140, window=entry)

img= tkinter.PhotoImage(file="pet.png")
lbl_img= tkinter.label(root,image=img)
lbl_img.pack()
# Label is what output will be show on the window 
label1 = tkinter.Label(root, text='Hello Pet owners !')
label1.pack()
Canvas.create_window(200, 100, window=label1)


  
# calling mainloop method which is used

# when your application is ready to run
# and it tells the code to keep displaying 

root.mainloop()