# Works on Python 3.12
import tkinter as tk
from doctest import master

from tktable import Table
from enum import Enum

class Zone(Enum):
    Central = 1
    West = 2
    East = 3

data = [
    (1,'San Salvador', Zone.Central),
    (2, 'Santa Ana', Zone.West),
    (3, 'San Miguel', Zone.East),
    (4, 'La Libertad', Zone.Central),
    (5, 'Sonsonate', Zone.West),
    (6, 'Usulutan', Zone.East),
    (7, 'Chalatenango', Zone.Central),
    (8, 'Ahuachapan', Zone.West),
    (9, 'Morazan', Zone.East),
    (10, 'Cuscatlan', Zone.Central),
    (11, 'La Paz', Zone.Central),
    (12, 'Cabanas', Zone.Central),
    (13, 'San Vicente', Zone.Central),
]

table_headers = (
    'ID',
    'Nombre',
    'Zona'
    )

def main():
    window = tk.Tk()
    greeting = tk.Label(text="Hello World, in a Window!")
    greeting.pack()

    add = tk.Button(text="Add")
    delete = tk.Button(text="Delete")
    update = tk.Button(text="Update")

    panel = [add, delete, update]
    for item in panel:
        item.pack()

    row = tk.Frame(master=window, width=700, height=300)
    row.pack()

    table = Table(row, table_headers)
    table.pack()

    for item in data:
        table.insert_row(item)

    print("Hola")

    window.mainloop()

""" This is a multi-line comment function. """
if __name__ == '__main__':
    main()
