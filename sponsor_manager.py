"""
sponsor_manager.py
Author: Timothy Gist
Database Support: Maranda Dodgson
12/13/2023: The Sponsor Manager program is meant to be a utility to allow the club to manage sponsors.
functionality includes a login function to restrict access to the information contained herein.
The main program allows the user to view entries in the database in order to better manage
interaction with those sponsors.  See the 'about' function from the menubar for more detailed
information about the specific functions available.
There is also functionality that allows the user to add new sponsors and then return to the main program.
This is not intended to be the final version at this time, but rather a working prototype that can
allow for greater functionality in the future.
"""

import tkinter as tk
import tkinter.messagebox as tkmessagebox
from login_module_V3 import *
import sqlite3
from tkinter import ttk
from new_sponsor import *

login()


# Create base window
root = tk.Tk()
root.title('Sponsor Manager')
root.geometry('700x700')


def group_members():
    result = tkmessagebox.showinfo('Team Members',
                                   'Team Leader: Timothy Gist \nData Support: Maranda Dodgson', icon="info")


def about():
    about_page = tk.Tk()
    about_page.title("How to")
    about_page.geometry("800x800")
    about_page.configure(background='grey')
    panel = tk.Text(about_page, height=50, width=100)
    f = open("about.txt", "r")

    for line in f:
        panel.insert('end', line)

    f.close()

    panel.grid(row=0, column=0)
    # scrollbar = ttk.Scrollbar(panel, orient='vertical', command=panel.yview)
    # scrollbar.grid(row=0, column=1, sticky=tk.NS)
    # panel['yscrollcommand'] = scrollbar.set
    about_page.mainloop()


def goodbye():
    result = tkmessagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


root_menubar = tk.Menu(root)
root.config(menu=root_menubar)
file_menu = tk.Menu(root_menubar, tearoff=False)
file_menu.add_command(label='Team Members', command=group_members)
file_menu.add_command(label='About', command=about)
file_menu.add_command(label="Exit", command=goodbye)
root_menubar.add_cascade(label="File", menu=file_menu)
# Create frame to hold group member labels
frame = tk.LabelFrame(root, text="Group 1 Team Members", relief=tk.RAISED, padx=12, pady=12)
frame.grid(row=0, column=0, columnspan=5)


# Buttons for functionality
def sponsors():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM sponsors')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def membership():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Membership_level')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def member_level():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('SELECT Membership_level FROM Membership_level')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def sponsor_names():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('SELECT Sponsor_Name FROM sponsors')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        print_records += f'Sponsor Name: {str(record)} \n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def payment_received():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM sponsors WHERE Payment_Received = "Yes"')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def payment_not_received():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM sponsors WHERE Payment_Received = "No"')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def sponsor_level():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('''SELECT Sponsors.Sponsor_Name, Membership_level.Membership_level 
                    FROM Sponsors JOIN Sponsors.Membership_ID ON Membership_level.Membership_ID''')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def membership_cost():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('''SELECT Sponsors.Sponsor_Name, Membership_level.Membership_cost 
                        FROM Sponsors JOIN Membership_level.Membership_ID ON Sponsors.Membership_id''')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def membership_renewal():
    txt_edit.delete(1.0, tk.END)
    conn = sqlite3.connect('db_member.db')
    cur = conn.cursor()
    cur.execute('''SELECT Sponsors.Sponsor_Name, Membership_level.Membership_renewal, Membership_level.Membership_cost 
                            FROM Sponsors JOIN Membership_level.Membership_ID ON Sponsors.Membership_id''')
    records = cur.fetchall()
    print_records = ''
    for record in records:
        for item in record:
            print_records += str(item) + '\n'
        txt_edit.insert('end', f'{print_records} \n')
        print_records = ''

    conn.commit()
    conn.close()


def add_sponsor():
    new_sponsor()


# Create the text box for query output
txt_edit = tk.Text(root)
# Create the frame to hold the buttons
frm_buttons = tk.Frame(root, relief=tk.RAISED)
# Create the buttons
btn1 = tk.Button(frm_buttons, text='Sponsors', command=sponsors)
btn2 = tk.Button(frm_buttons, text="Membership", command=membership)
btn3 = tk.Button(frm_buttons, text='Membership Level', command=member_level)
btn4 = tk.Button(frm_buttons, text='Sponsor Names', command=sponsor_names)
btn5 = tk.Button(frm_buttons, text='Payment Received', command=payment_received)
btn6 = tk.Button(frm_buttons, text='Payment Not received', command=payment_not_received)
btn7 = tk.Button(frm_buttons, text='Sponsor Level', command=sponsor_level, state='disabled')
btn8 = tk.Button(frm_buttons, text='Membership Cost', command=membership_cost, state='disabled')
btn9 = tk.Button(frm_buttons, text='Membership Renewal', command=membership_renewal, state='disabled')
btn10 = tk.Button(frm_buttons, text='Add New Sponsor', command=add_sponsor)
# Place everything in the main window
btn1.grid(row=1, column=0, padx=5, pady=5)
btn2.grid(row=2, column=0, padx=5, pady=5)
btn3.grid(row=3, column=0, padx=5, pady=5)
btn4.grid(row=4, column=0, padx=5, pady=5)
btn5.grid(row=5, column=0, padx=5, pady=5)
btn6.grid(row=6, column=0, padx=5, pady=5)
btn7.grid(row=7, column=0, padx=5, pady=5)
btn8.grid(row=8, column=0, padx=5, pady=5)
btn9.grid(row=9, column=0, padx=5, pady=5)
btn10.grid(row=10, column=0, padx=5, pady=5)

frm_buttons.grid(row=1, column=0, sticky="ns")
txt_edit.grid(row=1, column=1, sticky="nsew")

root.mainloop()
