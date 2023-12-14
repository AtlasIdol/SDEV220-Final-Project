"""
new_sponsor.py
Author: Timothy Gist
Database Support: Maranda Dodgson
12/13/2023: This is a module that provides functionality to add records to the Sponsors table of the database.
"""


def new_sponsor():
    import tkinter as tk
    import sqlite3

    root = tk.Tk()
    root.title('Add New Sponsor')
    root.geometry('400x300')

    # conn = sqlite3.connect('address_book.db')
    # cur = conn.cursor()

    # cur.execute('''
    #             CREATE TABLE addresses
    #             (first_name text,
    #             last_name text,
    #             address text,
    #             city text,
    #             state text,
    #             zipcode integer
    #             )''')

    def submit():
        conn = sqlite3.connect('db_member.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Sponsors VALUES (:sponsor_id, :name, :address, :city, :phone_number, :membership_id,
                     :payment_received, :contact_fname, :contact_lname)''',
                    {
                        'sponsor_id': sponsor_id.get(),
                        'name': name.get(),
                        'address': address.get(),
                        'city': city.get(),
                        'phone_number': phone_number.get(),
                        'membership_id': membership_id.get(),
                        'payment_received': payment_received.get(),
                        'contact_fname': contact_fname.get(),
                        'contact_lname': contact_lname.get()
                    })
        sponsor_id.delete(0, tk.END)
        name.delete(0, tk.END)
        address.delete(0, tk.END)
        city.delete(0, tk.END)
        phone_number.delete(0, tk.END)
        membership_id.delete(0, tk.END)
        payment_received.delete(0, tk.END)
        contact_fname.delete(0, tk.END)
        contact_lname.delete(0, tk.END)

        conn.commit()
        conn.close()

    def query():
        root.destroy()

    sponsor_id = tk.Entry(root, width=30)
    sponsor_id.grid(row=0, column=1, padx=20)
    name = tk.Entry(root, width=30)
    name.grid(row=1, column=1, padx=20)
    address = tk.Entry(root, width=30)
    address.grid(row=2, column=1, padx=20)
    city = tk.Entry(root, width=30)
    city.grid(row=3, column=1, padx=20)
    phone_number = tk.Entry(root, width=30)
    phone_number.grid(row=4, column=1, padx=20)
    membership_id = tk.Entry(root, width=30)
    membership_id.grid(row=5, column=1, padx=20)
    payment_received = tk.Entry(root, width=30)
    payment_received.grid(row=6, column=1, padx=20)
    contact_fname = tk.Entry(root, width=30)
    contact_fname.grid(row=7, column=1, padx=20)
    contact_lname = tk.Entry(root, width=30)
    contact_lname.grid(row=8, column=1, padx=20)

    sponsor_id_label = tk.Label(root, text='Sponsor_ID')
    sponsor_id_label.grid(row=0, column=0, padx=20)
    name_label = tk.Label(root, text='Name:')
    name_label.grid(row=1, column=0, padx=20)
    address_label = tk.Label(root, text='Address:')
    address_label.grid(row=2, column=0, padx=20)
    city_label = tk.Label(root, text='City:')
    city_label.grid(row=3, column=0, padx=20)
    phone_number_label = tk.Label(root, text='Phone Number:')
    phone_number_label.grid(row=4, column=0, padx=20)
    membership_id_label = tk.Label(root, text='Membership ID:')
    membership_id_label.grid(row=5, column=0, padx=20)
    payment_received_label = tk.Label(root, text='Payment Received?:')
    payment_received_label.grid(row=6, column=0, padx=20)
    contact_fname_label = tk.Label(root, text='Contact First Name')
    contact_fname_label.grid(row=7, column=0, padx=20)
    contact_lname_label = tk.Label(root, text='Contact Last Name')
    contact_lname_label.grid(row=8, column=0, padx=20)

    submit_btn = tk.Button(root, text='Add Record to Database', command=submit)
    submit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    query_btn = tk.Button(root, text='Return to Main Program', command=query)
    query_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    root.mainloop()


if __name__ == '__main__':
    new_sponsor()
