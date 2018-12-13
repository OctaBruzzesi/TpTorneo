class Form:
    def __init__(self):
        pass

    def get_select(self, tree):
        selection = tree.selection()
        sele = tree.item(selection)
        return sele['text']
