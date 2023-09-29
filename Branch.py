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
        mycursor.execute("SELECT * FROM Branch") #try cross join
        rows = mycursor.fetchall()
        root = tk.Tk()
        root.title("Branch Details:")
        tree = ttk.Treeview(root)
        tree["columns"] = ("BranchId", "managerId", "Locality","city", "state" , "country")
        tree.heading("#0", text="Index")
        tree.heading("BranchId", text="BranchId")
        tree.heading("managerId", text="ManagerID")
        tree.heading("Locality", text="Locality")
        tree.heading("city", text="City")
        tree.heading("state", text="State")
        tree.heading("country", text="Country")

        i = 1
        for row in rows:
            tree.insert(parent="", index=i, text=str(i), values=row)
            i += 1
       #tree.pack()
        tree.grid(row=1,column=1,padx=20,pady=20)


def show():
    branch = branchid_entry.get()
    sql = "select * from Staff, branch where staff.staffid = branch.managerid and branch.branchid = %s"
    cursor = mydb.cursor()
    val = (branch,)

    if branchid_entry.get() == '':
            results_label.config(text="Error:Enter values", foreground = "red")
    else:

            cursor.execute(sql, val)
            rows = cursor.fetchall()
            root = tk.Tk()
            root.title("Staff Details:")
            tree = ttk.Treeview(root)
            tree["columns"] = ("StaffID", "StaffFName", "StaffMName", "StaffLName", "Sex", "DOB", "Position", "Salary", "BranchID", "SuperID", "StartDate", "Bonus")
            tree.heading("#0", text="Index")
            tree.heading("StaffID", text="StaffID")
            tree.heading("StaffFName", text="First Name")
            tree.heading("StaffMName", text="Middle Name")
            tree.heading("StaffLName", text="Last Name")
            tree.heading("Sex", text="Sex")
            tree.heading("DOB", text="Date Of Birth")
            tree.heading("Position", text="Position")
            tree.heading("Salary", text="Salary")
            tree.heading("BranchID", text="BranchID")
            tree.heading("SuperID", text="SuperID")
            tree.heading("StartDate", text="Starting Date")
            tree.heading("Bonus", text="Bonus")
            #tree.heading("StaffNumber", text="Telephone Number")

            i = 1
            for row in rows:
                tree.insert(parent="", index=i, text=str(i), values=row)
                i += 1
            tree.pack()




def submit():
        branch_id = branchid_entry.get()
        mid = staffid_entry.get()
        locality = locality_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        country = country_entry.get()
        
        #val2 = (property_entry.get(), type_entry.get(), room_entry.get(), rent_entry.get(), locality_entry.get(), city_entry.get(), state_entry.get(), country_entry.get(), staffid_entry.get(), owner_num_entry.get(), bustype_entry.get())

        mycursor = mydb.cursor()
        try:
            sql = "INSERT INTO Branch(BranchID, ManagerID, locality, city, state, country) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (branch_id, mid, locality, city, state, country)
            if branchid_entry.get() == '' or staffid_entry.get() == '' or locality_entry.get()== '' or city_entry.get() == '' or state_entry.get() == '' or country_entry.get() == '':
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
    branch_id = branchid_entry.get()
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM Branch WHERE BranchId = %s"
        val = (branch_id,)
        if branchid_entry.get() == '' or staffid_entry.get() == '' or locality_entry.get()== '' or city_entry.get() == '' or state_entry.get() == '' or country_entry.get() == '':
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
    branch_id = branchid_entry.get()
    mid = staffid_entry.get()
    locality = locality_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    country = country_entry.get()

    try:
            mycursor = mydb.cursor()
            sql = "UPDATE Properties SET Type = %s, NumOfRooms = %s, Rent = %s, locality = %s, city = %s, state = %s, country = %s, ownerId = %s, RegisteredAtBranchId = %s, ManagingStaffId = %s, TypeOfBusiness = %s, contactName = %s, Availability = %s, depositRequired = %s WHERE PropertyId = %s"
            val = (branch_id, mid, locality, city, state, country)
            if branchid_entry.get() == '' or staffid_entry.get() == '' or locality_entry.get()== '' or city_entry.get() == '' or state_entry.get() == '' or country_entry.get() == '':
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
root.title("Branch Registration")
root.configure(background="#6495ed")

branchid_label = tk.Label(root, text="Branch ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
branchid_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
branchid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
branchid_entry.grid(row = 0, column=1, padx=5, pady=5)
branchid_label.config(background="#6495ed")

locality_label = tk.Label(root, text="Locality:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
locality_label.grid(row = 0, column=3, padx=5, pady=5, sticky="w")
locality_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
locality_entry.grid(row = 0, column=4, padx=5, pady=5)
locality_label.config(background="#6495ed")

city_label = tk.Label(root, text="City:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
city_label.grid(row = 1, column=3, padx=5, pady=5, sticky="w")
city_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
city_entry.grid(row = 1, column=4, padx=5, pady=5)
city_label.config(background="#6495ed")

state_label = tk.Label(root, text="State:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
state_label.grid(row = 2, column=3, padx=5, pady=5, sticky="w")
state_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
state_entry.grid(row = 2, column=4, padx=5, pady=5)
state_label.config(background="#6495ed")

country_label = tk.Label(root, text="Country:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
country_label.grid(row = 3, column=3, padx=5, pady=5, sticky="w")
country_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
country_entry.grid(row = 3, column=4, padx=5, pady=5)
country_label.config(background="#6495ed")

staffid_label = tk.Label(root, text="Manager ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
staffid_label.grid(row = 1, column=0, padx=5, pady=5, sticky="w")
staffid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staffid_entry.grid(row = 1, column=1, padx=5, pady=5)
staffid_label.config(background="#6495ed")

tele_label = tk.Label(root, text="Branch Tele Number:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
tele_label.grid(row = 2, column=0, padx=5, pady=5, sticky="w")
tele_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
tele_entry.grid(row = 2, column=1, padx=5, pady=5)
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

sql = "select * from Staff, branch where staff.staffid = branch.managerid"
execute_button = ttk.Button(root, text="Display Staff Information",style="Custom.TButton", command=show)
execute_button.grid(row = 7, column=0, padx=20, pady=20)

results_label = tk.Label(root, text="", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
results_label.grid(row = 8, column=2, padx=5, pady=5)
results_label.config(background = "#6495ed")

submit_button.config(command=submit)
display_button.config(command=Display)
delete_button.config(command=delete)
update_button.config(command=update)


root.mainloop()