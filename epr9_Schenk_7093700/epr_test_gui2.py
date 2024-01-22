""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk 7001303, Lautsch"


import tkinter as tk
import warnings
from tkinter.messagebox import showinfo

from ttkwidgets.autocomplete import AutocompleteCombobox

warnings.filterwarnings("ignore")


def getdata(possible_ressources):
    """ This function manages the GUI for the user on a local machine.

    """

    def calculation_clicked():
        """ This function starts after the calculation button has been triggered and calls the calculation methods.

        """
        # global is allowed in this epr exercise!
        global existing_ressources, existing_ressources1, new_ressources, new_ressources1

        # get the entry data given by the user
        new_ressources = str(new_ressources1.get())
        existing_ressources = str(existing_ressources1.get())
        ressources_now = str(ressources_now0.get())
        inhabitants_now = str(inhabitants_now1.get())
        bankroll_now = str(bankroll_now1.get())
        sentiment_now = str(sentiment_now1.get())

        # let the user know calculations have started
        if new_ressources != '':
            msg = f' The influence of a new ressource ({new_ressources}) will be calculated'
        else:
            msg = f' The influence of deleting an existing ressource ({existing_ressources}) will be calculated'
        showinfo(title='Information', message=msg)

        # CASE 1: new ressource will be deleted
        if new_ressources != '' and new_ressources != '_none':
            data = add_new_ressource(new_ressources, ressources_now, inhabitants_now, bankroll_now, sentiment_now)

            # insert the new values into the entry fields for the user
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

        # CASE 2: existing ressources will be deleted
        elif existing_ressources != '' and existing_ressources != '_none':
            data = delete_existing_ressource(existing_ressources, ressources_now, inhabitants_now, bankroll_now, sentiment_now)

            # insert the new values into the entry fields for the user
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


    # design settings for the GUI
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


    # global is allowed in this epr exercise!
    global new_ressources, new_ressources1, existing_ressources, existing_ressources1

    # coordinates for the labels, buttons and entry fields (this makes it easy to change position)
    x1 = 50
    x2 = 350
    y1 = 70
    y2 = 45
    y3 = 70

    # ----------------- GUI BEFORE CALCULATION ----------------

    schrift = tk.Label(text="Here you can calculate how your community likes your changes!", font=("Helvetica", 13, 'bold'), bg=background, fg=foreground)
    schrift.place(x=x1, y=24)

    # inhabitants of community
    inhabitants_change = tk.Label(text="Starting community inhabitants", font=("Helvetica", fontsize), fg=foreground, bg=background)
    inhabitants_change.place(x=x2, y=y3 + y2 * 0)
    inhabitants_change1 = tk.Label(text='100', font=("Helvetica", fontsize + 2), fg=foreground, bg=background)
    inhabitants_change1.place(x=x1, y=y1 + y2 * 0)

    # starting bankroll of community
    revenue_yearly = tk.Label(text="Starting community bankroll", font=("Helvetica", fontsize), bg=background, fg=foreground)
    revenue_yearly.place(x=x2, y=y3 + y2 * 0.5)
    revenue_yearly1 = tk.Label(text='1000', font=("Helvetica", fontsize + 2), fg=foreground, bg=background)
    revenue_yearly1.place(x=x1, y=y1 + y2 * 0.5)

    # starting sentiment of community
    costs_fix = tk.Label(text="Starting community sentiment", font=("Helvetica", fontsize), bg=background, fg=foreground)
    costs_fix.place(x=x2, y=y3 + y2 * 1)
    costs_fix1 = tk.Label(text='50', font=("Helvetica", fontsize + 2), fg=foreground, bg=background)
    costs_fix1.place(x=x1, y=y1 + y2 * 1)

    # choices of new possible ressources
    new_ressources = tk.Label(text="Add a new ressource", font=("Helvetica", fontsize), bg=background, fg=foreground)
    new_ressources.place(x=x2, y=y3 + y2 * 2)
    new_ressources1 = AutocompleteCombobox(root, completevalues=possible_ressources, foreground='white', width=22, state='readonly')
    new_ressources1.place(x=x1, y=y1 + y2 * 2)

    # choices of deletable possible ressources
    existing_ressources = tk.Label(text="Delete an existing ressource", font=("Helvetica", fontsize), bg=background, fg=foreground)
    existing_ressources.place(x=x2, y=y3 + y2 * 3)
    existing_ressources1 = AutocompleteCombobox(root, completevalues=possible_ressources, foreground='white', width=22, state='readonly')
    existing_ressources1.place(x=x1, y=y1 + y2 * 3)


    # ----------------- GUI AFTER CALCULATION ----------------

    # updated ressources in the community
    ressources_now = tk.Label(text="Ressources in your community", font=("Helvetica", fontsize), bg=background, fg=foreground)
    ressources_now.place(x=x2, y=y3 + y2 * 8)
    ressources_now0 = tk.StringVar()
    ressources_now0 = tk.Entry(textvariable=ressources_now0, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    ressources_now0.place(x=x1, y=y1 + y2 * 8)
    ressources_now0.insert(0, str('none yet'))

    # fixed costs for the new ressource
    costs_now = tk.Label(text="Fixed costs", font=("Helvetica", fontsize), bg=background, fg=foreground)
    costs_now.place(x=x2, y=y3 + y2 * 9)
    costs_now1 = tk.StringVar()
    costs_now1 = tk.Entry(textvariable=costs_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    costs_now1.place(x=x1, y=y1 + y2 * 9)

    # fixed savings for the new/existing ressource
    revenue_now = tk.Label(text="Fixed savings", font=("Helvetica", fontsize), bg=background, fg=foreground)
    revenue_now.place(x=x2, y=y3 + y2 * 10)
    revenue_now1 = tk.StringVar()
    revenue_now1 = tk.Entry(textvariable=revenue_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    revenue_now1.place(x=x1, y=y1 + y2 * 10)

    # updated change of inhabitants for community
    inhabitants_now = tk.Label(text="Updated community inhabitants", font=("Helvetica", fontsize), bg=background, fg=foreground)
    inhabitants_now.place(x=x2, y=y3 + y2 * 11)
    inhabitants_now1 = tk.StringVar()
    inhabitants_now1 = tk.Entry(textvariable=inhabitants_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    inhabitants_now1.place(x=x1, y=y1 + y2 * 11)
    inhabitants_now1.insert(0, str(100))

    # updated change of bankroll for community
    bankroll_now = tk.Label(text="Updated community bankroll", font=("Helvetica", fontsize), bg=background, fg=foreground)
    bankroll_now.place(x=x2, y=y3 + y2 * 12)
    bankroll_now1 = tk.StringVar()
    bankroll_now1 = tk.Entry(textvariable=bankroll_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    bankroll_now1.place(x=x1, y=y1 + y2 * 12)
    bankroll_now1.insert(0, str(1000))

    # updated change of sentiment in community
    sentiment_now = tk.Label(text="Updated community sentiment", font=("Helvetica", fontsize), bg=background, fg=foreground)
    sentiment_now.place(x=x2, y=y3 + y2 * 13)
    sentiment_now1 = tk.StringVar()
    sentiment_now1 = tk.Entry(textvariable=sentiment_now1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    sentiment_now1.place(x=x1, y=y1 + y2 * 13)
    sentiment_now1.insert(0, str(50))


    # total 10-year profit of all existing community ressources in portfolio
    total = tk.Label(text="Total profit of all existing ressources, next 10 years (=)", font=("Helvetica", fontsize, 'bold'), bg=background, fg=foreground)
    total.place(x=x2, y=y3 + y2 * 14.7)
    total1 = tk.StringVar()
    total1 = tk.Entry(textvariable=total1, background='white', foreground='yellow', width=30, bg=background2, fg=foreground2)
    total1.place(x=x1, y=y1 + y2 * 14.7)

    # adds a beautiful line
    canvas = tk.Canvas(width=470, height=0.00001)
    canvas.create_line(0, 0, 470, 0, width=0.00001)
    canvas.place(x=x1, y=y1 + y2 * 14.35)

    # creates the button which will trigger the calculations
    login_button = tk.Button(root, text="Calculate Community Effects", font=("Helvetica", 16), command=calculation_clicked, fg='#000000', bg='#FF8C00')
    login_button.place(x=x1, y=y1 + y2 * 7 - 15)

    root.mainloop()


class Ressource:
    def __init__(self):
        self.costs_fix = 0
        self.yearly_revenue = 0
        self.inhabitants_change = 0
        self.sentiment_change = 0

    def apply_effects(self, inhabitants_now, sentiment_now, costs_fix):
        # Convert to integers if they are strings
        inhabitants_now = int(inhabitants_now)
        sentiment_now = int(sentiment_now)
        costs_fix = int(costs_fix)

        # Perform the arithmetic operations
        inhabitants_now += self.inhabitants_change
        sentiment_now += self.sentiment_change
        costs_fix -= self.costs_fix
        profit_next_years = self.yearly_revenue * 10 - self.costs_fix

        return inhabitants_now, sentiment_now, costs_fix, profit_next_years

class Church(Ressource):
    def __init__(self):
        super().__init__()
        self.costs_fix = 500
        self.yearly_revenue = -10
        self.inhabitants_change = -15
        self.sentiment_change = -2

class Supermarket(Ressource):
    def __init__(self):
        super().__init__()
        self.costs_fix = 100
        self.yearly_revenue = 20
        self.inhabitants_change = 10
        self.sentiment_change = 15

class Pool(Ressource):
    def __init__(self):
        super().__init__()
        self.costs_fix = 40
        self.yearly_revenue = 10
        self.inhabitants_change = 2
        self.sentiment_change = 5

class Bus(Ressource):
    def __init__(self):
        super().__init__()
        self.costs_fix = 80
        self.yearly_revenue = 10
        self.inhabitants_change = 5
        self.sentiment_change = 5

class Train(Ressource):
    def __init__(self):
        super().__init__()
        self.costs_fix = 400
        self.yearly_revenue = 100
        self.inhabitants_change = 20
        self.sentiment_change = 5


def add_new_ressource(new_resource, resources_now, inhabitants_now, bankroll_now, sentiment_now):
    """ This function calculates the effects for adding a new ressource in the community.

    """
    resource_classes = {'church': Church, 'supermarket': Supermarket, 'pool': Pool, 'train': Train, 'bus': Bus}
    if new_resource not in resources_now:
        # Replace 'none yet' if it's the first resource
        if 'none yet' in resources_now:
            resources_now = resources_now.replace('none yet', new_resource)
        else:
            resources_now += f', {new_resource}' if resources_now else new_resource
        print(resources_now)
        # Create an instance of the resource and apply its effects
        if 'church' in resources_now:
            resource = resource_classes['church']()
            inhabitants_now, sentiment_now, costs_fix, profit_next_years = resource.apply_effects(inhabitants_now, sentiment_now, costs_fix)
        if 'pool' in resources_now:
            resource = resource_classes['pool']()
            inhabitants_now, sentiment_now, bankroll_now, profit_next_years = resource.apply_effects(inhabitants_now, sentiment_now, costs_fix)
        if 'bus' in resources_now:
            resource = resource_classes['bus']()
            inhabitants_now, sentiment_now, bankroll_now, profit_next_years = resource.apply_effects(inhabitants_now, sentiment_now, costs_fix)
        if 'train' in resources_now:
            resource = resource_classes['train']()
            inhabitants_now, sentiment_now, bankroll_now, profit_next_years = resource.apply_effects(inhabitants_now, sentiment_now, costs_fix)
        return [resources_now, resource.costs_fix, resource.yearly_revenue, inhabitants_now, bankroll_now, sentiment_now, profit_next_years]

    return [resources_now, 0, 0, inhabitants_now, bankroll_now, sentiment_now, 0]


def delete_existing_ressource(existing_ressource, ressources_now, inhabitants_now, bankroll_now, sentiment_now):
    """ This function calculates the effects for deleting an existing ressource in the community.

    """
    resource_classes = {'church': Church, 'supermarket': Supermarket, 'pool': Pool, 'train': Train, 'bus': Bus}
    # be careful with duplicates in the existing portfolio of ressources
    if existing_ressource in ressources_now:
        # kick them out of the portfolio
        if ', ' in ressources_now:
            ressources_now = ressources_now.replace(', ' + str(existing_ressource), '')
            ressources_now = ressources_now.replace(str(existing_ressource), '')
        else:
            ressources_now = existing_ressource

        # Create an instance of the resource and apply its effects
        resource = resource_classes[existing_ressource]()
        inhabitants_now, sentiment_now, bankroll_now, profit_next_years = resource.apply_effects(inhabitants_now, sentiment_now, bankroll_now)
        return [ressources_now, resource.costs_fix, resource.yearly_revenue, inhabitants_now, bankroll_now, sentiment_now, profit_next_years]

    return [ressources_now, 0, 0, inhabitants_now, bankroll_now, sentiment_now, 0]


# START: set the choices for new/existing ressources in your community, then start GUI
possible_ressources = ['_none', 'pool', 'church', 'bus', 'supermarket', 'train']
getdata(possible_ressources)
