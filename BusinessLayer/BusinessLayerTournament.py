from DataLayer.DataLayerTournament import DataLayerTournament
from DataLayer.DataLayerTournamentTeam import DataLayerTournamentTeam
from BusinessLayer.BusinessLayerMatch import BusinessLayerMatch

dlt = DataLayerTournament()
dlTournamentTeam = DataLayerTournamentTeam()
blm = BusinessLayerMatch()


class BusinessLayerTournament:
    def __init__(self):
        pass

    def create(self, tournament):
        if tournament.tournament_name is None:
            raise Exception("El torneo debe tener nombre")
        if len(tournament.tournament_name) < 3:
            raise Exception("El nombre debe tener mas de 3 caracteres")
        if tournament.contestants != 4 and tournament.contestants != 8 and tournament.contestants != 16 and tournament.contestants != 32:
            raise Exception("El torneo puede tener 4, 8, 16 o 32 participantes")
        return dlt.create_tournament(tournament)

    def get_all(self):
        return (dlt.list_tournaments())

    def start(self, tournament, teams):
        for i in teams:
            dlTournamentTeam.create_tournament_team(tournament.id, i.id)
        return blm.create_matches(tournament, teams)

    def get_tournament(self, id):
        return (dlt.get_tournament(id))

    def update(self, tournament):
        if tournament.tournament_name is None:
            raise Exception("El torneo debe tener nombre")
        if len(tournament.tournament_name) < 3:
            raise Exception("El nombre debe tener mas de 3 caracteres")
        return dlt.update_tournament(tournament)

    def delete(self,id):
        dlt.delete(id)
