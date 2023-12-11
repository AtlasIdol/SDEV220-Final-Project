""" login_module_V3.py
Author: Timothy Gist
12/1/2023: This is a module that provides a login function inside a TKinter GUI.
12/3/2023: The original version of this module did not clear the login form from the screen
and did not return control to the calling program.  I fixed that by adding the
.destroy() method and inserting the return keyword in the successful login blocks.
12/8/2023: Added database functionality to the login module.
"""

def login():
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
    from tkinter import StringVar
    import sqlite3

    my_font = ("Lucida Console", 14)

    root = tk.Tk()
    root.title("Sponsor Manager Login")

    width = 640
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    def database():
        global conn, cursor
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS 'users' ("
                       "user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")

    username = StringVar()
    password = StringVar()

    def loginform():
        global LoginFrame, lbl_result1
        LoginFrame = tk.Frame(root)
        LoginFrame.pack(side=tk.TOP, pady=80)
        lbl_username = tk.Label(LoginFrame, text="Username:", font=my_font, bd=18)
        lbl_username.grid(row=1)
        lbl_password = tk.Label(LoginFrame, text="Password:", font=my_font, bd=18)
        lbl_password.grid(row=2)
        lbl_result1 = tk.Label(LoginFrame, text="", font=my_font)
        lbl_result1.grid(row=3, columnspan=2)
        ent_username = tk.Entry(LoginFrame, font=my_font, textvariable=username, width=15)
        ent_username.grid(row=1, column=1)
        ent_password = tk.Entry(LoginFrame, font=my_font, textvariable=password, width=15, show="*")
        ent_password.grid(row=2, column=1)
        btn_login = tk.Button(LoginFrame, text="Login", font=my_font, width=35, command=login_now)
        btn_login.grid(row=4, columnspan=2, pady=20)
        # lbl_register = tk.Label(LoginFrame, text="Register", fg="Blue", font=my_font)
        # lbl_register.grid(row=0, sticky=tk.W)
        # lbl_register.bind('<Button-1>', toggletoregister)

    # def registerform():
    #     global RegisterFrame, lbl_result2
    #     RegisterFrame = tk.Frame(root)
    #     RegisterFrame.pack(side=tk.TOP, pady=40)
    #     lbl_username = tk.Label(RegisterFrame, text="Username:", font=my_font, bd=18)
    #     lbl_username.grid(row=1)
    #     lbl_password = tk.Label(RegisterFrame, text="Password:", font=my_font, bd=18)
    #     lbl_password.grid(row=2)
    #     lbl_result2 = tk.Label(RegisterFrame, text="", font=my_font)
    #     lbl_result2.grid(row=5, columnspan=2)
    #     ent_username = tk.Entry(RegisterFrame, font=my_font, width=15)
    #     ent_username.grid(row=1, column=1)
    #     ent_password = tk.Entry(RegisterFrame, font=my_font, width=15, show="*")
    #     ent_password.grid(row=2, column=1)
    #     lbl_result2 = tk.Label(RegisterFrame, text="", font=my_font)
    #     lbl_result2.grid(row=5, columnspan=2)
    #     ent_username = tk.Entry(RegisterFrame, font=my_font, textvariable=username, width=15)
    #     ent_username.grid(row=1, column=1)
    #     ent_password = tk.Entry(RegisterFrame, font=my_font, textvariable=password, width=15, show="*")
    #     ent_password.grid(row=2, column=1)
    #     btn_login = tk.Button(RegisterFrame, text="Register", font=my_font, width=35, command=register)
    #     btn_login.grid(row=6, columnspan=2, pady=20)
    #     lbl_login = tk.Label(RegisterFrame, text="Login", fg="Blue", font=my_font)
    #     lbl_login.grid(row=0, sticky=tk.W)
    #     lbl_login.bind('<Button-1>', toggletologin)

    # =======================================METHODS=======================================
    def goodbye():
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    # def toggletologin(event=None):
    #     RegisterFrame.destroy()
    #     loginform()
    #
    # def toggletoregister(event=None):
    #     LoginFrame.destroy()
    #     registerform()
    #
    # def register():
    #     database()
    #     if username.get == "" or password.get() == "":
    #         lbl_result2.config(text="Please complete the required field!", fg="orange")
    #     else:
    #         cursor.execute("SELECT * FROM `users` WHERE `username` = ?", (username.get(),))
    #         if cursor.fetchone() is not None:
    #             lbl_result2.config(text="Username is already taken", fg="red")
    #         else:
    #             cursor.execute("INSERT INTO `users` (username, password) VALUES(?, ?)",
    #                            (str(username.get()), str(password.get())))
    #             conn.commit()
    #             username.set("")
    #             password.set("")
    #             lbl_result2.config(text="Successfully Created!", fg="black")
    #         cursor.close()
    #         conn.close()

    def login_now():
        database()
        if username.get == "" or password.get() == "":
            lbl_result1.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `users` WHERE `username` = ? and `password` = ?",
                           (username.get(), password.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="Login Success!", fg="blue")
            root.destroy()
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")

    loginform()

    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=goodbye)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    root.mainloop()

if __name__ == '__main__':
    login()
