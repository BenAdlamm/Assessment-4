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
    d = int(input("Enter Day: "))
    m = int(input("Enter Month: "))
    y = int(input("Enter Year: "))
    
    date = datetime(y, m, d)
    udate = date.strftime('%d/%m/%Y')
    
    cursor.execute("SELECT * FROM company_data")
    
    for row in cursor.fetchall():
        rowDate = datetime.strftime(row.company_founded,    '%d/%m/%Y')
    
        if udate in rowDate:
            date_str = 'Company Name: {name} /nRevenue: {revenue}'.format(name=row.company_name, revenue=row.year_revenue)
            break
        else:
            date_str = "Records not found"
        
    print(date_str)
    
def companies_between_dates():
    start_date_entry = entry_start_date.get()
    end_date_entry = entry_end_date.get()
    start_date = datetime.strptime(start_date_entry, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_entry, "%Y-%m-%d")

        
    cursor.execute('SELECT * FROM company_data WHERE company_founded BETWEEN ? AND ?',(start_date, end_date))


    print(f'{"Company Name":<19}{"Industry":<21}{"Revenue":<10}{"Growth":<10}{"Employee Count":<20}{"Headquarter":<20}{"Founded Date":<10}')
    print(f'{"_":_<120}')

    for row in cursor.fetchall():
        record = f'{row.company_name:<19}{row.industry:<21}{row.year_revenue:<10}{row.revenue_growth:<10}{row.employee_no:<20}{row.headquarter:<20}{date:<10}'

        print(record)

        print('\n\n')

    
root = tk.Tk()
root.title("Company Management Data")

frame = tk.Frame(root)
frame.pack(pady=10)

print_allbtn = tk.Button(frame, text="Print All Records", command=print_all)
print_allbtn.grid(row=0, column=0, padx=10, pady=10)

positive_growthbtn = tk.Button(frame, text="Print Positive Growth", command=positive_growth)
positive_growthbtn.grid(row=1, column=0, padx=10, pady=10)






root.mainloop()