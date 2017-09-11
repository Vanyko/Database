class Model(object):
    def __init__(self, company, mid, name, consumption, speed, evolume):
        self.company = company
        self.mid = mid
        self.name = name
        self.consumption = consumption
        self.speed = speed
        self.evolume = evolume
    def __str__(self):
        return str(self.company)+", id: %d, name: %s, consumption: %.1f (l/100km), speed: %d (kmph), engine volume: %.1f (l)"%(self.mid, self.name, self.consumption, self.speed, self.evolume)
