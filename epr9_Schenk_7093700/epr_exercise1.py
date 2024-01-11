""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk 8017459, Ratnakumar"

import tkinter as tk

from ttkwidgets.autocomplete import AutocompleteCombobox


def calculate():
    """ This function

    """

    # START DEFINITIONS
    bank = 1000
    inhabitants = 100
    exists = ['pool', 'church', 'bus']
    missing = ['supermarket', 'train']
    cycle = 1

    print('JAAAA')


def start_gui(possible_ressources):
    """ This function

    """
    root = tk.Tk()
    background = '#FFFFCC'
    foreground = '#000000'
    cellcolour = '#FFDF00'
    background2 = '#FFDF00'
    foreground2 = '#000000'
    fontsize = 12
    root.geometry('1920x1080')
    root.resizable(True, True)
    root.title('Your Solar Savings Calculator')
    root['bg'] = background

    x1 = 50
    x2 = 290
    y1 = 70
    y2 = 45
    y3 = 70

    schrift = tk.Label(text="Here you can manage your commune!",
                       font=("Helvetica", 13, 'bold'), bg=background, fg=foreground)
    schrift.place(x=x1, y=24)

    land = tk.Label(text="Enter new ressource for your community", font=("Helvetica", fontsize), bg=background, fg=foreground)
    land.place(x=x2, y=y3 + y2 * 0)
    land1 = AutocompleteCombobox(root, completevalues=possible_ressources, foreground='white', width=22, state='readonly')
    land1.place(x=x1, y=y1 + y2 * 0)
    canvas = tk.Canvas(width=470, height=0.00001)
    canvas.create_line(0, 0, 470, 0, width=0.00001)
    canvas.place(x=x1, y=y1 + y2 * 14.35)

    login_button = tk.Button(root, text="See how your community likes the update!", font=("Helvetica", 16), command=calculate, fg='#000000', bg='#FF8C00')
    login_button.place(x=x1, y=y1 + y2 * 8 - 15)

    root.mainloop()


possible_ressources = ['pool', 'church', 'bus', 'supermarket', 'train']
start_gui(possible_ressources)
