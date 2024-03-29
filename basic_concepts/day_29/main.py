from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json 

# ----------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    
    letters = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']
        
    pw_letters = [choice(letters) for _ in range(randint(8,10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        
    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password) 
    # Add newly saved password to clipboard for immediate use
    pyperclip.copy(password) 
# ----------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': password,
        }
    }                                  
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="ERROR!",message=f"Please ensure all fields are complely filled out.")
    else:
        try:# Try reading file if it exists
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            #Create and open newly created filed with write
            with open("data.json", "w") as data_file:
                # Save new data to new file
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear fields    
            website_entry.delete(0, END)
            password_entry.delete(0, END)
     
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passwod Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0, "example@email.com")
password_entry =  Entry(width=19)
password_entry.grid(row=3,column=1)

#Button
generate_password = Button(text="Generate Password", width=12, command=generate_passwd)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()