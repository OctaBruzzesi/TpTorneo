from DataLayer.DataLayerMatch import DataLayerMatch

dlm = DataLayerMatch()


class BusinessLayerMatch:
    def __init__(self):
        pass

    def create_matches(self, tournament, teams):
        phase = tournament.contestants - 1
        for i in range(0, tournament.contestants - 1, 2):
            dlm.create_match(teams[i].id, teams[i+1].id, tournament.id, phase)
            phase = phase - 1
        for i in range(1, phase + 1, 1):
            dlm.create_next_match(tournament.id, i)

    def result(self, match, score_team_1, score_team_2):
        if match.id_phase != 1:
            id_next_phase = int(match.id_phase / 2)
            if dlm.is_match_done(match.id_tournament, id_next_phase):
                raise Exception("No se puede modificar el puntaje")
        if score_team_1 < 0 | score_team_2 < 0:
            raise Exception("El puntaje debe ser mayor a 0")
        if score_team_1 == score_team_2:
            raise Exception("No puede haber empate")
        matchResult = dlm.result(match, score_team_1, score_team_2)
        if matchResult.score_team_1 > matchResult.score_team_2:
            dlm.winner(matchResult, matchResult.team_1)
        else:
            dlm.winner(matchResult, matchResult.team_2)
        return matchResult

    def get_match(self, id):
        return dlm.get_match(id)

    def get_matches(self, tournament, range_matches):
        return (dlm.get_matches(tournament, range_matches))
