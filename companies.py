class Companies(object):
    def __init__(self):
        self.companies = []
    def add(self, company):
        if self.exists(company.id):
            return False
        self.companies.append(company)
        return True
    def __str__(self):
        if not self.companies:
            return "Empty"
        return '\n'.join(str(company) for company in self.companies)
    def exists(self, id):
        for company in self.companies:
            if company.id == id:
                return True
        return False
    def delete(self, id, models):
        if models.cexists(id):
            return False
        for company in self.companies:
            if company.id == id:
                self.companies.pop(self.companies.index(company))
                return True
        return False
    def showById(self, id):
        flag = False
        for company in self.companies:
            if company.id == id:
                print company
                flag = True
        if not flag:
            print "There is not companies with id:%d"%(id)
    def get(self, id):
        for company in self.companies:
            if company.id == id:
                return company
        return False
    def update(self, id, name, attr, models):
        if not self.exists(id):
            return False
        if models.cexists(id):
            return False
        company = self.get(id)
        if name == "id":
            company.id = int(attr)
            return True
        if name == "name":
            company.name = attr
            return True
        if name == "country":
            company.country = attr
            return True
        return False



