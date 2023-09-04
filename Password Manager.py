from tkinter import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []
  password_lettr=[random.choice(letters) for i in range(nr_letters)]
  print(password_lettr)
  password_num=[random.choice(numbers) for j in range(nr_symbols)]
  print(password_num)
  password_sym=[random.choice(symbols) for k in range(nr_symbols)]
  print(password_sym)
  password_list=password_lettr + password_num +password_sym 
  random.shuffle(password_list)
  print(f"Your password is: {password_list}")
  password=""
  for i in password_list:
    password +=i
  pw.insert(0, f"{password}")
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
data=open('Program Data.txt',"a")
def save_password():
    web=website.get()
    email=mail.get()
    password=pw.get()
    if len(email) and len(password) !=0:
     is_ok=messagebox.askokcancel(title='f{web}',message=f"These are the details entered: \n {email} \n{password} \n Is it okay to save?")
     if is_ok:
       #messagebox.showinfo(title='Title', message='Message')
       data.writelines([ f'{web} |'  ,f'{email}|',f'{password} \n'])
       data.close()
       website.delete(0, END)
       pw.delete(0, END)
       
    else:
       messagebox.showwarning(title='Error', message="Please don't have any fields empty") 

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)
canvas=Canvas(width=200, height=200)

img=PhotoImage(file="C:\\Users\\FACULTY OFFICIAL\\Downloads\\password-manager-start\\logo.png")
canvas.create_image(100,100,image=img)
#canvas.create_line(20,100, 220,100)
#canvas.create_rectangle(20,180,180,0)
canvas.grid(row=0,column=1)


field1=Label(text='Website:')
field1.grid(row=1,column=0)
field2=Label(text='Email/Username:')
field2.grid(row=2,column=0)
field3=Label(text='Password:')
field3.grid(row=3,column=0)

website=Entry(width=35)
website.grid(row=1,column=1,columnspan=2)
website.focus()
mail=Entry(width=35)
mail.grid(row=2,column=1,columnspan=2)
mail.insert(0, "ewez@gmail.com")
pw=Entry(width=17)
pw.grid(row=3,column=1)

generate_pass=Button(text='Generate Password',width=14, command= generate_password)
generate_pass.grid(row=3,column=2)
add=Button(text='Add',width=30,command=save_password)
add.grid(row=4, column=1,columnspan=2)


window.mainloop()