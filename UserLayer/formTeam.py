from tkinter import *
from tkinter import ttk
from BusinessLayer.BusinessLayerTeam import BusinessLayerTeam
from Entities.Team import Team


blt = BusinessLayerTeam()

class FormTeam:
    def __init__(self, tournament):

        self.selectedTeams = []
        self.teams = blt.get_all()

        self.window = Tk()

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

        self.button_save = Button(self.frame, text='Alta', command=self.create_team)
        self.button_save.pack(side='left')

        self.button_delete = Button(self.frame, text='Baja')
        self.button_delete.pack(side='left')

        self.button_update = Button(self.frame, text='Modificación')
        self.button_update.pack(side='left')

        self.selectFrame = Frame(self.window, width=150, height=300)
        self.selectFrame.grid(row=1, column=2)

        self.button_select = Button(self.selectFrame, text='Seleccionar', command=self.select_team)
        self.button_select.pack(side='left')

        self.button_remove = Button(self.selectFrame, text='Eliminar', command=self.remove_team)
        self.button_remove.pack(side='left')

        self.tree.grid(row=1, column=1)
        self.treeSelected.grid(row=1, column=3)
        self.updateView()
        self.tournament = tournament

        print(tournament)

    def create_team(self):
        def abort():
            form.destroy()

        def save():
            noti = Toplevel()
            team = Team(None, name.get())
            try:
                blt.create(team)
                self.updateView()
                noti.destroy()

            except Exception as e:
                print(e)
                Label(master=noti, text=e).grid(row=0, column=0)
            form.destroy()

        form = Toplevel()

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
        number_teams = IntVar()

        e_name = Entry(form, textvariable=name)
        e_name.grid(row=0, column=1)

    def select_team(self):
        #self.teams.remove()
        selectedTeam = self.tree.selection()
        print(selectedTeam)
        id = self.tree.item(selectedTeam)
        print(id)
        self.selectedTeams.append(id['text'])
        print(self.selectedTeams)
        #self.updateView()

    def remove_team(self):
        selectedTeam = self.treeSelected.selection()
        id = self.treeSelected.item(selectedTeam)
        self.selectedTeams.remove(id['text'])
        print(self.selectedTeams)
        self.updateView()


    def updateView(self):
        self.tree.delete(*self.tree.get_children())
        #self.tree.delete(*self.tree.get_children())
        for i in blt.get_all():
            self.tree.insert("", 'end', text=i[0], values=(i[1]))
        #for i in self.selectedTeams:
            #self.treeSelected.insert("", "end", text=i[0], values=(i[1]))
