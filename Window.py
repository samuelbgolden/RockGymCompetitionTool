from tkinter import *
from tkinter import font

window = Tk()  # tkinter object


def not_implemented():  # using this for all the menubar functions that haven't been implemented yet
    print("This hasn't been implemented yet!")


menubar = Menu(window)  # menu bar object

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

mainPanel = PanedWindow(window, sashwidth=8, bg='dark gray')  # object that contains the three resizeable panes
mainPanel.pack(fill=BOTH, expand=1)  # puts the pack in the window object

mainPanelFont = font.Font(family='fixedsys', size=12)  # defines a font

f1 = LabelFrame(mainPanel, text="Competitors", font=mainPanelFont, width=400, height=600)  # first pane
f2 = LabelFrame(mainPanel, text="Routes", font=mainPanelFont, width=400, height=600)  # second pane
f3 = LabelFrame(mainPanel, text="Competition", font=mainPanelFont, width=400, height=600)  # third pane
mainPanel.add(f1)
mainPanel.add(f2)
mainPanel.add(f3)  # adds the panes defined in lines 30-32

for i in range(0,10):
    Label(f1, text=("Competitor",i+1)).grid(row=i, column=0)  # example competitor labels, will eventually be objects

for i in range(0,25):
    Label(f2, text=("Route",i+1,' \t\t')).grid(row=i, column=0)  # example route labels, will eventually be objects
    Label(f2, text=("Route",i+1,' \t\t')).grid(row=i, column=1)

window.mainloop()  # runs main loop of the tkinter object

# Rhys was here :3
