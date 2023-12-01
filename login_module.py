# login_module.py
'''This is a module that provides a login function inside a TKinter GUI.'''


def login():
    import tkinter as tk
    from tkinter import messagebox
    import sqlite3

    login_window = tk.Tk()
    login_window.geometry('350x500')
    login_window.title('L O G I N')
    login_window.resizable(0, 0)

    j = 0
    r = 0
    for i in range(100):
        c = str(222222 + r)
        tk.Frame(login_window, width=10, height=500, bg='#' + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    tk.Frame(login_window, width=250, height=400, bg='white').place(x=50, y=50)

    # username label
    user_label = tk.Label(login_window, text='Username', bg='white')
    my_font = ('Lucida Console', 14)  # font, text size
    user_label.config(font=my_font)
    user_label.place(x=80, y=200)

    # username entry
    user_entry = tk.Entry(login_window, width=20, border=0)
    user_entry.config(font=my_font)
    user_entry.place(x=80, y=230)

    # password label
    pass_label = tk.Label(login_window, text='Password', bg='white')
    pass_label.config(font=my_font)
    pass_label.place(x=80, y=280)

    # password entry
    pass_entry = tk.Entry(login_window, width=20, border=0)
    pass_entry.config(font=my_font)
    pass_entry.place(x=80, y=310)

    tk.Frame(login_window, width=180, height=2, bg='#141414').place(x=80, y=250)
    tk.Frame(login_window, width=180, height=2, bg='#141414').place(x=80, y=330)

    def cmd():
        if user_entry.get() == 'Timothy' and pass_entry.get() == 'timothy':
            messagebox.showinfo('LOGIN SUCCESSFUL', f'          WELCOME {user_entry.get()}!         ')
        elif user_entry.get() == 'Mandy' and pass_entry.get() == 'mandy':
            messagebox.showinfo('LOGIN SUCCESSFUL', f'          WELCOME {user_entry.get()}!         ')
        elif user_entry.get() == 'Ethan' and pass_entry.get() == 'ethan':
            messagebox.showinfo('LOGIN SUCCESSFUL', f'          WELCOME {user_entry.get()}!         ')
        else:
            messagebox.showinfo('LOGIN FAILED', '          PLEASE TRY AGAIN          ')

    login_button = tk.Button(
        login_window, width=20, height=2, fg='white', bg='#994422', border=0, command=cmd, text='L O G I N'
    )
    login_button.place(x=100, y=370)

    login_window.mainloop()
    return
