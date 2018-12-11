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
