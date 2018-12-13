from DataLayer.DataLayerTeam import DataLayerTeam

dlt = DataLayerTeam()

class BusinessLayerTeam:

    def create(self, team):
            if team.team_name is None:
                raise Exception("El equipo debe tener nombre")
            if dlt.search_by_name(team.team_name):
                raise Exception("Ya existe un equipo con ese nombre")
            if len(team.team_name) < 3:
                raise Exception("El nombre debe tener mas de 3 caracteres")
            return dlt.create_team(team)

    def get_all(self):
        return dlt.list_teams()

    def update(self, team):
        if team.team_name is None:
            raise Exception("El torneo debe tener nombre")
        if dlt.search_by_name(team.team_name):
            raise Exception("Ya existe un equipo con ese nombre")
        if len(team.team_name) < 3:
            raise Exception("El nombre debe tener mas de 3 caracteres")
        return dlt.update_team(team)

    def get_team(self, id):
        return dlt.get_team(id)

    def delete_team(self, id):
        dlt.delete_team(id)


