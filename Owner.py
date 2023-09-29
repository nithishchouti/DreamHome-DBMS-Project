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
        mycursor.execute("SELECT * FROM Owner") #try cross join
        rows = mycursor.fetchall()
        root = tk.Tk()
        root.title("Owner Details:")
        tree = ttk.Treeview(root)
        tree["columns"] = ("ownerId", "Name", "locality","city", "state" , "country")
        #tree.heading("#0", text="Index")
        tree.heading("ownerId", text="OwnerID")
        tree.heading("Name", text="Name")
        tree.heading("locality", text="Locality")
        tree.heading("city", text="City")
        tree.heading("state", text="State")
        tree.heading("country", text="Country")

        i = 1
        for row in rows:
            tree.insert(parent="", index=i, text=str(i), values=row)
            i += 1
       #tree.pack()
        tree.grid(row=1,column=1,padx=20,pady=20)


def submit():
        owner_id = owner_entry.get()
        name = name_entry.get()
        locality = locality_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        country = country_entry.get()

        mycursor = mydb.cursor()
        try:
            sql = "INSERT INTO Owner(OwnerID, Name, locality, city, state, country) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (owner_id, name, locality, city, state, country)
            if owner_entry.get() == '' or name_entry.get() == ''  or locality_entry.get() == ''  or city_entry.get() == ''  or state_entry.get() == ''  or country_entry.get() == '' :
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
    ownerId = owner_entry.get()
    
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM Owner WHERE ownerId = %s"
        val = (ownerId,)
        if owner_entry.get() == '' or name_entry.get() == ''  or locality_entry.get() == ''  or city_entry.get() == ''  or state_entry.get() == ''  or country_entry.get() == '' :               
            mycursor.execute(sql, val)
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
    
    owner_id = owner_entry.get()
    name = name_entry.get()
    locality = locality_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    country = country_entry.get()

    try:
            mycursor = mydb.cursor()
            sql = "UPDATE Owner SET Name = %s, locality = %s, city = %s, state = %s, country = %s WHERE ownerId = %s"
            val = (name, locality, city, state, country, owner_id)
            if owner_entry.get() == '' or name_entry.get() == ''  or locality_entry.get() == ''  or city_entry.get() == ''  or state_entry.get() == ''  or country_entry.get() == '' :               
                results_label.config(text="Error: Enter Values", foreground = "red")
            else:
                mycursor.execute(sql, val)
                if mycursor.rowcount > 0:
                    results_label.config(text="Dream home features updated successfully.", foreground = "black")
                    mydb.commit()
                else:
                    results_label.config(text="Error: Cannot be updated", foreground = "red")
               
    except mysql.connector.IntegrityError as e:
        print("Query was not successful: {}".format(e))

    except mysql.connector.Error as error:
        print("Failed to update into MySQL table {}".format(error))


root = tk.Tk()
root.title("Property Registration")
root.configure(background="#6495ed")

owner_label = tk.Label(root, text="Owner ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
owner_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
owner_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
owner_entry.grid(row = 0, column=1, padx=5, pady=5)
owner_label.config(background="#6495ed")

name_label = tk.Label(root, text="Name:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
name_label.grid(row = 0, column=3, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
name_entry.grid(row = 0, column=4, padx=5, pady=5)
name_label.config(background="#6495ed")

locality_label = tk.Label(root, text="Locality:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
locality_label.grid(row = 1, column=0, padx=5, pady=5, sticky="w")
locality_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
locality_entry.grid(row = 1, column=1, padx=5, pady=5)
locality_label.config(background="#6495ed")

city_label = tk.Label(root, text="City:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
city_label.grid(row = 1, column=3, padx=5, pady=5, sticky="w")
city_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
city_entry.grid(row = 1, column=4, padx=5, pady=5)
city_label.config(background="#6495ed")

state_label = tk.Label(root, text="State:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
state_label.grid(row = 2, column=0, padx=5, pady=5, sticky="w")
state_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
state_entry.grid(row = 2, column=1, padx=5, pady=5)
state_label.config(background="#6495ed")

country_label = tk.Label(root, text="Country:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
country_label.grid(row = 2, column=3, padx=5, pady=5, sticky="w")
country_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
country_entry.grid(row = 2, column=4, padx=5, pady=5)
country_label.config(background="#6495ed")

tele_label = tk.Label(root, text="Branch Tele Number:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
tele_label.grid(row = 3, column=0, padx=5, pady=5, sticky="w")
tele_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
tele_entry.grid(row = 3, column=1, padx=5, pady=5)
tele_label.config(background="#6495ed")

style = ttk.Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")

submit_button = ttk.Button(root, text="Submit", style="Custom.TButton")
submit_button.grid(row = 5, column=1, padx=20, pady=20)

display_button = ttk.Button(root, text="Display", style="Custom.TButton")
display_button.grid(row = 5, column=3, padx=20, pady=20)

delete_button = ttk.Button(root, text="Delete", style="Custom.TButton")
delete_button.grid(row = 5, column=2, padx=20, pady=20)

update_button = ttk.Button(root, text="Update", style="Custom.TButton")
update_button.grid(row = 5, column=4, padx=20, pady=20)

results_label = tk.Label(root, text="", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
results_label.grid(row = 6, column=2, padx=5, pady=5)
results_label.config(background = "#6495ed")

submit_button.config(command=submit)
display_button.config(command=Display)
delete_button.config(command=delete)
update_button.config(command=update)

root.mainloop()
