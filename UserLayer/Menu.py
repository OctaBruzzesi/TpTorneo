from tkinter import *
from tkinter import ttk
from UserLayer.formTournament import FormTournament
from UserLayer.formTeam import FormTeam


class Menu:
    def __init__(self):

        self.window = Tk()

        title_frame = Frame(self.window, width=150)
        title_frame.grid(row=0, column=0, columnspan=3)
        title_frame.configure(background="#4FC1E9")

        label = ttk.Label(title_frame, text="Tournaments")
        label.pack(pady=10, padx=125)
        label.configure(background="#3BAFDA")

        button_frame = Frame(self.window, width=150)
        button_frame.grid(row=1, column=0, columnspan=3)

        button = ttk.Button(button_frame, text="Lista de Torneos", command=self.open_tournament)
        button.pack()

        button2 = ttk.Button(button_frame, text="Lista de Equipos", command=self.open_team)
        button2.pack()

        button3 = ttk.Button(button_frame, text="Informes")
        button3.pack()

        self.window.mainloop()

    def open_tournament(self):
        FormTournament()

    def open_team(self):
        FormTeam(None, False)

Menu()
