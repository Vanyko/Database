class Company(object):
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country
    def __str__(self):
        return "Company #%d: %s, country: %s"%(self.id, self.name, self.country)
