class Team:
    lost = False
    gameIds = []
    def __init__(self, team, seed, wins):
      self.team = team 
      self.seed = seed
      self.wins = wins
      self.gameIds = []
      self.lost = False
      self.roundLost = 0