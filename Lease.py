import tkinter as tk
import mysql.connector
from tkinter import ttk
import numpy as np

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Nithish@2003",
database="dreamhouse"
)
def Display():
        mycursor = mydb.cursor() #spacing issue
        mycursor.execute("SELECT * FROM LeaseAgreement") #try cross join
        rows = mycursor.fetchall()
        root = tk.Tk()
        root.title("Lease Agreement Details:")
        tree = ttk.Treeview(root)
        tree["columns"] = ("LeaseID", "ClientID", "PropertyID","MonthlyRent", "paymentmethod" , "deposit", "RentStartDate", "RentEndDate")
        tree.heading("#0", text="Index")
        tree.heading("LeaseID", text="LeaseID")
        tree.heading("ClientID", text="ClientID")
        tree.heading("PropertyID", text="PropertyID")
        tree.heading("MonthlyRent", text="MonthlyRent")
        tree.heading("paymentmethod", text="paymentmethod")
        tree.heading("deposit", text="deposit")
        tree.heading("RentStartDate", text="RentStartDate")
        tree.heading("RentEndDate", text="RentEndDate")

        i = 1
        for row in rows:
            tree.insert(parent="", index=i, text=str(i), values=row)
            i += 1
       #tree.pack()
        tree.grid(row=1,column=1,padx=20,pady=20)


def submit():
        lid = lid_entry.get()
        cid = cid_entry.get()
        propid = property_entry.get()
        rent = rent_entry.get()
        pay = paym_entry.get()
        dep = dep_entry.get()
        rstart = rentstart_entry.get()
        rend = rentend_entry.get()
        
        mycursor = mydb.cursor()
        
        try:
            sql = "INSERT INTO LeaseAgreement(LeaseID, ClientID, PropertyID, MonthlyRent, paymentmethod, deposit, RentStartDate, RentEndDate) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (lid_entry.get(), cid_entry.get(), property_entry.get(), rent_entry.get(), paym_entry.get(), dep_entry.get(), rentstart_entry.get(), rentend_entry.get())
            if lid_entry.get() == '' or cid_entry.get() == '' or property_entry.get() == '' or rent_entry.get() == ''or paym_entry.get() == '' or dep_entry.get() == '' or rentstart_entry.get() == '' or rentend_entry.get() == '' :
                results_label.config(text="Error: Dream home features not saved successfully, Enter values", foreground = "red")
            else:
                mycursor.execute(sql, val)
                if mycursor.rowcount > 0:
                    results_label.config(text="Dream home features saved successfully.", foreground = "black")
                    mydb.commit()
                else:
                    results_label.config(text="Error: Dream home features not saved successfully", foreground = "red")
               
        except mysql.connector.IntegrityError as e:
            print("Query was not successful: {}".format(e))

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

def delete():
    lease_id = lid_entry.get()

    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM LeaseAgreement WHERE LeaseId = %s"
        val = (lease_id,)
        if lid_entry.get() == '' or cid_entry.get() == '' or property_entry.get() == '' or rent_entry.get() == ''or paym_entry.get() == '' or dep_entry.get() == '' or rentstart_entry.get() == '' or rentend_entry.get() == '' :
            results_label.config(text="Error: Enter Values", foreground = "red")
        else:
            mycursor.execute(sql, val)
            if mycursor.rowcount > 0:
                results_label.config(text="Deleted successdully.", foreground = "black")
                mydb.commit()
            else:
                results_label.config(text="Error: Cannot be Deleted", foreground = "red")
            
    except mysql.connector.IntegrityError as e:
        print("Query was not successful: {}".format(e))

    except mysql.connector.Error as error:
        print("Failed to delete into MySQL table {}".format(error))


def update():
        lid = lid_entry.get()
        cid = cid_entry.get()
        propid = property_entry.get()
        rent = rent_entry.get()
        pay = paym_entry.get()
        dep = dep_entry.get()
        rstart = rentstart_entry.get()
        rend = rentend_entry.get()
        try:
            mycursor = mydb.cursor()
            sql = "UPDATE LeaseAgreement SET clientid = %s, propertyId = %s, MonthlyRent = %s, paymentmethod = %s, deposit = %s, RentStartDate = %s, RentEndDate = %s WHERE LeaseId = %s"
            val = (lid, cid, propid, rent, pay, dep, rstart, rend)
            if lid_entry.get() == '' or cid_entry.get() == '' or property_entry.get() == '' or rent_entry.get() == ''or paym_entry.get() == '' or dep_entry.get() == '' or rentstart_entry.get() == '' or rentend_entry.get() == '' :
               results_label.config(text="Error: Enter Values", foreground = "red")
            else:
                mycursor.execute(sql, val)
                if mycursor.rowcount > 0:
                    results_label.config(text="Deleted successdully.", foreground = "black")
                    mydb.commit()
                else:
                    results_label.config(text="Error: Cannot be Deleted", foreground = "red")
               
        except mysql.connector.IntegrityError as e:
            print("Query was not successful: {}".format(e))

        except mysql.connector.Error as error:
            print("Failed to update into MySQL table {}".format(error))
        

   

root = tk.Tk()
root.title("Property Registration")
root.configure(background="#6495ed")

lid_label = tk.Label(root, text="Lease ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
lid_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
lid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
lid_entry.grid(row = 0, column=1, padx=5, pady=5)
lid_label.config(background="#6495ed")

cid_label = tk.Label(root, text="Client ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cid_label.grid(row = 1, column=0, padx=5, pady=5, sticky="w")
cid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cid_entry.grid(row = 1, column=1, padx=5, pady=5, sticky="w")
cid_label.config(background="#6495ed")

property_label = tk.Label(root, text="Property ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
property_label.grid(row = 0, column=3, padx=5, pady=5, sticky="w")
property_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
property_entry.grid(row = 0, column=4, padx=5, pady=5)
property_label.config(background="#6495ed")

en_label = tk.Label(root, text="Enter Payment Details:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
property_label.grid(row = 2, column=0, padx=5, pady=5, sticky="w")
en_label.config(background="#6495ed")

rent_label = tk.Label(root, text="Monthly Rent:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
rent_label.grid(row = 3, column=0, padx=5, pady=5, sticky="w")
rent_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
rent_entry.grid(row = 3, column=1, padx=5, pady=5)
rent_label.config(background="#6495ed")

paym_label = tk.Label(root, text="Payment Method:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
paym_label.grid(row = 4, column=0, padx=5, pady=5, sticky="w")
paym_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
paym_entry.grid(row = 4, column=1, padx=5, pady=5)
paym_label.config(background="#6495ed")

dep_label = tk.Label(root, text="Desposit Paid(T/F):", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
dep_label.grid(row = 5, column=0, padx=5, pady=5, sticky="w")
dep_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
dep_entry.grid(row = 5, column=1, padx=5, pady=5)
dep_label.config(background="#6495ed")

rentstart_label = tk.Label(root, text="Rent Start Date:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
rentstart_label.grid(row = 3, column=3, padx=5, pady=5, sticky="w")
rentstart_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
rentstart_entry.grid(row = 3, column=4, padx=5, pady=5)
rentstart_label.config(background="#6495ed")

rentend_label = tk.Label(root, text="Rent End Date:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
rentend_label.grid(row = 4, column=0, padx=5, pady=5, sticky="w")
rentend_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
rentend_entry.grid(row = 4, column=1, padx=5, pady=5)
rentend_label.config(background="#6495ed")

                   
style = ttk.Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")

submit_button = ttk.Button(root, text="Submit", style="Custom.TButton")
submit_button.grid(row = 6, column=1, padx=20, pady=20)

display_button = ttk.Button(root, text="Display", style="Custom.TButton")
display_button.grid(row = 6, column=3, padx=20, pady=20)

delete_button = ttk.Button(root, text="Delete", style="Custom.TButton")
delete_button.grid(row = 6, column=2, padx=20, pady=20)

update_button = ttk.Button(root, text="Update", style="Custom.TButton")
update_button.grid(row = 6, column=4, padx=20, pady=20)

results_label = tk.Label(root, text="", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
results_label.grid(row = 7, column=2, padx=5, pady=5)
results_label.config(background = "#6495ed")

submit_button.config(command=submit)
display_button.config(command=Display)
delete_button.config(command=delete)
update_button.config(command=update)

root.mainloop()
