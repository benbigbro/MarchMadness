import copy
import sys
import os

from Bracket import Bracket

def sort_key(obj):
    return (obj.score, obj.maxScore)

def generateBracket(name) -> Bracket:
    if name == 'result':
        bracket = Bracket(name)
        return bracket
    
def generateLines(filePath):
    contents = open(filePath, "r").read()
    lines = contents.split("\n")
    author = lines[0]
    for i in range(len(lines)):
      lines[i] = lines[i].split(" ")
    return lines

def lostTeams(resultBracket):
    #returns the teams which have been elimated
    retVal = []
    for team in resultBracket.teams:
        if resultBracket.teams[team].lost:
            retVal.append(team)
    return retVal

def generateBestCaseScenarioLines(resultBracket, participantBracket):
    #each line is a team in the tournament
    #space delimited
    #first is seed
    #then team name
    #then 'X's indicating the number of wins
    # lines = resultBracket.lines

    #start from the result bracket
    lines = []
    for line in resultBracket.lines:
        resultX = ""
        resultTeam = resultBracket.teams[" ".join(line)]
        participantTeam = participantBracket.teams[" ".join(line)]
        for i in range(resultBracket.teams[" ".join(line)].wins):
            resultX += "X"

        lines.append([resultBracket.teams[" ".join(line)].seed] + line + [resultX])
    
    for round in range(len(roundGames)):
        winsNeeded = round + 1
        for index, participantTeam in enumerate(participantBracket.lines):
            participantTeam = " ".join(participantTeam)
            gameNumber = resultBracket.teams[participantTeam].gameIds[round]
            hasWinner = False
            for lineNumber in range(len(resultBracket.lines)):
                team = resultBracket.teams[' '.join(resultBracket.lines[lineNumber])]
                if team.gameIds[round] == gameNumber:
                    if team.wins >= winsNeeded:
                        hasWinner = True
            if (not hasWinner) and (participantBracket.teams[participantTeam].wins >= winsNeeded) and (participantBracket.teams[participantTeam].gameIds[round] == gameNumber) and (participantBracket.teams[participantTeam].roundLost > round or participantBracket.teams[participantTeam].roundLost == 0) and (resultBracket.teams[participantTeam].roundLost > round or resultBracket.teams[participantTeam].roundLost == 0):
                lines[index][-1] += 'X'

    for index in range(len(lines)):
        if lines[index][-1] == "":
            del lines[index][-1]
    return lines


        

#BONUSES
# firstround = 1
# secondround = 2
# thirdround = 3
# fourthround = 4
# fifthround = 5
# sixthround = 6


firstround = 1
secondround = 5
thirdround = 10
fourthround = 15
fifthround = 20
sixthround = 25

roundBonuses = [1,5,10,15,20,25]
roundGames = [32,16,8,4,2,1]
#CONFIG
hardloss = True #people who are in the loss column are garunteed to be out
maxScores = True #spit out the max score to make sure I inputted correct brackets
scoringSeeds = True

if len(sys.argv) != 3:
    print("Please enter the year as second command line argument")
    print("Please enter the group as third command line argument")
    exit(-1)
year = sys.argv[1]
group = sys.argv[2]
print("\n\n\n")

participantPath = f"{os.getcwd()}\\{year}\\groups\\{group}"

predictionBracketFiles = os.listdir(participantPath)

predictionBrackets = []

resultPath = f"{os.getcwd()}\\{year}\\results.txt"
lines = generateLines(resultPath)
resultBracket = Bracket("Result", lines[1:] )
alive = []
dead = []

for file in predictionBracketFiles:
    filePath = f"{os.getcwd()}\\{year}\\groups\\{group}\\{file}"
    lines = generateLines(filePath)
    bracket = Bracket(" ".join(lines[0]), lines[1:])
    bestCaseLines = generateBestCaseScenarioLines(resultBracket, bracket)
    bestCaseBracket = Bracket("Best Case", bestCaseLines)
    
    score = 0
    maxScore = 0
    #get the current score of this bracket
    for index, (resultRound, participantRound, roundBonus) in enumerate(zip(resultBracket.games, bracket.games, roundBonuses)):
        for resultGame, participantGame in zip(resultRound, participantRound):
            if(resultGame.winner != None):
                #the result has a winner, we can calculate if the participant gets points or not
                if(resultGame.winner.team == participantGame.winner.team):
                    score += resultGame.winner.seed + roundBonus

    #get the max score of this bracket
    for index, (resultRound, participantRound, roundBonus) in enumerate(zip(bestCaseBracket.games, bracket.games, roundBonuses)):
        for resultGame, participantGame in zip(resultRound, participantRound):
            if(resultGame.winner != None):
                #the result has a winner, we can calculate if the participant gets points or not
                if(resultGame.winner.team == participantGame.winner.team):
                    maxScore += resultGame.winner.seed + roundBonus

    bracket.score = score
    bracket.maxScore = maxScore

    predictionBrackets.append(bracket)

    alive.append(" ".join(lines[0]))

predictionBrackets.sort(key=sort_key, reverse=True)

for i in range(len(predictionBrackets)):
    #determine the bracket which will be the best case scenario for this participant
    participant = predictionBrackets[i].author

    #create a new bracket
    # if a game has already happened, use it in this bracket
    # if a game has not finished yet:
        # slot the team in if they are scheduled to be in this game if they keep winning
        # leave the lot None if the team has been eliminated
    lines = generateBestCaseScenarioLines(resultBracket, predictionBrackets[i])
    bestCaseScenarioBracket = Bracket("Best Case", lines)

    #determine the scores of everybody else if this was the final bracket
    topScore = 0
    topScorer = ""

    for j in range(len(predictionBrackets)):
        score = 0
        for index, (resultRound, participantRound, roundBonus) in enumerate(zip(bestCaseScenarioBracket.games, predictionBrackets[j].games, roundBonuses)):
            for resultGame, participantGame in zip(resultRound, participantRound):
                if(resultGame.winner != None):
                    #the result has a winner, we can calculate if the participant gets points or not
                    if(resultGame.winner.team == participantGame.winner.team):
                        score += resultGame.winner.seed + roundBonus
                else:
                    #the result does not have a winner
                    participantWinner = participantGame.winner
                    if(not resultBracket.teams[participantWinner.team].lost):
                        maxScore += participantGame.winner.seed + roundBonus


        if(score > predictionBrackets[i].maxScore):
            #this person has been elimiated
            predictionBrackets[i].eliminated = True
        
print(f"{year} March Madness Results")
print(f"----------------------------")
print()
print()


print("Still alive                        Score                  Max Score")
print("---------------------------------------------------------------------------")
for prediction in predictionBrackets:
    if(not prediction.eliminated):
        author = prediction.author
        if len(author) < 20:
            for i in range(20-len(author)):
                author += " "
        print(f"{author}                  {prediction.score}                   {prediction.maxScore}")


print()
print()
print("Eliminated                         Score                  Max Score")
print("----------------------------------------------------------------------------")
for prediction in predictionBrackets:
    if(prediction.eliminated):
        author = prediction.author
        if(len(author) < 20):
            for i in range(20-len(author)):
                author += " "
        print(f"{author}                  {prediction.score}                    {prediction.maxScore}")