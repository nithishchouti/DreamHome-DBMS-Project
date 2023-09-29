import tkinter as tk
import mysql.connector
from tkinter import ttk
import numpy as np

def show_results(query):
    # Connect to the database
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nithish@2003",
    database="dreamhouse"

    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    new_window = tk.Toplevel(root)
    new_window.title("Query Results")
    #new_window.configure(background="#6495ed")


    for row_index, row in enumerate(results):
        for col_index, col in enumerate(row):
            label = tk.Label(new_window, text=str(col))
            label.grid(row=row_index, column=col_index)

root = tk.Tk()
root.title("Queries")
root.configure(background="#6495ed")
    # Create a label and an entry for the query
query_label = tk.Label(root, text="Enter your query:", font=("Helvetica", 18), foreground="#000080", background="#6495ed")
query_label.grid(row = 0, column=0, padx=5, pady=5, sticky="w")
query_entry = tk.Text(root)
query_entry.grid(row = 1, column=1, padx=5, pady=5, sticky="w")
query_entry.configure(font=("Helvetica", 18), background='#6495ed', foreground='#000080', bd=2, relief='solid')
query_label.config(background="#6495ed")

style = ttk.Style()
style.configure("Custom.TButton", borderwidth=2, relief="ridge", 
                font=("Helvetica", 18), foreground="#000080", 
                background="#ff1493")

execute_button = ttk.Button(root, text="Execute",style="Custom.TButton", command=lambda: show_results(query_entry.get('1.0', 'end')))
execute_button.grid(row = 2, column=0, padx=20, pady=20)

root.mainloop()