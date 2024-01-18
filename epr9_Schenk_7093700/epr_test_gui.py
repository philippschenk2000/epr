import tkinter as tk
import warnings
from tkinter.messagebox import showinfo

import matplotlib
from ttkwidgets.autocomplete import AutocompleteCombobox

matplotlib.use('TkAgg')
warnings.filterwarnings("ignore")


def getdata(possible_ressources):

    def calculation_clicked():
        global existing_ressources, existing_ressources1, new_ressources, new_ressources1
        new_ressources = str(new_ressources1.get())
        existing_ressources = str(existing_ressources1.get())
        ressources_now = str(ressources_now0.get())
        inhabitants_now = str(inhabitants_now1.get())
        bankroll_now = str(bankroll_now1.get())
        sentiment_now = str(sentiment_now1.get())
        if new_ressources != '':
            msg = f' The influence of a new ressource ({new_ressources}) will be calculated'
        else:
            msg = f' The influence of deleting an existing ressource ({existing_ressources}) will be calculated'
        showinfo(title='Information', message=msg)
        # CASE 1: NEW RESSOURCE IS ADDED
        if new_ressources != '' and new_ressources != '_none':
            data = add_new_ressource(new_ressources, ressources_now, inhabitants_now, bankroll_now, sentiment_now)
            #[ressources_now, costs, revenue, inhabitants_now, bankroll_now, sentiment_now, profit_next_years]
            ressources_now0.delete(0, 200)
            ressources_now0.insert(0, data[0])
            costs_now1.delete(0, 200)
            costs_now1.insert(0, data[1])
            revenue_now1.delete(0, 200)
            revenue_now1.insert(0, data[2])
            inhabitants_now1.delete(0, 200)
            inhabitants_now1.insert(0, data[3])
            bankroll_now1.delete(0, 200)
            bankroll_now1.insert(0, data[4])
            sentiment_now1.delete(0, 200)
            sentiment_now1.insert(0, data[5])
            total1.delete(0, 200)
            total1.insert(0, data[6])
        # CASE 1: NEW RESSOURCE IS ADDED
        elif existing_ressources != '' and existing_ressources != '_none':
            data = delete_existing_ressource(existing_ressources, ressources_now, inhabitants_now, bankroll_now, sentiment_now)
            ressources_now0.delete(0, 200)
            ressources_now0.insert(0, data[0])
            costs_now1.delete(0, 200)
            costs_now1.insert(0, data[1])
            revenue_now1.delete(0, 200)
            revenue_now1.insert(0, data[2])
            inhabitants_now1.delete(0, 200)
            inhabitants_now1.insert(0, data[3])
            bankroll_now1.delete(0, 200)
            bankroll_now1.insert(0, data[4])
            sentiment_now1.delete(0, 200)
            sentiment_now1.insert(0, data[5])
            total1.delete(0, 200)
            total1.insert(0, data[6])



    root = tk.Tk()
    background = '#FFFFCC'
    foreground = '#000000'
    cellcolour = '#FFDF00'
    background2 = '#FFDF00'
    foreground2 = '#000000'
    fontsize = 12
    root.geometry('1920x1080')
    root.resizable(True, True)
    root.title('Your Community Effect Calculator')
    root['bg'] = background

    global new_ressources, new_ressources1, existing_ressources, existing_ressources1

    x1 = 50
    x2 = 350
    y1 = 70
    y2 = 45
    y3 = 70

    # ----------------- GUI BEFORE CALCULATION ----------------

    schrift = tk.Label(text="Here you can calculate how your community likes your changes!", font=("Helvetica", 13, 'bold'), bg=background, fg=foreground)
    schrift.place(x=x1, y=24)


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

    new_ressources = tk.Label(text="Add a new ressource", font=("Helvetica", fontsize), bg=background, fg=foreground)
    new_ressources.place(x=x2, y=y3 + y2 * 2)
    new_ressources1 = AutocompleteCombobox(root, completevalues=possible_ressources, foreground='white', width=22, state='readonly')
    new_ressources1.place(x=x1, y=y1 + y2 * 2)

    existing_ressources = tk.Label(text="Delete an existing ressource", font=("Helvetica", fontsize), bg=background, fg=foreground)
    existing_ressources.place(x=x2, y=y3 + y2 * 3)
    existing_ressources1 = AutocompleteCombobox(root, completevalues=possible_ressources, foreground='white', width=22, state='readonly')
    existing_ressources1.place(x=x1, y=y1 + y2 * 3)


    # ----------------- GUI AFTER CALCULATION ----------------

    ressources_now = tk.Label(text="Ressources in your community", font=("Helvetica", fontsize), bg=background, fg=foreground)
    ressources_now.place(x=x2, y=y3 + y2 * 8)
    ressources_now0 = tk.StringVar()
    ressources_now0 = tk.Entry(textvariable=ressources_now0, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    ressources_now0.place(x=x1, y=y1 + y2 * 8)
    ressources_now0.insert(0, str('none yet'))

    costs_now = tk.Label(text="Fixed costs", font=("Helvetica", fontsize), bg=background, fg=foreground)
    costs_now.place(x=x2, y=y3 + y2 * 9)
    costs_now1 = tk.StringVar()
    costs_now1 = tk.Entry(textvariable=costs_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    costs_now1.place(x=x1, y=y1 + y2 * 9)

    revenue_now = tk.Label(text="Fixed savings", font=("Helvetica", fontsize), bg=background, fg=foreground)
    revenue_now.place(x=x2, y=y3 + y2 * 10)
    revenue_now1 = tk.StringVar()
    revenue_now1 = tk.Entry(textvariable=revenue_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    revenue_now1.place(x=x1, y=y1 + y2 * 10)

    inhabitants_now = tk.Label(text="Updated community inhabitants", font=("Helvetica", fontsize), bg=background, fg=foreground)
    inhabitants_now.place(x=x2, y=y3 + y2 * 11)
    inhabitants_now1 = tk.StringVar()
    inhabitants_now1 = tk.Entry(textvariable=inhabitants_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    inhabitants_now1.place(x=x1, y=y1 + y2 * 11)
    inhabitants_now1.insert(0, str(100))

    bankroll_now = tk.Label(text="Updated community bankroll", font=("Helvetica", fontsize), bg=background, fg=foreground)
    bankroll_now.place(x=x2, y=y3 + y2 * 12)
    bankroll_now1 = tk.StringVar()
    bankroll_now1 = tk.Entry(textvariable=bankroll_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    bankroll_now1.place(x=x1, y=y1 + y2 * 12)
    bankroll_now1.insert(0, str(1000))

    sentiment_now = tk.Label(text="Updated community sentiment", font=("Helvetica", fontsize), bg=background, fg=foreground)
    sentiment_now.place(x=x2, y=y3 + y2 * 13)
    sentiment_now1 = tk.StringVar()
    sentiment_now1 = tk.Entry(textvariable=sentiment_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    sentiment_now1.place(x=x1, y=y1 + y2 * 13)
    sentiment_now1.insert(0, str(50))


    total = tk.Label(text="Total next 10 years (=)", font=("Helvetica", fontsize, 'bold'), bg=background, fg=foreground)
    total.place(x=x2, y=y3 + y2 * 14.7)
    total1 = tk.StringVar()
    total1 = tk.Entry(textvariable=total1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    total1.place(x=x1, y=y1 + y2 * 14.7)

    canvas = tk.Canvas(width=470, height=0.00001)
    canvas.create_line(0, 0, 470, 0, width=0.00001)
    canvas.place(x=x1, y=y1 + y2 * 14.35)

    login_button = tk.Button(root, text="Calculate Community Effects", font=("Helvetica", 16), command=calculation_clicked, fg='#000000', bg='#FF8C00')
    login_button.place(x=x1, y=y1 + y2 * 7 - 15)

    root.mainloop()


def add_new_ressource(new_ressources, ressources_now, inhabitants_now, bankroll_now, sentiment_now):
    costs_fix = 0
    yearly_revenue = 0

    if new_ressources not in ressources_now:
        if 'none yet' in ressources_now:
            ressources_now = ressources_now.replace('none yet', '') + new_ressources
        else:
            ressources_now = ressources_now + ', ' + new_ressources
        if 'church' in ressources_now:
            costs_fix = costs_fix + 500
            yearly_revenue = yearly_revenue + -10
            inhabitants_now = int(inhabitants_now) + -15
            sentiment_now = int(sentiment_now) + -2
        if 'supermarket' in ressources_now:
            costs_fix = costs_fix + 100
            yearly_revenue = yearly_revenue + 20
            inhabitants_now = int(inhabitants_now) + 10
            sentiment_now = int(sentiment_now) + 15
        if 'pool' in ressources_now:
            costs_fix = costs_fix + 40
            yearly_revenue = yearly_revenue + 10
            inhabitants_now = int(inhabitants_now) + 2
            sentiment_now = int(sentiment_now) + 5
        if 'train' in ressources_now:
            costs_fix = costs_fix + 400
            yearly_revenue = yearly_revenue + 100
            inhabitants_now = int(inhabitants_now) + 20
            sentiment_now = int(sentiment_now) + 5
        if 'bus' in ressources_now:
            costs_fix = costs_fix + 80
            yearly_revenue = yearly_revenue + 10
            inhabitants_now = int(inhabitants_now) + 5
            sentiment_now = int(sentiment_now) + 5

    bankroll_now = int(bankroll_now) - costs_fix
    profit_next_years = yearly_revenue * 10 - costs_fix
    return [ressources_now, costs_fix, yearly_revenue, inhabitants_now, bankroll_now, sentiment_now, profit_next_years]


def delete_existing_ressource(existing_ressource, ressources_now, inhabitants_now, bankroll_now, sentiment_now):
    print(existing_ressource, ressources_now, inhabitants_now, bankroll_now, sentiment_now)
    costs_fix = 0
    yearly_revenue = 0

    if existing_ressource in ressources_now:
        if ', ' in ressources_now:
            ressources_now = ressources_now.replace(', ' + str(existing_ressource), '')
            ressources_now = ressources_now.replace(str(existing_ressource), '')
        else:
            ressources_now = existing_ressource
        if 'church' in ressources_now:
            costs_fix = costs_fix + 500
            yearly_revenue = yearly_revenue + -10
            inhabitants_now = int(inhabitants_now) + -15
            sentiment_now = int(sentiment_now) + -2
        if 'supermarket' in ressources_now:
            costs_fix = costs_fix + 100
            yearly_revenue = yearly_revenue + 20
            inhabitants_now = int(inhabitants_now) + 10
            sentiment_now = int(sentiment_now) + 15
        if 'pool' in ressources_now:
            costs_fix = costs_fix + 40
            yearly_revenue = yearly_revenue + 10
            inhabitants_now = int(inhabitants_now) + 2
            sentiment_now = int(sentiment_now) + 5
        if 'train' in ressources_now:
            costs_fix = costs_fix + 400
            yearly_revenue = yearly_revenue + 100
            inhabitants_now = int(inhabitants_now) + 20
            sentiment_now = int(sentiment_now) + 5
        if 'bus' in ressources_now:
            costs_fix = costs_fix + 80
            yearly_revenue = yearly_revenue + 10
            inhabitants_now = int(inhabitants_now) + 5
            sentiment_now = int(sentiment_now) + 5

    print(ressources_now)
    bankroll_now = int(bankroll_now) - costs_fix
    profit_next_years = yearly_revenue * 10 - costs_fix
    return [ressources_now, costs_fix, yearly_revenue, inhabitants_now, bankroll_now, sentiment_now, profit_next_years]


possible_ressources = ['_none', 'pool', 'church', 'bus', 'supermarket', 'train']
getdata(possible_ressources)
