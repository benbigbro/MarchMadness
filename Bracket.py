from Team import Team
from Game import Game
class Bracket:

  games = []
    
  gameCounts = [32,16,8,4,2,1]

  teams = {}
  score = 0
  maxScore = 0
  eliminated = False

  def __init__(self, author, lines):
    self.eliminated = False
    self.score = 0
    self.maxScore = 0
    self.author = author
    self.lines = lines
    self.games = []
    self.teams = {}

    for i in range(len(self.gameCounts)):
      self.games.append([])
      numberOfGames = self.gameCounts[i]
      for gameNumber in range(numberOfGames):

        line1 = lines[gameNumber*2]
        line2 = lines[gameNumber*2 + 1] 

        if(i == 0):
          #initialize the teams dictionary
          seed1 = int(line1[0])
          seed2 = int(line2[0])
          wins1 = 0
          wins2 = 0
          del line1[0]
          del line2[0]
          

          if("X" == line1[-1][-1]):
              wins1 = len(line1[-1])
              del line1[-1]
              
          if("X" == line2[-1][-1]):
              wins2 = len(line2[-1])
              del line2[-1]

          lines[gameNumber*2] = line1
          lines[gameNumber*2 + 1] = line2
          team1Name = ' '.join(map(str,line1))
          team2Name = ' '.join(map(str,line2))
          team1 = Team(team1Name, seed1, wins1)
          team2 = Team(team2Name, seed2, wins2)


          self.teams[team1Name] = team1
          self.teams[team2Name] = team2


        winners = []
        losers = []
        if(i != 0):
          #get the winners from the previous round
          for game in self.games[i-1]:
            winners.append(game.winner)
            losers.append(game.loser)

          for loser in losers:
            if(loser != None):
              loser.lost = True
              self.teams[loser.team] = loser

          team1 = winners[gameNumber*2]
          team2 = winners[gameNumber*2 + 1]
              
        game = Game(team1, team2)
        self.games[i].append(game)