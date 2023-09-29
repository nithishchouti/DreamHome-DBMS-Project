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
        mycursor.execute("SELECT * FROM PropertyView") #try cross join
        rows = mycursor.fetchall()
        root = tk.Tk()
        root.title("Property View Details:")
        tree = ttk.Treeview(root)
        tree["columns"] = ("PropertyId", "ClientID", "DateofVisit","Comments")
        tree.heading("#0", text="Index")
        tree.heading("PropertyId", text="PropertyId")
        tree.heading("ClientID", text="ClientID")
        tree.heading("DateofVisit", text="DateofVisit")
        tree.heading("Comments", text="Comments")


        i = 1
        for row in rows:
            tree.insert(parent="", index=i, text=str(i), values=row)
            i += 1
        tree.pack()



def submit():
        prop_id = propid_entry.get()
        cid = cid_entry.get()
        dov = dov_entry.get()
        com = com_entry.get()

        mycursor = mydb.cursor()
        try:
            sql = "INSERT INTO PropertyView(PropertyID, ClientID, DateofVisit, Comments) VALUES (%s, %s, %s, %s)"
            val = (prop_id, cid, dov, com)
            if cid_entry.get() == '' or propid_entry.get() == '' or dov_entry.get() == '' or com_entry.get() == '' :
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
    property_id = propid_entry.get()
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM PropertyView WHERE PropertyId = %s"
        val = (property_id,)
        if cid_entry.get() == '' or propid_entry.get() == '' or dov_entry.get() == '' or com_entry.get() == '' :
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
    
    prop_id = propid_entry.get()
    cid = cid_entry.get()
    dov = dov_entry.get()
    com = com_entry.get()

    try:
            mycursor = mydb.cursor()
            sql = "UPDATE PropertyView SET ClientId = %s, DateofVisit = %s, Comments = %s WHERE PropertyId = %s"
            val = (prop_id, cid, dov, com)
            if cid_entry.get() == '' or propid_entry.get() == '' or dov_entry.get() == '' or com_entry.get() == '' :
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

propid_label = tk.Label(root, text="Property ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
propid_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
propid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
propid_entry.grid(row = 0, column=1, padx=5, pady=5)
propid_label.config(background="#6495ed")

cid_label = tk.Label(root, text="Client ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
cid_label.grid(row = 0, column=3, padx=5, pady=5, sticky="w")
cid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cid_entry.grid(row = 0, column=4, padx=5, pady=5)
cid_label.config(background="#6495ed")

dov_label = tk.Label(root, text="Date Of Visit:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
dov_label.grid(row = 1, column=0, padx=5, pady=5, sticky="w")
dov_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
dov_entry.grid(row = 1, column=1, padx=5, pady=5)
dov_label.config(background="#6495ed")

com_label = tk.Label(root, text="Comments:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
com_label.grid(row = 1, column=3, padx=5, pady=5, sticky="w")
com_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
com_entry.grid(row = 1, column=4, padx=5, pady=5)
com_label.config(background="#6495ed")

                   
style = ttk.Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")

submit_button = ttk.Button(root, text="Submit", style="Custom.TButton")
submit_button.grid(row = 2, column=1, padx=20, pady=20)

display_button = ttk.Button(root, text="Display", style="Custom.TButton")
display_button.grid(row = 2, column=3, padx=20, pady=20)

delete_button = ttk.Button(root, text="Delete", style="Custom.TButton")
delete_button.grid(row = 2, column=2, padx=20, pady=20)

update_button = ttk.Button(root, text="Update", style="Custom.TButton")
update_button.grid(row = 2, column=4, padx=20, pady=20)

results_label = tk.Label(root, text="", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
results_label.grid(row = 3, column=2, padx=5, pady=5)
results_label.config(background = "#6495ed")

submit_button.config(command=submit)
display_button.config(command=Display)
delete_button.config(command=delete)
update_button.config(command=update)

root.mainloop()
