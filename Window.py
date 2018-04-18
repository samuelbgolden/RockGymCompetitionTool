from tkinter import *
from tkinter import font
from tkinter.ttk import Notebook
from string import ascii_uppercase
import csv
from Route import Route
from collections import defaultdict
from EntryWithPlaceholder import EntryWithPlaceholder


def not_implemented():  # using this for all the menubar functions that haven't been implemented yet
    print("This hasn't been implemented yet!")

def update_competitor_table():
    for widget in competitorsTable.winfo_children():
        widget.destroy()

    try:
        csvfile = open(dynamicFileName, 'r')
        csvfile.close()
    except FileNotFoundError:
        return

    with open(dynamicFileName, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for rowNum, row in enumerate(reader):
            if rowNum % 2 == 0:
                tableRowBG = 'gray'
            else:
                tableRowBG = 'dark gray'
            Label(competitorsTable, bg=tableRowBG, width=FNAME_FIELD_WIDTH, text=row['fname']).grid(row=rowNum, column=0, sticky='NSW')
            Label(competitorsTable, bg=tableRowBG, width=LNAME_FIELD_WIDTH, text=row['lname']).grid(row=rowNum, column=1, sticky='NSW')
            Label(competitorsTable, bg=tableRowBG, width=LEVEL_FIELD_WIDTH, text=row['level']).grid(row=rowNum, column=2, sticky='NSW')
            Label(competitorsTable, bg=tableRowBG, width=SEX_FIELD_WIDTH, text=row['sex']).grid(row=rowNum, column=3, sticky='NSW')
            Label(competitorsTable, bg=tableRowBG, width=AGE_FIELD_WIDTH, text=row['age']).grid(row=rowNum, column=4, sticky='NSW')
            Label(competitorsTable, bg=tableRowBG, width=SCORE_FIELD_WIDTH, text=row['score']).grid(row=rowNum, column=5, sticky='NSW')
            Label(competitorsTable, bg=tableRowBG, width=ROUTES_FIELD_WIDTH, text='<<routes>>').grid(row=rowNum, column=6, sticky='NSW')
            Button(competitorsTable, bg='red', fg='white', height=1, text='X', command=lambda i=rowNum: delete_competitor(i)
                   ).grid(row=rowNum, column=7)


def register_competitor():
    writeHeadersFlag = False
    try:
        csvfile = open(dynamicFileName, 'r')
        if sum(1 for row in csvfile) == 0:
            writeHeadersFlag = True
        csvfile.close()
    except FileNotFoundError:
        writeHeadersFlag = True

    with open(dynamicFileName, 'a', newline='') as csvfile:
        colnames = ['fname', 'lname', 'level', 'sex', 'age', 'score', 'route1', 'route2', 'route3', 'route4', 'route5']
        writer = csv.DictWriter(csvfile, fieldnames=colnames)

        if writeHeadersFlag:
            writer.writeheader()

        writer.writerow({'fname': fnameEntry.get(),
                         'lname': lnameEntry.get(),
                         'level': levelEntry.get(),
                         'sex': sexEntry.get(),
                         'age': ageEntry.get(),
                         'score': 0,
                         'route1': '0',
                         'route2': '0',
                         'route3': '0',
                         'route4': '0',
                         'route5': '0'})
    update_competitor_table()  # end func definition


def delete_competitor(delLine):  # this function taken from sam's SO question on the topic of csv file removal
    with open(dynamicFileName, 'r+') as csvfile:  # assume first VALUE is zero indexed when calling this function (
        for i in range(delLine+2):
            pos = csvfile.tell()
            csvfile.readline()
        rest = csvfile.read()
        csvfile.seek(pos)
        csvfile.truncate()
        csvfile.write(rest)
    update_competitor_table()


def show_filtered_competitors(startingletter):
    columns = defaultdict(list)
    with open(dynamicFileName) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)  # LEARN HOW THESE LOOPS WORK
    lastnames = columns['lname']  # https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module

    filterednamesindeces = [index for index, name in enumerate(lastnames) if (name[0].upper() == startingletter)]

    buttonwidth = len(max(map(lambda a, b: a + b, columns['fname'], columns['lname']), key=len)) + 1
    # calculates the length of the longest name in the competitor list and adds 1 to it

    i = 0
    if len(filterednamesindeces) > 0:
        for i in range(0, len(filterednamesindeces)):
            Button(filteredNameFrame, text="{}, {}".format(columns['lname'][filterednamesindeces[i]], columns['fname'][filterednamesindeces[i]]),
                   height=2, width=buttonwidth).grid(column=i % 10, row=i // 10)

    Button(filteredNameFrame, text='BACK', bg='black', fg='white', command=show_block_letters).grid(column=i+1, row=i+1)

    competitorSelectionFrame.grid_remove()
    filteredNameFrame.grid()


def show_block_letters():
    filteredNameFrame.grid_remove()
    for widget in filteredNameFrame.winfo_children():
        widget.destroy()
    competitorSelectionFrame.grid()

dynamicFileName = 'currentcomp.csv'
FNAME_FIELD_WIDTH = 30
LNAME_FIELD_WIDTH = 30
LEVEL_FIELD_WIDTH = 10
SEX_FIELD_WIDTH = 3
AGE_FIELD_WIDTH = 4
SCORE_FIELD_WIDTH = 7
ROUTES_FIELD_WIDTH = 20

window = Tk()  # tkinter object

mainPanelFont = font.Font(family='fixedsys', size=20)  # defines a font
quickEntryBigLetterFont = font.Font(family='Courier', size=28, weight='bold')
bigNumberDisplay = font.Font(family='Sitka', size=22)
standardBG = '#2c2c2c'
window.configure(bg=standardBG)


menubar = Menu(window)  # menu bar object ############################################################################

filemenu = Menu(menubar, tearoff=0)  # File section of menu bar
filemenu.add_command(label="New Competition", command=not_implemented)
filemenu.add_command(label="Save", command=not_implemented)
filemenu.add_command(label="Save as...", command=not_implemented)
filemenu.add_separator()
filemenu.add_command(label="Open", command=not_implemented)
filemenu.add_command(label="Export", command=not_implemented)
filemenu.add_command(label="Print", command=not_implemented)
filemenu.add_separator()
filemenu.add_command(label="Close", command=not_implemented)
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)  # this is when the menu bar object gets displayed in the window object
# END menu bar object END ############################################################################################

notebook = Notebook(window)  # define notebook (thing with tabs at the top)

entryTab = Frame(window, bg=standardBG)  # widget containing the 2 frames, second tab in notebook
entryTab.pack(fill=BOTH, expand=1)  # packs entry tab in the window object

competitorSelectionFrame = LabelFrame(entryTab, text="Competitors", bg=standardBG, font=mainPanelFont)
filteredNameFrame = LabelFrame(entryTab, text="Competitors", bg=standardBG, font=mainPanelFont)
routesFrame = LabelFrame(entryTab, text="Routes", bg=standardBG, font=mainPanelFont)  # second pane
filteredNameFrame.grid(row=0, column=0)
competitorSelectionFrame.grid(row=0, column=0)
routesFrame.grid(row=1, column=0)
filteredNameFrame.grid_remove()

competitionTab = PanedWindow(window, bg=standardBG, sashwidth=8)

standingsFrame = LabelFrame(competitionTab, text="Standings", bg=standardBG, font=mainPanelFont)
competitorsFrame = LabelFrame(competitionTab, text="Competitors", bg=standardBG, font=mainPanelFont)
competitionTab.add(standingsFrame)
competitionTab.add(competitorsFrame)


blockLetterButtons = {}
for i in range(0, 26):
    blockLetterButtons[i] = Button(competitorSelectionFrame, text=ascii_uppercase[i], relief=FLAT,
                                   activebackground='white', bg='black', fg='white', font=quickEntryBigLetterFont,
                                   height=1, width=3, command=lambda i=i: show_filtered_competitors(ascii_uppercase[i]))
    blockLetterButtons[i].grid(column=i % 13, row=i//13)    # the lambda statement generates a function for each button
                                                            # that has no parameters, and takes the instance of i in
                                                            # the for loop during instantiation immediately
routeObjects = {}
for i in range(1, 51):
    routeObjects[i] = Route(i, (i*100), 0)

for i in range(0, 50):
    col = i // 10
    row = i % 10
    r = routeObjects[i+1]
    routeNumLabel = Label(routesFrame, font=bigNumberDisplay, bg=standardBG, text=r.num)
    routesBtnMinus = Button(routesFrame, relief=FLAT, bg=standardBG, command=r.decrement_attempts)
    routeAttemptsLabel = Label(routesFrame, textvariable=r.attempts, font=bigNumberDisplay, bg=standardBG)
    routesBtnPlus = Button(routesFrame, relief=FLAT, bg=standardBG, command=r.increment_attempts)
    routesBtnMinus.config(image=r.minus_icon)
    routesBtnPlus.config(image=r.plus_icon)
    routeNumLabel.grid(row=row, column=0+(col*5))
    routesBtnMinus.grid(row=row, column=1+(col*5))
    routeAttemptsLabel.grid(row=row, column=2+(col*5))
    routesBtnPlus.grid(row=row, column=3+(col*5))       # one below to for loop above handles route buttons
    Label(routesFrame, text="\t", bg=standardBG).grid(row=row, column=4+(col*5))

fnameEntry = EntryWithPlaceholder(competitorsFrame, width=FNAME_FIELD_WIDTH, placeholder='first')
lnameEntry = EntryWithPlaceholder(competitorsFrame, width=LNAME_FIELD_WIDTH, placeholder='last')
levelEntry = EntryWithPlaceholder(competitorsFrame, width=LEVEL_FIELD_WIDTH, placeholder='level')
sexEntry = EntryWithPlaceholder(competitorsFrame, width=SEX_FIELD_WIDTH, placeholder='sex')
ageEntry = EntryWithPlaceholder(competitorsFrame, width=AGE_FIELD_WIDTH, placeholder='age')
registerButton = Button(competitorsFrame, text="Register", bg='blue', fg='white', command=register_competitor)
fnameEntry.grid(row=1, column=0, sticky='W')
lnameEntry.grid(row=1, column=1, sticky='W')
levelEntry.grid(row=1, column=2, sticky='W')
sexEntry.grid(row=1, column=3, sticky='W')
ageEntry.grid(row=1, column=4, sticky='W')
Label(competitorsFrame, text='0', width=SCORE_FIELD_WIDTH, bg='white').grid(row=1, column=5, sticky='W')
Label(competitorsFrame, text='none', width=ROUTES_FIELD_WIDTH, bg='white').grid(row=1, column=6, sticky='W')

registerButton.grid(row=1, column=7, sticky='W')  # here to fnameEntry declaration above handles the registration form

competitorsTable = Frame(competitorsFrame, bg=standardBG)
competitorsTable.grid(row=2, column=0, columnspan=8)

notebook.add(competitionTab, text='Competition')
notebook.add(entryTab, text='Score Entry')
notebook.pack()

update_competitor_table()
window.mainloop()  # runs main loop of the tkinter object
