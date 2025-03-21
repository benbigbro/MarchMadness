from Team import Team
class Game:
    id = 0
    winner = None
    
    def __init__(self, winner:Team):
        self.id = 0
        self.winner:Team = winner
        self.teams:list[Team] = []

    def __init__(self, id:int):
        self.id = id
        self.teams = []