from Team import Team
from Game import Game
class Bracket:

  games = []
    
  gameCounts = [32,16,8,4,2,1]

  teams = {}
  score = 0
  maxScore = 0
  eliminated = False
  author = ""

  def __init__(self, author, lines):
    self.eliminated = False
    self.score = 0
    self.maxScore = 0
    self.author = author
    self.lines = lines
    self.games = []
    self.teams = {}


    for index, line in enumerate(self.lines):
      seed = int(line[0])
      wins = 0
      if(line[-1][-1] == 'X'):
        wins = len(line[-1])
        del line[-1]
      del line[0]
      teamName = ' '.join(line)     

      ids = [index//2, index//4, index//8, index//16, index//32, index//64]
      team = Team(teamName, seed, wins)
      team.gameIds = ids
      self.teams[teamName] = team

    for i in range(len(self.gameCounts)):
      self.games.append([])
      numberOfGames = self.gameCounts[i]

      round = i + 1
      for gameNumber in range(numberOfGames):
        #get the possible teams for this game
        teams = []
        game = Game(None)
        hasWinner = False
        for line in self.lines:
          teamName = " ".join(line)
          team = self.teams[teamName]
          if team.gameIds[i] == gameNumber:
            teams.append(team)
            if team.wins >= round:
              game.winner = team
              hasWinner = True
        if(hasWinner):
          for team in teams:
            if(team.team != game.winner.team):
              if(not self.teams[team.team].lost):
                self.teams[team.team].lost = True
                self.teams[team.team].roundLost = round
        self.games[i].append(game)