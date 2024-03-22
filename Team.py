class Team:
    lost = False
    def __init__(self, team, seed, wins):
      self.team = team 
      self.seed = seed
      self.wins = wins
      self.lost = False