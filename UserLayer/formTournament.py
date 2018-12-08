from tkinter import *
from tkinter import ttk
from Entities.Tournament import Tournament
from BusinessLayer.BusinessLayerTournament import BusinessLayerTournament
from UserLayer.formTeam import FormTeam

window = Tk()

tree = ttk.Treeview(window)

blt = BusinessLayerTournament()

def create_tournament():
    def abort():
        form.destroy()

    def save():
        noti = Toplevel()
        tournament = Tournament(None, name.get(), number_teams.get())
        try:
            blt.create(tournament)
            actualizarDatos()
            noti.destroy()
            FormTeam(tournament)
            form.destroy()

        except Exception as e:
            Label(master=noti, text=e).grid(row=0, column=0)

    form = Toplevel()

    label_nom = Label(form, text="Nombre del torneo")
    label_nom.grid(row=0, column=0)
    label_number_teams = Label(form, text="Cantidad de equipos")
    label_number_teams.grid(row=1, column=0)

    frame = Frame(form, width=50, height=10)
    frame.grid(row=4, column=1, columnspan=1)

    accept = Button(frame, text="Guardar", command=save)
    accept.pack(side="left")
    abort = Button(frame, text="Cancelar", command=abort)
    abort.pack(side="left")

    #Variables
    name = StringVar()
    number_teams = IntVar()

    e_name = Entry(form, textvariable=name)
    e_name.grid(row=0, column=1)
    e_number_teams = Entry(form, textvariable=number_teams)
    e_number_teams.grid(row=1, column=1)


def delete_tournament():
    noti = Toplevel()
    selection = tree.selection()
    selectedTournament = tree.item(selection)
    id = selectedTournament['text']
    try:
        blt.delete(id)
        tree.delete(*tree.get_children())
        actualizarDatos()
        Label(master=noti, text='torneo eliminado.').grid(row=0, column=0)
    except Exception as e:
        Label(master=noti, text=e).grid(row=0, column=0)

def update_tournament():
    def abort():
        form.destroy()

    def save():
        noti = Toplevel()
        try:
            blt.update(Tournament(tournament.id, name.get(), tournament.contestants))
            actualizarDatos()
            noti.destroy()
            form.destroy()

        except Exception as e:
            Label(master=noti, text=e).grid(row=0, column=0)

    form = Toplevel()

    label_nom = Label(form, text="Nuevo nombre del torneo")
    label_nom.grid(row=0, column=0)

    frame = Frame(form, width=50, height=10)
    frame.grid(row=4, column=1, columnspan=1)

    accept = Button(frame, text="Guardar", command=save)
    accept.pack(side="left")
    abort = Button(frame, text="Cancelar", command=abort)
    abort.pack(side="left")

    #Variables

    selection = tree.selection()
    selectedTournament = tree.item(selection)
    id = selectedTournament['text']

    tournament = blt.get_tournament(id)

    name = StringVar(value=tournament.tournament_name)

    e_name = Entry(form, textvariable=name)
    e_name.grid(row=0, column=1)



def actualizarDatos():
    tree.delete(*tree.get_children())
    for i in blt.get_all():
        tree.insert("", 'end', text=i[0], values=(i[1], i[2]))

actualizarDatos()

tree["columns"]=("name","team_number")
tree.heading('#0', text="Id")
tree.column("name", width=150)
tree.heading("name", text="Nombre")
tree.column("team_number", width=150)
tree.heading("team_number", text="Cantidad de equipos")


frame = Frame(window, width=500, height=100)
frame.grid(row=2, column=1, columnspan=3)

button_save = Button(frame, text='Alta', command=create_tournament)
button_save.pack(side='left')


button_delete = Button(frame, text='Baja', command=delete_tournament)
button_delete.pack(side='left')

button_update = Button(frame, text='Modificación', command=update_tournament)
button_update.pack(side='left')


tree.grid(row=1, column=1)
window.mainloop()

