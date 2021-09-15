# Add a class for a snack here!
class Snack:

    id = 1

    def __init__(self, name, kind):
        self.id = self.__class__.id
        self.name = name
        self.kind = kind
        Snack.id += 1