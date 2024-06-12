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
    
def revenue_growth():
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
    date_list[]
    while len (date_list) <= 1:
        d = int(input("Enter Day: "))
        m = int(input("Enter Month: "))
        y = int(input("Enter Year: "))
        
        date = datetime(y, m, d)
        udate = date.strftime('%d/%m/%Y')
        
        date_list.append(udate)
        print('\n',date_list)
        
    cursor.execute('SELECT * FROM company_data WHERE company_founded BETWEEN ? AND ?',(date_list[0],date_list[1]))


    print(f'{"Company Name":<19}{"Industry":<21}{"Revenue":<10}{"Growth":<10}{"Employee Count":<20}{"Headquarter":<20}{"Founded Date":<10}')
    print(f'{"_":_<120}')

    for row in cursor.fetchall():
        date = datetime.strftime(row.company_founded,   '%d/%m/%Y')
        record = f'{row.company_name:<19}{row.industry:<21}{row.year_revenue:<10}{row.revenue_growth:<10}{row.employee_no:<20}{row.headquarter:<20}{date:<10}'

        print(record)

        print('\n\n')

    
companies_between_dates()