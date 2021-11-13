import sqlite3
import tkinter
from tkinter import messagebox

# run the sql logic from sqlite3


def login():

    # connect to sqlite3
    db = sqlite3.connect('login.sqlite')
    # Create a user
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
    db.execute("INSERT INTO login(username, password) VALUES('zach', 'rochette')")
    #db.execute("INSERT INTO login(username, password) VALUES('ryan', 'reynolds')")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?",
                   (userinput.get(), pass_input.get()))
    row = cursor.fetchone()

    if row:
        messagebox.showinfo('info', 'login success')
    else:
        messagebox.showinfo('info', 'login failed')

    cursor.connection.commit()

    db.close()


# Design the login menu
main_window = tkinter.Tk()
main_window.title('Login')
main_window.geometry('400x300')
padd = 20
main_window['padx'] = padd
user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()
info_label = tkinter.Label(main_window, text='Login Application')
info_label.grid(row=0, column=0, pady=20)

info_user = tkinter.Label(main_window, text='Username')
info_user.grid(row=1, column=0)
userinput = tkinter.Entry(main_window, textvariable=user_input)
userinput.grid(row=1, column=1)

info_pass = tkinter.Label(main_window, text='Password')
info_pass.grid(row=2, column=0, pady=20)
passinput = tkinter.Entry(main_window, textvariable=pass_input, show='*')
passinput.grid(row=2, column=1)

login_btn = tkinter.Button(main_window, text='Login', command=login)
login_btn.grid(row=3, column=1)

main_window.mainloop()
