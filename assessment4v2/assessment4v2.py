import tkinter as tk
from tkinter import messagebox
import pyodbc
from datetime import datetime

#connect to database
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2019002577\source\repos\assessment4v2sol\assessment4v2\data\data.accdb;')
cursor = conn.cursor()

#formatting
formatTemp1 = '{0:<19}{1:<21}{2:<10}{3:<10}{4:<20}{5:<20}{6:<10}'

#function to print all
def print_all():
    cursor.execute("SELECT * FROM company_data")

    print(f'{"Company Name":<19}{"Industry":<21}{"Revenue":<10}{"Growth":<10}{"Employee Count":<20}{"Headquarter":<20}{"Founded Date":<10}')
    print(f'{"_":_<120}')

    for row in cursor.fetchall():
        date = datetime.strftime(row.company_founded,   '%d/%m/%Y')
        record = f'{row.company_name:<19}{row.industry:<21}{row.year_revenue:<10}{row.revenue_growth:<10}{row.employee_no:<20}{row.headquarter:<20}{date:<10}'

        print(record)

    print('\n\n')
    
def positive_growth():
    cursor.execute("SELECT * FROM company_data WHERE revenue_growth >0 ")

    print(f'{"Company Name":<19}{"Industry":<21}{"Revenue":<10}{"Growth":<10}{"Employee Count":<20}{"Headquarter":<20}{"Founded Date":<10}')
    print(f'{"_":_<120}')

    for row in cursor.fetchall():
        date = datetime.strftime(row.company_founded,   '%d/%m/%Y')
        record = f'{row.company_name:<19}{row.industry:<21}{row.year_revenue:<10}{row.revenue_growth:<10}{row.employee_no:<20}{row.headquarter:<20}{date:<10}'

        print(record)

    print('\n\n')

def record_by_date():
    date_input = entry_date.get()
    cursor.execute("SELECT * FROM company_data WHERE company_founded = ?", (date_input))
    records = cursor.fetchall()
    if records:
        print(records)
    else:
        messagebox.showinfo("No records found")
        
       

def companies_between_dates():
    start_date_entry = input_start_date.get()
    end_date_entry = input_end_date.get()
    start_date = datetime.strptime(start_date_entry, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_entry, "%Y-%m-%d")

        
    cursor.execute('SELECT * FROM company_data WHERE company_founded BETWEEN ? AND ?',(start_date, end_date))


    print(f'{"Company Name":<19}{"Industry":<21}{"Revenue":<10}{"Growth":<10}{"Employee Count":<20}{"Headquarter":<20}{"Founded Date":<10}')
    print(f'{"_":_<120}')

    for row in cursor.fetchall():
        record = f'{row.company_name:<19}{row.industry:<21}{row.year_revenue:<10}{row.revenue_growth:<10}{row.employee_no:<20}{row.headquarter:<20}{date:<10}'

        print(record)

        print('\n\n')

#GUI start
master = tk.Tk()
master.title("Company Management Data")
# master.geometry("700x400")

frame = tk.Frame(master)
frame.pack(pady=10)

#print all
print_allbtn = tk.Button(frame, text="Print All Records", command=print_all)
print_allbtn.grid(row=0, column=0, padx=10, pady=10)

#positive growth
positive_growthbtn = tk.Button(frame, text="Print Companies With Positive Growth", command=positive_growth)
positive_growthbtn.grid(row=0, column=1, padx=10, pady=10)

#company by date
label_date = tk.Label(frame, text="Enter Date (DD/MM/YYYY): ")
label_date.grid(row=1, column=0, padx=10, pady=10)
entry_date = tk.Entry(frame)
entry_date.grid(row=1, column=1, padx=10, pady=10)
record_by_datebtn = tk.Button(frame, text="Search Companies By Date", command=record_by_date)
record_by_datebtn.grid(row=1, column=2, padx=10, pady=10)

#company's within dates
label_start_date = tk.Label(frame, text="Enter Start Date (DD/MM/YYYY): ")
label_start_date.grid(row=2, column=0, padx=10, pady=10)
input_start_date = tk.Entry(frame)
input_start_date.grid(row=2, column=1, padx=10, pady=10)
label_end_date = tk.Label(frame, text="Enter End Date (DD/MM/YYYY): ")
label_end_date.grid(row=2, column=2, padx=10, pady=10)
input_end_date = tk.Entry(frame)
input_end_date.grid(row=2, column=3, padx=10, pady=10)
companies_between_datesbtn = tk.Button(frame, text="Search Companies Between These Dates", command=companies_between_dates)
companies_between_datesbtn.grid(row=2, column=4, padx=10, pady=10)



tk.mainloop()