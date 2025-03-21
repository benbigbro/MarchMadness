class Team:
    lost = False
    gameIds = []
    round_lost = -1
    def __init__(self, team, seed, wins):
      self.team = team 
      self.seed = seed
      self.wins = wins
      self.gameIds = []