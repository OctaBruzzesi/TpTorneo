from tkinter import *
from tkinter import ttk
from UserLayer.formTournament import FormTournament


class Menu:
    def __init__(self):

        self.window = Tk()

        label = ttk.Label(self.window, text="Start Page")
        label.pack(pady=10, padx=125)

        button = ttk.Button(self.window, text="Lista de Torneos", command=self.open_tournament)
        button.pack()

        button2 = ttk.Button(self.window, text="Lista de Equipos")
        button2.pack()

        button3 = ttk.Button(self.window, text="Informes")
        button3.pack()

        self.window.mainloop()

    def open_tournament(self):
        FormTournament()

Menu()