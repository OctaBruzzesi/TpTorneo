from DataLayer.DataLayerTeam import DataLayerTeam


class BusinessLayerTeam:
    def __init__(self):
        self.dlt = DataLayerTeam()

    def create(self, team):
        try:
            if team.team_name is None:
                raise Exception("El equipo debe tener nombre")
            if self.dlt.search(team.team_name) == True:
                raise Exception("Ya existe un torneo con ese nombre")
            if len(team.team_name) < 3:
                raise Exception("El nombre debe tener mas de 3 caracteres")
            else:
                return self.dlt.create_team(team)
        except Exception as e:
            return e

    def get_all(self):
        return (self.dlt.list_teams())

    def get_team(self, id):
        return self.dlt.get_team(id)

    def delete_team(self, id):
        self.dlt.delete_team(id)
