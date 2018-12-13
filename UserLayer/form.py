class Form:
    def __init__(self):
        None

    def get_select(self, tree):
        selection = tree.selection()
        sele = tree.item(selection)
        return sele['text']
