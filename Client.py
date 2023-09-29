import tkinter as tk
import mysql.connector
from tkinter import ttk

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Nithish@2003",
database="dreamhouse"
)

def Display():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Client")  #try cross join
        rows = mycursor.fetchall()
        root = tk.Tk()
        #root.geometry("400x250")
        root.title("Client Details:")
        tree = ttk.Treeview(root)
        tree["columns"] = ("ClientID", "ClientFName", "ClientMName", "ClientLName", "RegisteredAtBranchId", "RegisteredByStaffId", "DateofRegisteration", "TypeWanted", "MaxRent")
        tree.heading("ClientID", text="ClientID")
        tree.heading("ClientFName", text="First Name")
        tree.heading("ClientMName", text="Middle Name")
        tree.heading("ClientLName", text="Last Name")
        tree.heading("RegisteredAtBranchId", text="RegisteredAtBranchId")
        tree.heading("RegisteredByStaffId", text="DRegisteredByStaffId")
        tree.heading("DateofRegisteration", text="Date of Registrattion")
        tree.heading("TypeWanted", text="Type Wanted")
        tree.heading("MaxRent", text="MaxRent")
        #tree.heading("StaffNumber", text="Telephone Number")

        i = 1
        for row in rows:
            tree.insert(parent="", index=i, text=str(i), values=row)
            i += 1
        tree.pack()

    


def submit():
        cid = cid_entry.get()
        fn = cfn_entry.get()
        mn = cmn_entry.get()
        ln = cln_entry.get()
        type = type_entry.get()
        branchid = branch_entry.get(),
        staff = staff_entry.get()
        rent = rent_entry.get()
        tele = tele_entry.get()
        dor = dor_entry.get()
        

        mycursor = mydb.cursor()
        try:
            sql = "INSERT INTO Client (ClientId, ClientFName, ClientLName, RegisteredAtBranchId, RegisteredByStaffId, DateofRegistrattion, TypeWanted, MaxRent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (cid, fn, mn, ln, branchid, staff, dor,type, rent)
            if cid_entry.get() == '' or cfn_entry.get() == ''  or cmn_entry.get() == ''  or cln_entry.get() == '' or type_entry.get() == ''  or branch_entry.get() == '' or staff_entry.get() == ''  or rent_entry.get() == ''  or dor_entry.get() == '' :
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
    client_id = cid_entry.get()
    
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM Client WHERE ClientId = %s"
        val = (client_id,)
        if cid_entry.get() == '' or cfn_entry.get() == ''  or cmn_entry.get() == ''  or cln_entry.get() == '' or type_entry.get() == ''  or branch_entry.get() == '' or staff_entry.get() == ''  or rent_entry.get() == ''  or dor_entry.get() == '' :
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
    cid = cid_entry.get()
    fn = cfn_entry.get()
    mn = cmn_entry.get()
    ln = cln_entry.get()
    type = type_entry.get()
    branchid = branch_entry.get(),
    staff = staff_entry.get()
    rent = rent_entry.get()
    tele = tele_entry.get()
    dor = dor_entry.get()
    

    try:
            mycursor = mydb.cursor()
            sql = "UPDATE Client SET clientFname = %s, clientMname = %s, clientLname = %s, RegisteredAtBranchId = %s, RegisteredByStaffId = %s, DateofRegistrattion = %s, TypeWanted = %s, MaxRent = %s WHERE ClientId = %s"
            val = (cid, fn, mn, ln, branchid, staff, dor,type, rent)
            if cid_entry.get() == '' or cfn_entry.get() == ''  or cmn_entry.get() == ''  or cln_entry.get() == '' or type_entry.get() == ''  or branch_entry.get() == '' or staff_entry.get() == ''  or rent_entry.get() == ''  or dor_entry.get() == '' :
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
root.title("Client Registration")
root.configure(background="#6495ed")

cid_label = tk.Label(root, text="Client ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cid_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
cid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cid_entry.grid(row = 0, column=1, padx=5, pady=5)
cid_label.config(background="#6495ed")

cfn_label = tk.Label(root, text="First Name", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cfn_label.grid(row = 1, column=0, padx=5, pady=5, sticky="w")
cfn_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cfn_entry.grid(row = 1, column=1, padx=5, pady=5)
cfn_label.config(background="#6495ed")

cmn_label = tk.Label(root, text="Middle Name:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cmn_label.grid(row = 2, column=0, padx=5, pady=5, sticky="w")
cmn_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cmn_entry.grid(row = 2, column=1, padx=5, pady=5)
cmn_label.config(background="#6495ed")

cln_label = tk.Label(root, text="Last Name:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
cln_label.grid(row = 3, column=0, padx=5, pady=5, sticky="w")
cln_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
cln_entry.grid(row = 3, column=1, padx=5, pady=5)
cln_label.config(background="#6495ed")

branch_label = tk.Label(root, text="Branch ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
branch_label.grid(row = 0, column=3, padx=5, pady=5, sticky="w")
branch_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
branch_entry.grid(row = 0, column=4, padx=5, pady=5)
branch_label.config(background="#6495ed")

staff_label = tk.Label(root, text="Staff ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
staff_label.grid(row = 1, column=3, padx=5, pady=5, sticky="w")
staff_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staff_entry.grid(row = 1, column=4, padx=5, pady=5)
staff_label.config(background="#6495ed")

det_label = tk.Label(root, text="Enter Property Requirements:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
det_label.grid(row = 5, column=0, padx=5, pady=5, sticky="w")
det_label.config(background="#6495ed")

type_label = tk.Label(root, text="Type Wanted:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
type_label.grid(row = 6, column=0, padx=5, pady=5, sticky="w")
type_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
type_entry.grid(row = 6, column=1, padx=5, pady=5)
type_label.config(background="#6495ed")

rent_label = tk.Label(root, text="Maximum Rent:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
rent_label.grid(row = 7, column=3, padx=5, pady=5, sticky="w")
rent_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
rent_entry.grid(row = 7, column=4, padx=5, pady=5)
rent_label.config(background="#6495ed")

tele_label = tk.Label(root, text="Branch Tele Number:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
tele_label.grid(row = 3, column=3, padx=5, pady=5, sticky="w")
tele_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
tele_entry.grid(row = 3, column=4, padx=5, pady=5)
tele_label.config(background="#6495ed")

dor_label = tk.Label(root, text="Date of Registration:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
dor_label.grid(row = 4, column=3, padx=5, pady=5, sticky="w")
dor_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
dor_entry.grid(row = 4, column=4, padx=5, pady=5)
dor_label.config(background="#6495ed")


style = ttk.Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")

submit_button = ttk.Button(root, text="Submit", style="Custom.TButton")
submit_button.grid(row = 9, column=1, padx=20, pady=20)

display_button = ttk.Button(root, text="Display", style="Custom.TButton")
display_button.grid(row = 9, column=3, padx=20, pady=20)

delete_button = ttk.Button(root, text="Delete", style="Custom.TButton")
delete_button.grid(row = 9, column=2, padx=20, pady=20)

update_button = ttk.Button(root, text="Update", style="Custom.TButton")
update_button.grid(row = 9, column=4, padx=20, pady=20)

results_label = tk.Label(root, text="", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
results_label.grid(row = 10, column=2, padx=5, pady=5)
results_label.config(background = "#6495ed")

submit_button.config(command=submit)
display_button.config(command=Display)
delete_button.config(command=delete)
update_button.config(command=update)

root.mainloop()
