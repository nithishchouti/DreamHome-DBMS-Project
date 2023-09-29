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


def convertTuple(tup):
        str_list = [str(item) for item in tup if item is not None]
        result_str = ' '.join(str_list)
        return result_str



def Display():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Properties")
        rows = mycursor.fetchall()
        root = tk.Tk()
        root.title("Properties:")
        tree = ttk.Treeview(root)

        tree["columns"] = ("PropertyId", "Type", "NumOfRooms", "Rent", "Locality", "city", "state", "country", "ownerId", "RegisteredAtBranchId", "ManagingStaffId", "TypeOfBusiness", "ContactName", "Availability", "DepositRequired")
        tree.heading("#0", text="Index")
        tree.heading("PropertyId", text="PropertyId")
        tree.heading("Type", text="Type")
        tree.heading("NumOfRooms", text="NumOfRooms")
        tree.heading("Rent", text="Rent")
        tree.heading("Locality", text="Locality")
        tree.heading("city", text="city")
        tree.heading("state", text="state")
        tree.heading("country", text="country")
        tree.heading("ownerId", text="ownerId")
        tree.heading("RegisteredAtBranchId", text="RegisteredAtBranchId")
        tree.heading("ManagingStaffId", text="ManagingStaffId")
        tree.heading("TypeOfBusiness", text="TypeOfBusiness")
        tree.heading("ContactName", text="ContactName")
        tree.heading("Availability", text="Availability")
        tree.heading("DepositRequired", text="DepositRequired")

        i = 1
        for row in rows:
            tree.insert(parent="", index=i, text=str(i), values=row)
            i += 1
        tree.pack()

def submit():
        property_id = property_entry.get()
        typep = type_entry.get()
        num_rooms = room_entry.get()
        Rent = rent_entry.get()
        locality = locality_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        country = country_entry.get()
        staffid = staffid_entry.get(),
        owner_id = owner_num_entry.get(),
        bustype = bustype_entry.get()
        contact = contactname_entry.get()
        branchid = branchid_entry.get(),
        dep = dep_entry.get()
        
        #val2 = (property_entry.get(), type_entry.get(), room_entry.get(), rent_entry.get(), locality_entry.get(), city_entry.get(), state_entry.get(), country_entry.get(), staffid_entry.get(), owner_num_entry.get(), bustype_entry.get())

        mycursor = mydb.cursor()
        
        try:
            sql = "INSERT INTO Properties(`PropertyId`, `Type`, `NumOfRooms`, `Rent`, `locality`, `city`, `state`, `country`, `ownerId`, `RegisteredAtBranchId`, `ManagingStaffId`, `TypeOfBusiness`, `contactName`, `availability`, `depositRequired`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            #val = [property_id, typep, num_rooms, Rent, locality, city, state, country, owner_id, branchid, staffid, bustype, contact, 'T', dep]
            val2 = (property_entry.get(), type_entry.get(), room_entry.get(), rent_entry.get(), locality_entry.get(), city_entry.get(), state_entry.get(), country_entry.get(),  owner_num_entry.get(), branchid_entry.get(), staffid_entry.get(), bustype_entry.get(), contactname_entry.get(), 'T', dep_entry.get())
            if property_entry.get() == '' or type_entry.get() == '' or room_entry.get() == '' or rent_entry.get() == ''or locality_entry.get() == '' or city_entry.get() == '' or state_entry.get() == '' or country_entry.get() == '' or owner_num_entry.get() == ''or branchid_entry.get() == '' or staffid_entry.get() == '' or bustype_entry.get() == '' or contactname_entry.get() == '' or dep_entry.get() == '':
                results_label.config(text="Error: Dream home features not saved successfully, Enter values", foreground = "red")
            else:
                mycursor.execute(sql, val2)
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
    property_id = property_entry.get()

    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM Properties WHERE PropertyId = %s"
        val = (property_id,)
        print(mycursor.rowcount, "record(s) deleted.")
        if property_entry.get() == '' or type_entry.get() == '' or room_entry.get() == '' or rent_entry.get() == ''or locality_entry.get() == '' or city_entry.get() == '' or state_entry.get() == '' or country_entry.get() == '' or owner_num_entry.get() == ''or branchid_entry.get() == '' or staffid_entry.get() == '' or bustype_entry.get() == '' or contactname_entry.get() == '' or dep_entry.get() == '':

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
        property_id = property_entry.get()
        typep = type_entry.get()
        num_rooms = room_entry.get()
        Rent = rent_entry.get()
        locality = locality_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        country = country_entry.get()
        staffid = staffid_entry.get(),
        owner_id = owner_num_entry.get(),
        bustype = bustype_entry.get()
        contact = contactname_entry.get()
        branchid = branchid_entry.get(),
        dep = dep_entry.get()

        mycursor = mydb.cursor()
        try:
            
            sql = "UPDATE Properties SET Type = %s, NumOfRooms = %s, Rent = %s, locality = %s, city = %s, state = %s, country = %s, ownerId = %s, RegisteredAtBranchId = %s, ManagingStaffId = %s, TypeOfBusiness = %s, contactName = %s, Availability = %s, depositRequired = %s WHERE PropertyId = %s"
            val = (property_entry.get(), type_entry.get(), room_entry.get(), rent_entry.get(), locality_entry.get(), city_entry.get(), state_entry.get(), country_entry.get(),  owner_num_entry.get(), branchid_entry.get(), staffid_entry.get(), bustype_entry.get(), contactname_entry.get(), 'T', dep_entry.get())
            if property_entry.get() == '' or type_entry.get() == '' or room_entry.get() == '' or rent_entry.get() == ''or locality_entry.get() == '' or city_entry.get() == '' or state_entry.get() == '' or country_entry.get() == '' or owner_num_entry.get() == ''or branchid_entry.get() == '' or staffid_entry.get() == '' or bustype_entry.get() == '' or contactname_entry.get() == '' or dep_entry.get() == '':

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


property_label = tk.Label(root, text="Property Number:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
property_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
property_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
property_entry.grid(row = 0, column=1, padx=5, pady=5)
property_label.config(background="#6495ed")

type_label = tk.Label(root, text="Type:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
type_label.grid(row = 1, column=0, padx=5, pady=5, sticky="w")
type_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
type_entry.grid(row = 1, column=1, padx=5, pady=5)
type_label.config(background="#6495ed")

room_label = tk.Label(root, text="Number of Rooms:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
room_label.grid(row = 2, column=0, padx=5, pady=5, sticky="w")
room_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
room_entry.grid(row = 2, column=1, padx=5, pady=5)
room_label.config(background="#6495ed")

rent_label = tk.Label(root, text="Rent:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
rent_label.grid(row = 3, column=0, padx=5, pady=5, sticky="w")
rent_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
rent_entry.grid(row = 3, column=1, padx=5, pady=5)
rent_label.config(background="#6495ed")

locality_label = tk.Label(root, text="Locality:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
locality_label.grid(row = 4, column=0, padx=5, pady=5, sticky="w")
locality_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
locality_entry.grid(row = 4, column=1, padx=5, pady=5)
locality_label.config(background="#6495ed")


city_label = tk.Label(root, text="City:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
city_label.grid(row = 5, column=0, padx=5, pady=5, sticky="w")
city_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
city_entry.grid(row = 5, column=1, padx=5, pady=5)
city_label.config(background="#6495ed")

state_label = tk.Label(root, text="State:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
state_label.grid(row = 6, column=0, padx=5, pady=5, sticky="w")
state_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
state_entry.grid(row = 6, column=1, padx=5, pady=5)
state_label.config(background="#6495ed")

country_label = tk.Label(root, text="Country:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
country_label.grid(row = 7, column=0, padx=5, pady=5, sticky="w")
country_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
country_entry.grid(row = 7, column=1, padx=5, pady=5)
country_label.config(background="#6495ed")

staff_label = tk.Label(root, text="Managed by Staff:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staff_label.grid(row = 9, column=0, padx=5, pady=5, sticky="w")
staff_label.config(background="#6495ed")

staffid_label = tk.Label(root, text="Staff ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
staffid_label.grid(row = 10, column=0, padx=5, pady=5, sticky="w")
staffid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staffid_entry.grid(row = 10, column=1, padx=5, pady=5)
staffid_label.config(background="#6495ed")

owner_num_label = tk.Label(root, text="Owner Number:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
owner_num_label.grid(row = 0, column=3, padx=5, pady=5, sticky="w")
owner_num_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
owner_num_entry.grid(row = 0, column=4, padx=5, pady=5)
owner_num_label.config(background="#6495ed")

bustype_label = tk.Label(root, text="Type of Business:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
bustype_label.grid(row = 4, column=3, padx=5, pady=5, sticky="w")
bustype_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
bustype_entry.grid(row = 4, column=4, padx=5, pady=5)
bustype_label.config(background="#6495ed")

contactname_label = tk.Label(root, text="Contact Name:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
contactname_label.grid(row = 5, column=3, padx=5, pady=5, sticky="w")
contactname_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
contactname_entry.grid(row = 5, column=4, padx=5, pady=5)
contactname_label.config(background="#6495ed")

branchaddress_label = tk.Label(root, text="Resgistered At Branch:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
branchaddress_label.grid(row = 7, column=3, padx=5, pady=5, sticky="w")
branchaddress_label.config(background="#6495ed")

branchid_label = tk.Label(root, text="Branch ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
branchid_label.grid(row = 8, column=3, padx=5, pady=5, sticky="w")
branchid_entry = tk.Entry(root,font=("Helvetica", 18), foreground="#000080", background="#6495ed")
branchid_entry.grid(row = 8, column=4, padx=5, pady=5)
branchid_label.config(background="#6495ed")

dep_label = tk.Label(root, text="Desposit Required:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
dep_label.grid(row = 12, column=0, padx=5, pady=5, sticky="w")
dep_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
dep_entry.grid(row = 12, column=1, padx=5, pady=5)
dep_label.config(background="#6495ed")

style = ttk.Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")

# Create the button using the custom style
submit_button = ttk.Button(root, text="Submit", style="Custom.TButton")
submit_button.grid(row = 14, column=1, padx=20, pady=20)

display_button = ttk.Button(root, text="Display", style="Custom.TButton")
display_button.grid(row = 14, column=3, padx=20, pady=20)

delete_button = ttk.Button(root, text="Delete", style="Custom.TButton")
delete_button.grid(row = 14, column=2, padx=20, pady=20)

update_button = ttk.Button(root, text="Update", style="Custom.TButton")
update_button.grid(row = 14, column=4, padx=20, pady=20)


'''submit_button = tk.Button(root, text="Submit", foreground="#000080", background="#ff1493")
submit_button.grid(row = 14, column=1, padx=5, pady=5)
submit_button.config(background="#ff1493")

display_button = tk.Button(root, text="Display", foreground="#000080", background="#ff1493")
display_button.grid(row = 14, column=3, padx=5, pady=5)
display_button.config(background="#ff1493")'''

results_label = tk.Label(root, text="", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
results_label.grid(row = 15, column=2, padx=5, pady=5)
results_label.config(background = "#6495ed")


submit_button.config(command=submit)
display_button.config(command=Display)
delete_button.config(command=delete)
update_button.config(command=update)

root.mainloop()