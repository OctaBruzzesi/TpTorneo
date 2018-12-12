from tkinter import *
from tkinter import ttk
from UserLayer.formMatch import FormMatch
from BusinessLayer.BusinessLayerTournament import BusinessLayerTournament
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam
from Entities.Tournament import Tournament
from Entities.Team import Team


blt = BusinessLayerTeam()
blTournament = BusinessLayerTournament()

class Rounds:
    def __init__(self):

        self.selectedTeams = []
        self.teams = blt.get_all()

        self.window = Tk()

        #self.treeFinal = ttk.Treeview(self.window)
        #self.treeSemiFinal = ttk.Treeview(self.window)
        #self.treeQuarterFinal = ttk.Treeview(self.window)
        #self.treeFirstRound = ttk.Treeview(self.window)
        #self.treeSecondRound = ttk.Treeview(self.window)

        # self.treeFinal["columns"] = ("team_1", "team_2", "result")
        # self.treeFinal.heading('#0', text="Id")
        # self.treeFinal.column("team_1", width=150)
        # self.treeFinal.heading("team_1", text="Equipo 1")
        # self.treeFinal.column("team_2", width=150)
        # self.treeFinal.heading("team_2", text="Equipo 2")
        # self.treeFinal.column("result", width=150)
        # self.treeFinal.heading("result", text="Resultado")

        # self.treeSemiFinal["columns"] = ("team_1", "team_2", "result")
        # self.treeSemiFinal.heading('#0', text="Id")
        # self.treeSemiFinal.column("team_1", width=150)
        # self.treeSemiFinal.heading("team_1", text="Equipo 1")
        # self.treeSemiFinal.column("team_2", width=150)
        # self.treeSemiFinal.heading("team_2", text="Equipo 2")
        # self.treeSemiFinal.column("result", width=150)
        # self.treeSemiFinal.heading("result", text="Resultado")

        # self.treeQuarterFinal["columns"] = ("team_1", "team_2", "result")
        # self.treeQuarterFinal.heading('#0', text="Id")
        # self.treeQuarterFinal.column("team_1", width=150)
        # self.treeQuarterFinal.heading("team_1", text="Equipo 1")
        # self.treeQuarterFinal.column("team_2", width=150)
        # self.treeQuarterFinal.heading("team_2", text="Equipo 2")
        # self.treeQuarterFinal.column("result", width=150)
        # self.treeQuarterFinal.heading("result", text="Resultado")

        # self.treeFirstRound["columns"] = ("team_1", "team_2", "result")
        # self.treeFirstRound.heading('#0', text="Id")
        # self.treeFirstRound.column("team_1", width=150)
        # self.treeFirstRound.heading("team_1", text="Equipo 1")
        # self.treeFirstRound.column("team_2", width=150)
        # self.treeFirstRound.heading("team_2", text="Equipo 2")
        # self.treeFirstRound.column("result", width=150)
        # self.treeFirstRound.heading("result", text="Resultado")

        # self.treeSecondRound["columns"] = ("team_1", "team_2", "result")
        # self.treeSecondRound.heading('#0', text="Id")
        # self.treeSecondRound.column("team_1", width=150)
        # self.treeSecondRound.heading("team_1", text="Equipo 1")
        # self.treeSecondRound.column("team_2", width=150)
        # self.treeSecondRound.heading("team_2", text="Equipo 2")
        # self.treeSecondRound.column("result", width=150)
        # self.treeSecondRound.heading("result", text="Resultado")

        self.button_save = Button(self.window, text='Segunda Ronda')
        self.button_save.grid(row=0, column=0)

        self.button_save = Button(self.window, text='Primera Ronda')
        self.button_save.grid(row=1, column=0)

        self.button_save = Button(self.window, text='Cuartos de Final')
        self.button_save.grid(row=0, column=1)

        self.button_save = Button(self.window, text='Semi Final')
        self.button_save.grid(row=1, column=1)

        self.button_save = Button(self.window, text='Final', command=self.final)
        self.button_save.grid(row=2, column=0)

        #self.treeFinal.grid(row=1, column=1)
        #self.treeSemiFinal.grid(row=2, column=1)
        #self.treeQuarterFinal.grid(row=3, column=1)
        #self.treeFirstRound.grid(row=4, column=1)
        #self.treeSecondRound.grid(row=5, column=1)

        #self.updateView()
        self.tournament = blTournament.get_tournament(99)

        self.window.mainloop()

    def final(self):
        FormMatch(Tournament(89, 'Torneo 75', 8), (1, 1))

    # def updateView(self):
        # self.tree.delete(*self.tree.get_children())
        # self.treeSelected.delete(*self.treeSelected.get_children())
        # for i in self.teams:
        #     self.tree.insert("", 'end', text=i.id, values=(i.team_name))
        # for i in self.selectedTeams:
        #     self.treeSelected.insert("", 'end', text=i.id, values=(i.team_name))


Rounds()
