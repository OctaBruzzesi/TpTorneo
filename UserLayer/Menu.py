from tkinter import *
from tkinter import ttk
from UserLayer.formTournament import FormTournament
from UserLayer.formTeam import FormTeam


class Menu:
    def __init__(self):

        self.window = Tk()

        label = ttk.Label(self.window, text="Start Page")
        label.pack(pady=10, padx=125)

        button = ttk.Button(self.window, text="Lista de Torneos", command=self.open_tournament)
        button.pack()

        button2 = ttk.Button(self.window, text="Lista de Equipos", command=self.open_team)
        button2.pack()

        button3 = ttk.Button(self.window, text="Informes")
        button3.pack()

        self.window.mainloop()

    def open_tournament(self):
        FormTournament()

    def open_team(self):
        FormTeam(None, False)

Menu()
