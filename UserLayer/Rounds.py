from tkinter import *
from tkinter import ttk
from UserLayer.formMatch import FormMatch
from BusinessLayer.BusinessLayerTournament import BusinessLayerTournament
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam

blt = BusinessLayerTeam()
blTournament = BusinessLayerTournament()

class Rounds:
    def __init__(self, tournament):

        self.window = Tk()

        self.button_save = Button(self.window, text='Segunda Ronda', command=lambda: self.show_matches((16, 31)))
        self.button_save.grid(row=0, column=0)

        self.button_save = Button(self.window, text='Primera Ronda', command=lambda: self.show_matches((8, 15)))
        self.button_save.grid(row=1, column=0)

        self.button_save = Button(self.window, text='Cuartos de Final', command=lambda: self.show_matches((4, 7)))
        self.button_save.grid(row=0, column=1)

        self.button_save = Button(self.window, text='Semi Final', command=lambda: self.show_matches((2, 3)))
        self.button_save.grid(row=1, column=1)

        self.button_save = Button(self.window, text='Final', command=lambda: self.show_matches((1, 1)))
        self.button_save.grid(row=2, column=0)

        self.tournament = tournament

        self.window.mainloop()

    def show_matches(self, range_matches):
        FormMatch(self.tournament, range_matches)
