#Write a GUI program to will help users find pet sitters 

import tkinter as tk


HEIGHT = 400
WIDTH = 600

def buttonfunction(entry):
    print("this is a entry")

root = tk.Tk()
root.title("Petsitter")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
 


# background = tk.PhotoImage(file='pet.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#ff8080', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry1 = tk.Entry(frame, text='Introduce your zip code', font=40)
entry1.place(relwidth=0.65, relheight=1)

# entry2 = tk.Entry(frame, font=40)
# entry2.place(relwidth=1, relheight=0.1)

button1 = tk.Button(frame, text="Find petsitter", font=10, bg='#ff8080', bd=1, command=lambda: buttonfunction(entry1.get()))
button1.place(relx=0.7, relheight=1, relwidth=0.2)

# button2 = tk.Button(frame, text="Find petsitter", font=10, bg='#ff8080', bd=1)

# button2.place(relx=0.7, relheight=1, relwidth=0.2)



# Label is what output will be show on the window 
label1 = tk.Label(root, text='Hello Pet owners !', font=50,bd=20)
label1.pack()
label1.place(relx=0.4, relwidth=0.3, relheight=0.1)

# label = tk.Label(lower_frame)
# label.place(relwidth=1, relheight=1)

root.mainloop()
