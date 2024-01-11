import tkinter as tk
import warnings
from tkinter.messagebox import showinfo

import matplotlib
from ttkwidgets.autocomplete import AutocompleteCombobox

matplotlib.use('TkAgg')
warnings.filterwarnings("ignore")


def getdata(possible_ressources, ausrichtung):
    # START DEFINITIONS
    exists = ['church']

    def calculation_clicked():
        global missing_ressources, missing_ressources1, existing_ressources, existing_ressources1
        global costs_var, costs_var1
        missing_ressources = str(missing_ressources1.get())
        existing_ressources = str(existing_ressources1.get())
        costs_var = costs_var1.get()
        print(missing_ressources, existing_ressources, costs_var)
        if missing_ressources != '':
            msg = f' The influence of a new ressource ({missing_ressources}) will be calculated'
        else:
            msg = f' The influence of an existing ressource ({missing_ressources}) will be calculated'
        showinfo(title='Information', message=msg)
        main()



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

    global missing_ressources, missing_ressources1, existing_ressources, existing_ressources1
    global costs_var, costs_var1
    x1 = 50
    x2 = 290
    y1 = 70
    y2 = 45
    y3 = 70

    # ----------------- GUI BEFORE CALCULATION ----------------

    schrift = tk.Label(text="Here you can calculate how your community likes your changes!", font=("Helvetica", 13, 'bold'), bg=background, fg=foreground)
    schrift.place(x=x1, y=24)

    missing_ressources = tk.Label(text="Add a new ressource", font=("Helvetica", fontsize), bg=background, fg=foreground)
    missing_ressources.place(x=x2, y=y3 + y2 * 2)
    missing_ressources1 = AutocompleteCombobox(root, completevalues=[elem for elem in possible_ressources if elem not in exists], foreground='white', width=22, state='readonly')
    missing_ressources1.place(x=x1, y=y1 + y2 * 2)

    existing_ressources = tk.Label(text="Delete an existing community ressource (start = just church)", font=("Helvetica", fontsize), bg=background, fg=foreground)
    existing_ressources.place(x=x2, y=y3 + y2 * 3)
    existing_ressources1 = AutocompleteCombobox(root, completevalues=[elem for elem in possible_ressources if elem in exists], foreground='white', width=22, state='readonly')
    existing_ressources1.place(x=x1, y=y1 + y2 * 3)

    costs_var = tk.Label(text="Enter variable costs for new ressource or savings for existing ressource (yearly)", font=("Helvetica", fontsize), bg=background, fg=foreground)
    costs_var.place(x=x2, y=y3 + y2 * 4)
    costs_var1 = tk.StringVar()
    costs_var1 = tk.Entry(root, textvariable=costs_var1, fg=foreground, width=24, bg=cellcolour)
    costs_var1.place(x=x1, y=y1 + y2 * 4)
    costs_var1.insert(0, str(40))

    inhabitants_change = tk.Label(text="Starting community inhabitants", font=("Helvetica", fontsize), fg=foreground, bg=background)
    inhabitants_change.place(x=x2, y=y3 + y2 * 0)
    inhabitants_change1 = tk.Label(text='100', font=("Helvetica", fontsize + 2), fg=foreground, bg=background)
    inhabitants_change1.place(x=x1, y=y1 + y2 * 0)

    revenue_yearly = tk.Label(text="Starting community bankroll", font=("Helvetica", fontsize), bg=background, fg=foreground)
    revenue_yearly.place(x=x2, y=y3 + y2 * 0.5)
    revenue_yearly1 = tk.Label(text='1000', font=("Helvetica", fontsize + 2), fg=foreground, bg=background)
    revenue_yearly1.place(x=x1, y=y1 + y2 * 0.5)

    costs_fix = tk.Label(text="Starting community sentiment", font=("Helvetica", fontsize), bg=background, fg=foreground)
    costs_fix.place(x=x2, y=y3 + y2 * 1)
    costs_fix1 = tk.Label(text='50', font=("Helvetica", fontsize + 2), fg=foreground, bg=background)
    costs_fix1.place(x=x1, y=y1 + y2 * 1)


    # ----------------- GUI AFTER CALCULATION ----------------

    result = tk.Label(text="Costs, per Year", font=("Helvetica", fontsize), bg=background, fg=foreground)
    result.place(x=x2, y=y3 + y2 * 9)
    result1 = tk.StringVar()
    result1 = tk.Entry(textvariable=result1, background='white', foreground='yellow', width=24, bg=background2, fg=foreground2)
    result1.place(x=x1, y=y1 + y2 * 9)

    result2 = tk.Label(text="Revenue, per Year", font=("Helvetica", fontsize), bg=background, fg=foreground)
    result2.place(x=x2, y=y3 + y2 * 10)
    result3 = tk.StringVar()
    result3 = tk.Entry(textvariable=result3, background='white', foreground='yellow', width=24, bg=background2, fg=foreground2)
    result3.place(x=x1, y=y1 + y2 * 10)

    result2 = tk.Label(text="Revenue, per Year", font=("Helvetica", fontsize), bg=background, fg=foreground)
    result2.place(x=x2, y=y3 + y2 * 10)
    result3 = tk.StringVar()
    result3 = tk.Entry(textvariable=result3, background='white', foreground='yellow', width=24, bg=background2, fg=foreground2)
    result3.place(x=x1, y=y1 + y2 * 10)

    result4 = tk.Label(text="Total next 10 years,  excl. installation costs (=)", font=("Helvetica", fontsize), bg=background, fg=foreground)
    result4.place(x=x2, y=y3 + y2 * 13.5)
    result5 = tk.StringVar()
    result5 = tk.Entry(textvariable=result5, background='white', foreground='orange', width=24, bg=background2, fg=foreground2)
    result5.place(x=x1, y=y1 + y2 * 13.5)

    result8 = tk.Label(text="Total next 10 years (=)", font=("Helvetica", fontsize, 'bold'), bg=background, fg=foreground)
    result8.place(x=x2, y=y3 + y2 * 14.7)
    result9 = tk.StringVar()
    result9 = tk.Entry(textvariable=result9, background='white', foreground='yellow', width=24, bg=background2, fg=foreground2)
    result9.place(x=x1, y=y1 + y2 * 14.7)

    canvas = tk.Canvas(width=470, height=0.00001)
    canvas.create_line(0, 0, 470, 0, width=0.00001)
    canvas.place(x=x1, y=y1 + y2 * 14.35)

    login_button = tk.Button(root, text="Calculate Community Effects", font=("Helvetica", 16), command=calculation_clicked, fg='#000000', bg='#FF8C00')
    login_button.place(x=x1, y=y1 + y2 * 8 - 15)

    root.mainloop()





def main():
    print()




possible_ressources = ['pool', 'church', 'bus', 'supermarket', 'train']
ausrichtung = ['flat', 'north', 'east', 'south', 'west']
getdata(possible_ressources, ausrichtung)
