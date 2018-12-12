from tkinter import *
from tkinter import ttk
from BusinessLayer.BusinessLayerTournament import BusinessLayerTournament
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam
from BusinessLayer.BusinessLayerMatch import BusinessLayerMatch
from Entities.Tournament import Tournament
from Entities.Team import Team


blt = BusinessLayerTeam()
blTournament = BusinessLayerTournament()
blm = BusinessLayerMatch()


class FormMatch:
    def __init__(self, tournament, range_matches):

        self.selectedTeams = []
        self.teams = blt.get_all()

        self.window = Tk()

        self.tree = ttk.Treeview(self.window)

        self.tree["columns"] = ("team_1", "team_2", "result")
        self.tree.heading('#0', text="Id")
        self.tree.column("team_1", width=150)
        self.tree.heading("team_1", text="Equipo 1")
        self.tree.column("team_2", width=150)
        self.tree.heading("team_2", text="Equipo 2")
        self.tree.column("result", width=150)
        self.tree.heading("result", text="Resultado")

        self.tree.grid(row=0, column=0)

        self.frame = Frame(self.window, width=150, height=100)
        self.frame.grid(row=1, column=0)

        self.button_save = Button(self.frame, text='Resultado')
        self.button_save.pack(side="left")

        self.tournament = tournament

        self.matches = blm.get_matches(self.tournament, range_matches)

        self.updateView()

        self.window.mainloop()

    def updateView(self):
        self.tree.delete(*self.tree.get_children())
        for i in self.matches:
            self.tree.insert("", 'end', text=i.id, values=(i.team_1, i.team_2, i.winner_team))
