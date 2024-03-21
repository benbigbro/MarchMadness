import Team
class Game:
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.loser = None
        if(team1 != None and team2!=None):
            if team1.wins > team2.wins:
                self.winner = team1
                self.loser = team2
            if team2.wins > team1.wins:
                self.winner = team2
                self.loser = team1
            if team1.wins == team2.wins:
                self.winner = None
                self.loser = None
        