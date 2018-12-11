from DataLayer.DataLayerMatch import DataLayerMatch

dlm = DataLayerMatch()


class BusinessLayerMatch:
    def __init__(self):
        pass

    def create_matches(self, contestants, teams):
        for i in range(0, contestants - 1, 2):
            dlm.create(teams[i], teams[i+1])
