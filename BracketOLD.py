from Team import Team
from Game import Game
class Bracket:

  games: list[list[Game]] = []
    
  gameCounts = [32,16,8,4,2,1]

  teams = {}
  score = 0
  maxScore = 0
  eliminated = False
  author = ""

  gamesRemaining = 63

  winningScenarios = 0
  lines = []

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
              self.gamesRemaining -= 1
        if(hasWinner):
          for team in teams:
            if(team.team != game.winner.team):
              if(not self.teams[team.team].lost):
                self.teams[team.team].lost = True
                self.teams[team.team].roundLost = round
        self.games[i].append(game)

  def generateLines(self):
    retval = []
    for line in self.lines:
      team: Team = self.teams[" ".join(line)]
      xStr = ""
      for win in range(team.wins):
        xStr += "X"
      if len(xStr) > 0:
        retval.append([str(team.seed)] + line + [xStr])
      else:
        retval.append([str(team.seed)] + line)

    return retval

  def fillRemainingGames(self, seed:str):
    seedList = [elem for elem in seed]
    gameCoordinates = []
    for index, winner in enumerate(seedList):
      seenGames = -1
      for roundindex, round in enumerate(self.games):
        for gameindex, game in enumerate(round):
          if game.winner == None:
            seenGames += 1
            if seenGames == index:
              gameCoordinates.append([roundindex, gameindex])

    for index, coordinate in enumerate(gameCoordinates):
      prevRound = coordinate[0] - 1
      prevGame0 = coordinate[1] *2
      prevGame1 = (coordinate[1]*2) + 1
      prevWinner0 = self.games[prevRound][prevGame0].winner
      prevWinner1 = self.games[prevRound][prevGame1].winner
        
      prevTeam0 = self.teams[prevWinner0.team]
      prevTeam1 = self.teams[prevWinner1.team]
      currentGame:Game = self.games[coordinate[0]][coordinate[1]]

      if seed[index] == '0':
        currentGame.winner = prevWinner0
        prevTeam0.wins += 1
        prevTeam1.lost = True
        prevTeam1.roundLost = prevRound + 2
      if seed[index] == '1':
        currentGame.winner = prevWinner1
        prevTeam1.wins += 1
        prevTeam0.lost = True
        prevTeam0.roundLost = prevRound + 2