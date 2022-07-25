from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def login_func():
    email=email_input.get()
    password=password_input.get()

    if email == 'hey.omkar.katare@gmail.com' and password=='Tendulakr@10':
        messagebox.showinfo('Yey!, Login successful')
    else:
        messagebox.showinfo('Error','Login Failed')


root = Tk()
root.title('Login Form')
root.iconbitmap('1b9df43e6aa2d258840a0da1d127b631.ico')
# root.minsize(500,500)
# root.maxsize(1000,1000)
root.geometry('400x500')
root.configure(background='#0096DC')
img=Image.open(fp='Screenshot (178).png')
resized_img=img.resize((100,100))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))
text_label=Label(root,text="Omkar's~ APP",fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label=Label(root,text="Enter Email",fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',18))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text="Enter Password",fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',18))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))


login_btn=Button(root,text="Login",bg='white',fg='black',width=20,height=2,command=login_func)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',8))


root.mainloop()