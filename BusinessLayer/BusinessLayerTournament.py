from DataLayer.DataLayerTournament import DataLayerTournament

dlt = DataLayerTournament()


class BusinessLayerTournament:
    def __init__(self):
        pass

    def create(self, tournament):
        try:
            if tournament.tournament_name is None:
                raise Exception("El torneo debe tener nombre")
            #if dlt.search(tournament.tournament_name) == True:
                #raise Exception("Ya existe un torneo con ese nombre")
            if len(tournament.tournament_name) < 3:
                raise Exception("El nombre debe tener mas de 3 caracteres")
            if tournament.contestants != 4 and tournament.contestants != 8 and tournament.contestants != 16 and tournament.contestants != 32:
                raise Exception("El torneo puede tener 4, 8, 16 o 32 participantes")
        except Exception as e:
            return e
        else:
            return dlt.create_tournament(tournament)

    def delete(self, tournament):
        return dlt.delete(tournament.id)

    def update(self, tournament):
        try:
            if tournament.tournament_name is None:
                raise Exception("El torneo debe tener nombre")
            if dlt.search(tournament.tournament_name) == True:
                raise Exception("Ya existe un torneo con ese nombre")
            if len(tournament.tournament_name) < 3:
                raise Exception("El nombre debe tener mas de 3 caracteres")
            if tournament.contestants != 4 and tournament.contestants != 8 and tournament.contestants != 16 and tournament.contestants != 32:
                raise Exception("El torneo puede tener 4, 8, 16 o 32 participantes")
        except Exception as e:
            return e
        else:
            return dlt.update_tournament(tournament)

    def search_id(self, id):
        return (dlt.searchId(id))

    def get_all(self):
        return (dlt.getAllTournaments())