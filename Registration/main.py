from tkinter import *
import os



def login_sucess():
    screen3 = Toplevel(screen)
    screen3.title('sucess')
    screen3.geometry('150x100')
    Label(screen3,text = 'Login sucess').pack()
    Button(screen3,text = 'ok', command = screen3.destroy).pack()
def password_not_reco():
    screen4 = Toplevel(screen)
    screen4.title('Invalid Password')
    screen4.geometry('150x100')
    Label(screen4, text='Invalid password').pack()
    Button(screen4, text='ok', command=screen4.destroy).pack()
def usr_not_found():
    screen5 = Toplevel(screen)
    screen5.title('invalid user')
    screen5.geometry('150x100')
    Label(screen5, text='user not found').pack()
    Button(screen5, text='ok', command=screen5.destroy).pack()
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    for i in list_of_files:
        print(i)
    if username1 in list_of_files:
        file1 = open(username1,'r')
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_reco()
    else:
        usr_not_found()



def Register_usr():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info,'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text = 'Registration sucessful',fg = 'green',font = ('calibri',13)).pack()


def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Registration')
    screen1.geometry('300x250')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()




    Label(screen1, text='please enter details below ').pack()
    Label(screen1,text='username * ').pack()
    username_entry = Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text='password * ').pack()
    password_entry =  Entry(screen1,textvariable=password)
    password_entry.pack()
    Button(screen1,text = 'Register',width = '10',height = '1',command = Register_usr).pack()


def Login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title('login')
    screen2.geometry('300x250')
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    Label(screen2, text='please enter details below to login').pack()

    Label(screen2, text='username * ').pack()
    username_entry1 = Entry(screen2,textvariable = username_verify)
    username_entry1.pack()

    Label(screen2, text='password * ').pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()

    Button(screen2,text = 'login',width = '10',height = '1',command = login_verify).pack()
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title("Notes 1.0")
    Label(text = '').pack()
    Label(text = '').pack()
    Button(text = 'Login',height = '2',width = '30' , command = Login).pack()
    Button(text = 'Register',height = '2',width = '30',command = Register).pack()
    screen.mainloop()
main_screen()

