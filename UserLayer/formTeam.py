from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from BusinessLayer.BusinessLayerTournament import BusinessLayerTournament
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam
from UserLayer.Rounds import Rounds
from Entities.Team import Team

blt = BusinessLayerTeam()
blTournament = BusinessLayerTournament()
class FormTeam:
    def __init__(self, tournament):

        self.selectedTeams = []
        self.teams = blt.get_all()

        self.window = Tk()
        self.window.title('Seleccione los equipos')

        self.tree = ttk.Treeview(self.window)

        self.tree["columns"] = "name"
        self.tree.heading('#0', text="Id")
        self.tree.column("name", width=150)
        self.tree.heading("name", text="Nombre")

        self.treeSelected = ttk.Treeview(self.window)

        self.treeSelected["columns"] = "name"
        self.treeSelected.heading('#0', text="Id")
        self.treeSelected.column("name", width=150)
        self.treeSelected.heading("name", text="Nombre")

        self.frame = Frame(self.window, width=1500, height=100)
        self.frame.grid(row=2, column=1)

        self.button_save = Button(self.frame, text='Crear equipo', command=self.create_team)
        self.button_save.pack(side=LEFT, padx=6, pady=2)

        self.button_delete = Button(self.frame, text='Eliminar Equipo',fg="red", command=self.delete_team)
        self.button_delete.pack(side=LEFT, padx=6, pady=2)

        self.button_update = Button(self.frame, text='Editar Equipo', command=self.update_team)
        self.button_update.pack(side=LEFT, padx=6, pady=2)

        self.selectFrame = Frame(self.window, width=150, height=300)
        self.selectFrame.grid(row=1, column=2)

        self.button_select = Button(self.selectFrame, text='>>>>>', command=self.select_team)
        self.button_select.pack(side=LEFT, padx=6, pady=2)

        self.button_remove = Button(self.selectFrame,fg="red", text='<<<<<', command=self.remove_team)
        self.button_remove.pack(side=LEFT, padx=6, pady=2)

        self.button_start = Button(self.frame, text='Comenzar torneo', command=self.start_tournament)
        self.button_start.pack(side=LEFT, padx=6, pady=2)

        self.tree.grid(row=1, column=1)
        self.treeSelected.grid(row=1, column=3)
        self.updateView()
        self.tournament = tournament

    def delete_team(self):
        selection = self.tree.selection()
        selectedTeam = self.tree.item(selection)
        try:
            blt.delete_team(selectedTeam['text'])
            for i in self.teams:
                if(i.id == selectedTeam['text']):
                    self.teams.remove(i)
                break
            self.updateView()
        except Exception as e:
            noti = Toplevel()
            Label(master=noti, text=e).grid(row=0, column=0)

    def create_team(self):
        def abort():
            form.destroy()

        def save():
            team = Team(None, name.get())
            try:
                newTeam = blt.create(team)
                #self.teams = blt.get_all()
                self.updateView()
                form.destroy()
                self.teams.append(newTeam)
                self.updateView()

            except Exception as e:
                noti = Toplevel()
                noti.title('save de create')
                Label(master=noti, text=e).grid(row=0, column=0)

        form = Toplevel()
        form.title('form de create_team')

        label_nom = Label(form, text="Nombre del equipo")
        label_nom.grid(row=0, column=0)

        frame = Frame(form, width=50, height=10)
        frame.grid(row=4, column=1, columnspan=1)

        accept = Button(frame, text="Guardar", command=save)
        accept.pack(side="left")
        abort = Button(frame, text="Cancelar", command=abort)
        abort.pack(side="left")

        # Variables
        name = StringVar()

        e_name = Entry(form, textvariable=name)
        e_name.grid(row=0, column=1)

    def select_team(self):
        if(len(self.selectedTeams) < self.tournament.contestants):
            selection = self.tree.selection()
            selectedTeam = self.tree.item(selection)
            teamselec = Team(selectedTeam['text'], selectedTeam['values'][0])
            self.selectedTeams.append(teamselec)
            for i in self.teams:
                if(i.id == selectedTeam['text']):
                    self.teams.remove(i)
                    break
            self.updateView()
        else:
            messagebox.showinfo("Aviso", "El toreno se creó para " + str(self.tournament.contestants)+ " equipos", parent=self.window)

    def remove_team(self):
        selection = self.treeSelected.selection()
        selectedTeam = self.treeSelected.item(selection)
        teamselec = Team(selectedTeam['text'], selectedTeam['values'][0])
        self.teams.append(teamselec)
        for i in self.selectedTeams:
            if(i.id == selectedTeam['text']):
                self.selectedTeams.remove(i)
                break
        self.updateView()

    def update_team(self):
        def abort():
            form.destroy()

        def save():
            noti = Toplevel()
            noti.title('save')
            try:
                updated_team = blt.update(Team(team.id, name.get()))
                for i in enumerate(self.teams):
                    if self.teams[i[0]].id == updated_team.id:
                        self.teams[i[0]] = updated_team

                self.updateView()
                noti.destroy()
                form.destroy()
                for i in self.teams:
                    if(i.id == selectedTeam['text']):
                        self.teams.remove(i)
                    break

            except Exception as e:
                Label(master=noti, text=e).grid(row=0, column=0)

        form = Toplevel()
        form.title('top level 1')

        label_nom = Label(form, text="Nuevo nombre del torneo")
        label_nom.grid(row=0, column=0)

        frame = Frame(form, width=50, height=10)
        frame.grid(row=4, column=1, columnspan=1)

        accept = Button(frame, text="Guardar", command=save)
        accept.pack(side="left")
        abort = Button(frame, text="Cancelar", command=abort)
        abort.pack(side="left")

        # Variables

        selection = self.tree.selection()
        selectedTeam = self.tree.item(selection)
        id = selectedTeam['text']

        team = blt.get_team(id)

        name = StringVar(value=team.team_name)

        e_name = Entry(form, textvariable=name)
        e_name.grid(row=0, column=1)

    def start_tournament(self):
        if(len(self.selectedTeams) == self.tournament.contestants):
            try:
                blTournament.start(self.tournament, self.selectedTeams)
                self.window.destroy()
                Rounds(self.tournament)
            except Exception as e:
                noti = Toplevel()
                Label(master=noti, text=e).grid(row=0, column=0)
        else:
            messagebox.showinfo("Aviso", "El toreno se creó para " + str(self.tournament.contestants)+ " equipos", parent=self.window)


    def updateView(self):
        self.tree.delete(*self.tree.get_children())
        self.treeSelected.delete(*self.treeSelected.get_children())
        for i in self.teams:
            self.tree.insert("", 'end', text=i.id, values=(i.team_name))
        for i in self.selectedTeams:
            self.treeSelected.insert("", 'end', text=i.id, values=(i.team_name))
