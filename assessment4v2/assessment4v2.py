import tkinter as tk
from tkinter import messagebox
import pyodbc
from datetime import datetime

#connect to database
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2019002577\source\repos\assessment4v2sol\assessment4v2\data\data.accdb;')
cursor = conn.cursor()
