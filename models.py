class Models(object):
    def __init__(self):
        self.models = []
    def __str__(self):
        if not self.models:
            return "Empty"
        return '\n'.join(str(model) for model in self.models)
    def add(self, model):
        if self.mexists(model.mid):
            return False
        self.models.append(model)
        return True
    def cexists(self, cid):
        for model in self.models:
            if model.company.id == cid:
                return True
        return False
    def mexists(self, mid):
        for model in self.models:
            if model.mid == mid:
                return True
        return False
    def delete(self, id):
        for model in self.models:
            if model.mid == id:
                self.models.pop(self.models.index(model))
                return True
        return False
    def get(self, id):
        for model in self.models:
            if model.mid == id:
                return model
        return False
    def update(self, id, name, attr, companies):
        if not self.mexists(id):
            return False
        model = self.get(id)
        if name == "company":
            if not companies.exists(attr):
                return False
            model.company = companies.get(attr)
            return True
        if name == "mid":
            model.mid = int(attr)
            return True
        if name == "name":
            model.name = attr
            return True
        if name == "consumption":
            model.consumption = float(attr)
            return True
        if name == "speed":
            model.speed = int(attr)
            return True
        if name == "evolume":
            model.evolume = float(attr)
            return True
        return False
    def searchByEvolume(self, volume):
        for model in self.models:
            if model.evolume == volume:
                print model.company
