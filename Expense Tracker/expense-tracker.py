from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import sqlite3
import datetime

# function to list all the expenses
def listAllExpenses():
    global dbconnector, data_table
    data_table.delete(*data_table.get_children())
    all_data = dbconnector.execute('SELECT * FROM ExpenseTracker')
    data = all_data.fetchall()
    for val in data:
        data_table.insert('', END, values=val)

# function to view an expense information
def viewExpenseInfo():
    global data_table, dateField, payee, description, amount, modeOfPayment
    if not data_table.selection():
        mb.showerror('No expense selected', 'Please select an expense from the table to view its details')
    else:
        currentSelectedExpense = data_table.item(data_table.focus())
        val = currentSelectedExpense['values']
        expenditureDate = datetime.date(int(val[1][:4]), int(val[1][5:7]), int(val[1][8:]))
        dateField.set_date(expenditureDate)
        payee.set(val[2])
        description.set(val[3])
        amount.set(val[4])
        modeOfPayment.set(val[5])

# function to clear the entries from the entry fields
def clearFields():
    global description, payee, amount, modeOfPayment, dateField, data_table
    todayDate = datetime.datetime.now().date()
    description.set('')
    payee.set('')
    amount.set(0.0)
    modeOfPayment.set('Cash')
    dateField.set_date(todayDate)
    data_table.selection_remove(*data_table.selection())

# function to delete the selected record
def removeExpense():
    global data_table, dbconnector
    if not data_table.selection():
        mb.showerror('No record selected!', 'Please select a record to delete!')
    else:
        currentSelectedExpense = data_table.item(data_table.focus())
        valuesSelected = currentSelectedExpense['values']
        confirmation = mb.askyesno('Are you sure?', f'Are you sure that you want to delete the record of {valuesSelected[2]}')
        if confirmation:
            dbconnector.execute('DELETE FROM ExpenseTracker WHERE ID=%d' % valuesSelected[0])
            dbconnector.commit()
            listAllExpenses()
            mb.showinfo('Record deleted successfully!', 'The record you wanted to delete has been deleted successfully')

# function to delete all the entries
def removeAllExpenses():
    global data_table, dbconnector
    confirmation = mb.askyesno('Are you sure?', 'Are you sure that you want to delete all the expense items from the database?', icon='warning')
    if confirmation:
        data_table.delete(*data_table.get_children())
        dbconnector.execute('DELETE FROM ExpenseTracker')
        dbconnector.commit()
        clearFields()
        listAllExpenses()
        mb.showinfo('All Expenses deleted', 'All the expenses were successfully deleted')
    else:
        mb.showinfo('Ok then', 'The task was aborted and no expense was deleted!')

# function to add an expense
def addAnotherExpense():
    global dateField, payee, description, amount, modeOfPayment, dbconnector
    if not dateField.get() or not payee.get() or not description.get() or not amount.get() or not modeOfPayment.get():
        mb.showerror('Fields empty!', "Please fill all the missing fields before pressing the add button!")
    else:
        dbconnector.execute('INSERT INTO ExpenseTracker (Date, Payee, Description, Amount, ModeOfPayment) VALUES (?, ?, ?, ?, ?)',
                            (dateField.get_date(), payee.get(), description.get(), amount.get(), modeOfPayment.get()))
        dbconnector.commit()
        clearFields()
        listAllExpenses()
        mb.showinfo('Expense added', 'The expense whose details you just entered has been added to the database')

# function to edit the details of an expense
def editExpense():
    global data_table, dateField, amount, description, payee, modeOfPayment
    def editExistingExpense():
        global dateField, amount, description, payee, modeOfPayment, dbconnector, data_table
        currentSelectedExpense = data_table.item(data_table.focus())
        content = currentSelectedExpense['values']
        dbconnector.execute('UPDATE ExpenseTracker SET Date = ?, Payee = ?, Description = ?, Amount = ?, ModeOfPayment = ? WHERE ID = ?',
                            (dateField.get_date(), payee.get(), description.get(), amount.get(), modeOfPayment.get(), content[0]))
        dbconnector.commit()
        clearFields()
        listAllExpenses()
        mb.showinfo('Data edited', 'We have updated the data and stored in the database as you wanted')
        editSelectedButton.destroy()
    if not data_table.selection():
        mb.showerror('No expense selected!', 'You have not selected any expense in the table for us to edit; please do that!')
    else:
        viewExpenseInfo()
        editSelectedButton = Button(frameL3, text="Edit Expense", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=editExistingExpense)
        editSelectedButton.grid(row=0, column=0, sticky=W, padx=50, pady=10)

# function to display the details of selected expense into words
def selectedExpenseToWords():
    global data_table
    if not data_table.selection():
        mb.showerror('No expense selected!', 'Please select an expense from the table for us to read')
    else:
        currentSelectedExpense = data_table.item(data_table.focus())
        val = currentSelectedExpense['values']
        msg = f'Your expense can be read like: \n"You paid {val[4]} to {val[2]} for {val[3]} on {val[1]} via {val[5]}"'
        mb.showinfo('Here\'s how to read your expense', msg)

# function to display the about information
def about():
    mb.showinfo('About', 'This application is a simple expense tracker made using Python and SQLite3 by @PythonistaCoders. \n\nVersion 1.0, ©2024 PythonistaCoders. All rights reserved.')

# connecting to the database
dbconnector = sqlite3.connect('ExpenseTracker.db')
dbcursor = dbconnector.cursor()

# creating the table if it doesn't already exist
try:
    dbcursor.execute('''CREATE TABLE ExpenseTracker (ID INTEGER PRIMARY KEY AUTOINCREMENT, Date DATE, Payee TEXT, Description TEXT, Amount REAL, ModeOfPayment TEXT)''')
except sqlite3.OperationalError:
    pass

# creating the main window
main_win = Tk()
main_win.title('Expense Tracker')
main_win.geometry('800x650')

# setting up frames for the window
frame1 = Frame(main_win, bg="#4CAF50")
frame1.pack(side=TOP, fill=X)

frame2 = Frame(main_win)
frame2.pack(side=TOP, fill=X)

frame3 = Frame(main_win)
frame3.pack(side=BOTTOM, fill=BOTH, expand=True)

frameL1 = Frame(frame2, bg="#C0C0C0")
frameL1.grid(row=0, column=0)

frameL2 = Frame(frame2)
frameL2.grid(row=1, column=0)

frameL3 = Frame(frame2, bg="#C0C0C0")
frameL3.grid(row=2, column=0)

# adding widgets to frame 1
label1 = Label(frame1, text='Your Expense Tracker', font=("Bahnschrift Condensed", "25"), bg="#4CAF50", fg="#FFFFFF")
label1.pack(pady=10)

# adding widgets to frame 2
dateLabel = Label(frameL1, text='Date', font=("Bahnschrift Condensed", "15"), bg="#C0C0C0", fg="#000000")
dateLabel.grid(row=0, column=0, sticky=W, padx=50, pady=10)

dateField = DateEntry(frameL1, width=20, font=("Bahnschrift Condensed", "12"), bg="#90EE90", fg="#000000", borderwidth=2)
dateField.grid(row=0, column=1, sticky=W, padx=10, pady=10)

payeeLabel = Label(frameL1, text='Payee', font=("Bahnschrift Condensed", "15"), bg="#C0C0C0", fg="#000000")
payeeLabel.grid(row=1, column=0, sticky=W, padx=50, pady=10)

payee = StringVar()
payeeEntry = Entry(frameL1, textvariable=payee, font=("Bahnschrift Condensed", "12"), bg="#90EE90", fg="#000000", width=20)
payeeEntry.grid(row=1, column=1, sticky=W, padx=10, pady=10)

descLabel = Label(frameL1, text='Description', font=("Bahnschrift Condensed", "15"), bg="#C0C0C0", fg="#000000")
descLabel.grid(row=2, column=0, sticky=W, padx=50, pady=10)

description = StringVar()
descEntry = Entry(frameL1, textvariable=description, font=("Bahnschrift Condensed", "12"), bg="#90EE90", fg="#000000", width=20)
descEntry.grid(row=2, column=1, sticky=W, padx=10, pady=10)

amtLabel = Label(frameL1, text='Amount', font=("Bahnschrift Condensed", "15"), bg="#C0C0C0", fg="#000000")
amtLabel.grid(row=3, column=0, sticky=W, padx=50, pady=10)

amount = DoubleVar()
amtEntry = Entry(frameL1, textvariable=amount, font=("Bahnschrift Condensed", "12"), bg="#90EE90", fg="#000000", width=20)
amtEntry.grid(row=3, column=1, sticky=W, padx=10, pady=10)

paymentLabel = Label(frameL1, text='Mode of Payment', font=("Bahnschrift Condensed", "15"), bg="#C0C0C0", fg="#000000")
paymentLabel.grid(row=4, column=0, sticky=W, padx=50, pady=10)

modeOfPayment = StringVar()
paymentOptions = ttk.Combobox(frameL1, textvariable=modeOfPayment, font=("Bahnschrift Condensed", "12"), width=18)
paymentOptions['values'] = ['Cash', 'Credit Card', 'Debit Card', 'UPI', 'Net Banking']
paymentOptions.grid(row=4, column=1, sticky=W, padx=10, pady=10)

# adding buttons to frame 3
viewAllButton = Button(frameL3, text="View All Expenses", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=listAllExpenses)
viewAllButton.grid(row=0, column=0, sticky=W, padx=50, pady=10)

viewSelectedButton = Button(frameL3, text="View Selected Expense", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=viewExpenseInfo)
viewSelectedButton.grid(row=0, column=1, sticky=W, padx=50, pady=10)

editSelectedButton = Button(frameL3, text="Edit Selected Expense", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=editExpense)
editSelectedButton.grid(row=0, column=2, sticky=W, padx=50, pady=10)

removeSelectedButton = Button(frameL3, text="Remove Selected Expense", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=removeExpense)
removeSelectedButton.grid(row=1, column=0, sticky=W, padx=50, pady=10)

removeAllButton = Button(frameL3, text="Remove All Expenses", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=removeAllExpenses)
removeAllButton.grid(row=1, column=1, sticky=W, padx=50, pady=10)

addButton = Button(frameL3, text="Add Expense", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=addAnotherExpense)
addButton.grid(row=1, column=2, sticky=W, padx=50, pady=10)

viewInWordsButton = Button(frameL3, text="View Expense in Words", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=selectedExpenseToWords)
viewInWordsButton.grid(row=2, column=0, sticky=W, padx=50, pady=10)

aboutButton = Button(frameL3, text="About", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=about)
aboutButton.grid(row=2, column=1, sticky=W, padx=50, pady=10)

exitButton = Button(frameL3, text="Exit", font=("Bahnschrift Condensed", "13"), width=30, bg="#90EE90", fg="#000000", relief=GROOVE, activebackground="#008000", activeforeground="#98FB98", command=main_win.destroy)
exitButton.grid(row=2, column=2, sticky=W, padx=50, pady=10)

# adding a treeview widget to display the data
data_table = ttk.Treeview(frame2, column=('column1', 'column2', 'column3', 'column4', 'column5', 'column6'), show='headings', height=20)
data_table.heading('#1', text='ID')
data_table.heading('#2', text='Date')
data_table.heading('#3', text='Payee')
data_table.heading('#4', text='Description')
data_table.heading('#5', text='Amount')
data_table.heading('#6', text='Mode of Payment')
data_table.grid(row=0, column=1, rowspan=2)

# auto adjusting the width of columns
for col in data_table['column']:
    data_table.column(col, width=70)

# viewing all the expenses initially when the program starts
listAllExpenses()

# running the main loop
main_win.mainloop()
