from tkinter import PhotoImage
from tkinter import IntVar


class Route:
    def __init__(self, num, points, attempts):
        self.num = num
        self.points = points
        self.attempts = IntVar()
        self.attempts.set(attempts)
        self.plus_icon = PhotoImage(file="plus-icon.png")
        self.minus_icon = PhotoImage(file="minus-icon.png")
        self.check_icon = PhotoImage(file="check-icon.png")

    def increment_attempts(self):
        self.attempts.set(self.attempts.get()+1)

    def decrement_attempts(self):
        self.attempts.set(self.attempts.get()-1)
        if self.attempts.get() < 0:
            self.attempts.set(0)
