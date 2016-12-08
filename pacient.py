class Pacient:

    def __init__(self, name, diagnose):
        self.name = name
        self.diagnose = diagnose
        self.ekg = []

    def __init__(self, name, diagnose, ekg):
        self.name = name
        self.diagnose = diagnose
        self.ekg = ekg