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
        mycursor.execute("SELECT * FROM Staff")  #try cross join
        rows = mycursor.fetchall()
        root = tk.Tk()
        #root.geometry("400x250")
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
        staff_id = staffid_entry.get()
        fn = stafffn_entry.get()
        mn = staffmn_entry.get()
        ln = staffln_entry.get()
        sex = sex_entry.get()
        pos = pos_entry.get()
        dob = dob_entry.get()
        salary = salary_entry.get()
        superid = superid_entry.get(),
        branch_id = branchid_entry.get(),
        start = start_entry.get()
        bonus = bonus_entry.get()
        tele = tele_entry.get()
        
        mycursor = mydb.cursor()
        try:
            '''s = "INSERT INTO StaffTelephone VALUE (%s, %s)"
            v = (staff_id, tele)'''
            sql = "INSERT INTO Staff (StaffId, StaffFName, StaffLName, Sex, DOB, Position, Salary, BranchId, SuperId, Startdate, Bonus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (staff_id, fn, mn, ln, sex, dob, pos,salary, branch_id, superid, start, bonus)
            if staffid_entry.get() == '' or stafffn_entry.get() == '' or staffmn_entry.get() == '' or sex_entry.get() == ''or pos_entry.get() == '' or dob_entry.get() == '' or salary_entry.get() == '' or superid_entry.get() == '' or branchid_entry.get() == '' or start_entry.get() == '':
                results_label.config(text="Error: Dream home features not saved successfully, Enter values", foreground = "red")
            else:
                mycursor.execute(sql, val)
                if mycursor.rowcount > 0:
                    results_label.config(text="Dream home features saved successfully.", foreground = "black")
                    mydb.commit()
                    '''mycursor.execute(s, val)
                    mydb.commit()'''
                    
                else:
                    results_label.config(text="Error: Dream home features not saved successfully", foreground = "red")
        except mysql.connector.IntegrityError as e:
            print("Query was not successful: {}".format(e))

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

def delete():
    staffid = staffid_entry.get()
    
    mycursor = mydb.cursor()
        
    try:
        Es = "Delete from StaffTelephone where (%s)"
        sql = "DELETE FROM Staff WHERE StaffId = %s"
        val = (staffid,)
        if staffid_entry.get() == '' or stafffn_entry.get() == '' or staffmn_entry.get() == '' or sex_entry.get() == ''or pos_entry.get() == '' or dob_entry.get() == '' or salary_entry.get() == '' or superid_entry.get() == '' or branchid_entry.get() == '' or start_entry.get() == '':
            results_label.config(text="Error: Enter Values", foreground = "red")
        else:
            mycursor.execute(sql, val)
            if mycursor.rowcount > 0:
                results_label.config(text="Deleted successdully.", foreground = "black")
                mydb.commit()
                '''mycursor.execute(s, val)
                mydb.commit()'''

            else:
                results_label.config(text="Error: Cannot be Deleted", foreground = "red")
            
    except mysql.connector.IntegrityError as e:
        print("Query was not successful: {}".format(e))

    except mysql.connector.Error as error:
        print("Failed to delete into MySQL table {}".format(error))

def update():
    staff_id = staffid_entry.get()
    fn = stafffn_entry.get()
    mn = staffmn_entry.get()
    ln = staffln_entry.get()
    sex = sex_entry.get()
    pos = pos_entry.get()
    dob = dob_entry.get()
    salary = salary_entry.get()
    superid = superid_entry.get(),
    branch_id = branchid_entry.get(),
    start = start_entry.get()
    bonus = bonus_entry.get()
    tele = tele_entry.get()
    mycursor = mydb.cursor()

    try:
            '''s = "UPDATE Staff SET StaffNumber = %s WHERE StaffId = %s"
            v = (tele, staff_id)'''
            sql = "UPDATE Staff SET StaffFName = %s, StaffMName = %s, StaffLName = %s, Sex = %s, Position = %s, Salary = %s, BranchId = %s, SuperId = %s, Startdate = %s, Bonus = %s WHERE StaffId = %s"
            val = (fn, mn, ln, sex, pos, salary, branch_id, superid, start, bonus, staff_id)
            if staffid_entry.get() == '' or stafffn_entry.get() == '' or staffmn_entry.get() == '' or sex_entry.get() == ''or pos_entry.get() == '' or dob_entry.get() == '' or salary_entry.get() == '' or superid_entry.get() == '' or branchid_entry.get() == '' or start_entry.get() == '':
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
root.title("Staff Registration")
root.configure(background="#6495ed")

staffid_label = tk.Label(root, text="Staff Number:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staffid_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
staffid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staffid_entry.grid(row = 0, column=1, padx=5, pady=5)
staffid_label.config(background="#6495ed")

stafffn_label = tk.Label(root, text="First Name", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
stafffn_label.grid(row = 1, column=0, padx=5, pady=5, sticky="w")
stafffn_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
stafffn_entry.grid(row = 1, column=1, padx=5, pady=5)
stafffn_label.config(background="#6495ed")

staffmn_label = tk.Label(root, text="Middle Name:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staffmn_label.grid(row = 2, column=0, padx=5, pady=5, sticky="w")
staffmn_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staffmn_entry.grid(row = 2, column=1, padx=5, pady=5)
staffmn_label.config(background="#6495ed")

staffln_label = tk.Label(root, text="Last Name:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
staffln_label.grid(row = 3, column=0, padx=5, pady=5, sticky="w")
staffln_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
staffln_entry.grid(row = 3, column=1, padx=5, pady=5)
staffid_label.config(background="#6495ed")

sex_label = tk.Label(root, text="Sex:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
sex_label.grid(row = 4, column=0, padx=5, pady=5, sticky="w")
sex_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
sex_entry.grid(row = 4, column=1, padx=5, pady=5)
sex_label.config(background="#6495ed")

pos_label = tk.Label(root, text="Position:", font=("Helvetica", 18), foreground="#000080", background="#6495ed" )
pos_label.grid(row = 5, column=0, padx=5, pady=5, sticky="w")
pos_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
pos_entry.grid(row = 5, column=1, padx=5, pady=5)
pos_label.config(background="#6495ed")

dob_label = tk.Label(root, text="Date of Birth:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
dob_label.grid(row = 5, column=0, padx=5, pady=5, sticky="w")
dob_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
dob_entry.grid(row = 5, column=1, padx=5, pady=5)
dob_label.config(background="#6495ed")

salary_label = tk.Label(root, text="Salary:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
salary_label.grid(row = 7, column=0, padx=5, pady=5, sticky="w")
salary_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
salary_entry.grid(row = 7, column=1, padx=5, pady=5)
salary_label.config(background="#6495ed")

det_label = tk.Label(root, text="Enter details wherever applicable:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
det_label.grid(row = 8, column=0, padx=5, pady=5, sticky="w")
det_label.config(background="#6495ed")

superid_label = tk.Label(root, text="Supervisor's ID", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
superid_label.grid(row = 9, column=0, padx=5, pady=5, sticky="w")
superid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
superid_entry.grid(row = 9, column=1, padx=5, pady=5)
superid_label.config(background="#6495ed")

branchid_label = tk.Label(root, text="Branch ID:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
branchid_label.grid(row = 0, column=3, padx=5, pady=5, sticky="w")
branchid_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
branchid_entry.grid(row = 0, column=4, padx=5, pady=5)
branchid_label.config(background="#6495ed")

tele_label = tk.Label(root, text="Telephone Number:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
tele_label.grid(row = 1, column=3, padx=5, pady=5, sticky="w")
tele_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
tele_entry.grid(row = 1, column=4, padx=5, pady=5)
tele_label.config(background="#6495ed")

start_label = tk.Label(root, text="Start Date:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
start_label.grid(row = 9, column=3, padx=5, pady=5, sticky="w")
start_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
start_entry.grid(row = 9, column=4, padx=5, pady=5)
stafffn_label.config(background="#6495ed")

bonus_label = tk.Label(root, text="Bonus:", font=("Helvetica", 18), foreground="#000080", background="#6495ed") 
bonus_label.grid(row = 10, column=3, padx=5, pady=5, sticky="w")
bonus_entry = tk.Entry(root, font=("Helvetica", 18), foreground="#000080", background="#6495ed")
bonus_entry.grid(row = 10, column=4, padx=5, pady=5)
bonus_label.config(background="#6495ed")


style = ttk.Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")

submit_button = ttk.Button(root, text="Submit", style="Custom.TButton")
submit_button.grid(row = 12, column=1, padx=20, pady=20)

display_button = ttk.Button(root, text="Display", style="Custom.TButton")
display_button.grid(row = 12, column=3, padx=20, pady=20)

delete_button = ttk.Button(root, text="Delete", style="Custom.TButton")
delete_button.grid(row = 12, column=2, padx=20, pady=20)

update_button = ttk.Button(root, text="Update", style="Custom.TButton")
update_button.grid(row = 12, column=4, padx=20, pady=20)

results_label = tk.Label(root, text="", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
results_label.grid(row = 13, column=2, padx=5, pady=5)
results_label.config(background = "#6495ed")

submit_button.config(command=submit)
display_button.config(command=Display)
delete_button.config(command=delete)
update_button.config(command=update)


root.mainloop()
