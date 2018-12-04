from DataLayer.DataLayerTeam import DataLayerTeam


class BusinessLayerTeam:
    def __init__(self):
        self.dlt = DataLayerTeam()

    def create(self, team):
        try:
            if team.team_name is None:
                raise Exception("El equipo debe tener nombre")
            #if dlt.search(tournament.tournament_name) == True:
                #raise Exception("Ya existe un torneo con ese nombre")
            if len(team.team_name) < 3:
                raise Exception("El nombre debe tener mas de 3 caracteres")
            else:
                print('estoy')
                return self.dlt.create_team(team)
        except Exception as e:
            return e

    def todos(self):
        return (self.dlt.list_teams())
