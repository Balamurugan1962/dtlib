class DNode:
    def __init__(self,data,ind=None,entropy=None,isleaf=False,predClass=None,_parent=None):
        self.data = data
        self.ind = ind

        self.left = None
        self.right = None

        self._uid = None

        self._parent = _parent

        self.isleaf = isleaf
        self.predClass = predClass

    def __repr__(self):
        return str(self.ind)
