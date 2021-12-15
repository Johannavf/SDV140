 # Program name : Pet Sitter
 # Author : Johanna Velasquez


 # Main Function

from tkinter import *
import requests
from tkinter import messagebox, Tk
from functools import partial
from tkinter import font
from types import LambdaType
from PIL import ImageTk, Image


#Create a main window
root = Tk()
# Set a window tittle 
root.title("Welcome to Petsitter app")
# Set a window dimensions 
root.geometry('600x600')
root.configure(bg='lightblue')

background_image = ImageTk.PhotoImage(Image.open('pet.jpg' ))
background_label = Label(root, image=background_image)
background_label.place( relwidth=1, relheight=1)

font_style = ('verdana', 20)

label1 = Label(root, text='Hello Pet owners !', font=font_style).grid(row=0, padx=10, pady=10)

frame = Frame(root, bg='lightblue')
frame.place(relx=0.2, rely=0.1, relwidth=0.5, relheight=0.06)


#define main function 

def format_response(sitter):
	try:
		name = sitter['name']
		desc = sitter['city'][0]

		final_str = 'Name: %s \nCity: %s' % (name,desc)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_petsitter(city):

    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

    querystring = {"q":"pet sitters, city","pageNumber":"1","pageSize":"10","autoCorrect":"true"}
    # querystring = {"q":"pet sitters","pageNumber":"1","autoCorrect":"true"}

    headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "9dd6181a17mshafda4591933e5c8p1c4a0ejsn8d7b105f1d09"
    }

    response = requests.get( url, headers=headers, params=querystring)

    print(response.text)
    sitter = response.json()
    
    label['text'] = format_response(sitter)


 # function to verify the inputs 
def action(cp,vp):
    if cp.get()!=vp.get():
        messagebox.showerror("Error", "Password and confirm password entries does not match")
        return
    else:
        messagebox.showinfo("info", "Your account has been created successfully")

        

# create the labels:
zip_code_label= Label(frame,text=' Zip Code', font=('Aharoni',12), bg='lightblue').grid(column=0, row=1, padx=5, pady=5)
Sign_label= Label(root,text='Sign In', font=('verdana',18), bg='lightblue').grid(row=6, padx=5, pady=5)
first_name_label = Label(root, text= "First Name",).grid(row=8, padx=5, pady=5)
last_name_label = Label(root, text= "Last Name").grid(row=8, column=2, padx=5, pady=5)
user_name_label = Label(root, text= "User Name").grid(row=9, padx=5, pady=5)
choose_password_label= Label(root, text="Choose a password").grid(row=10, padx=5, pady=5)
confirm_password_label=Label(root, text= "Confirm password").grid(row=11, padx=5, pady=5)

#create variables
cp=StringVar()
vp=StringVar()

#create required textboxes:
zip_code_entry = Entry(bg='lightblue').grid(row=2, column=1, padx=5, pady=5)
# entry1.place(relwidth=0.65, relheight=1)
first_name_entry= Entry().grid(row=8, column=1,padx=5, pady=5)
last_name_entry= Entry().grid(row=8, column=3,padx=5, pady=5)
user_name_entry= Entry().grid(row=9, column=1,padx=5, pady=5)
choose_password_entry= Entry(root, textvariable=cp).grid(row=10, column=1,padx=5, pady=5)
confirm_password_entry=Entry(root, textvariable=vp).grid(row=11, column=1,padx=5, pady=5)

call_result = partial(action, cp, vp)

# def secondWindow():
#     root = Toplevel()
#     button = Button(root, text = "New Search button")
  
#     # label.pack()
#     buttonExample.pack()
# app = Tk()
# buttonExample = Button(app, text="Exit",command=secondWindow)
# buttonExample.pack()

# app.mainloop()

#CLASS function

def clicked():
    res= messagebox.askyesno('Did you find it','Would you like another search')
    

#Create the buttons 
sign_button = Button(root, text="More!", font=('verdana',14), bg='lightblue', command=clicked).grid(column=3, row=0, padx=5, pady=5)

button = Button(root,text='Find petsitter', font=5, bg='#ff8080', bd=1,command=lambda: get_petsitter(Entry)).grid(column=2,row=2)


Submit_button = Button(root, text="Submit", command=call_result).grid(column=1, row=12, padx=5,pady=5)


lower_frame = Frame(root, bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.3, anchor='n')

label = Label(lower_frame)
label.place(relwidth=1, relheight=1)
#loop
root.mainloop()
