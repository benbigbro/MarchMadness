import copy
import sys
import os
from tqdm import tqdm

from Bracket import Bracket, UserBracket, HypotheticalBracket

def sort_key(obj):
    return (obj.score, obj.max_score)

def generateLines(filePath):
    with open(filePath, "r") as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]
    return lines

def generateHypotheticalLines(resultBracket: Bracket, seedString):
    lines = []
    hypotheticalBracketLines = resultBracket.generateLines()
    hypotheticalBracket:Bracket = Bracket(f"seed {seedString}", hypotheticalBracketLines)

    hypotheticalBracket.fillRemainingGames(seedString)
    return hypotheticalBracket.generateLines()

def determineNumberOfWinningScenarios(resultBracket:Bracket, prediction_brackets: list[UserBracket], winning_brackets: dict[str, int]):
    # if(resultBracket.games_remaining > 20):
    #     return
    count = 2**resultBracket.games_remaining
    if(resultBracket.games_remaining > 7):
        count = 2**7
    for seed in tqdm(range(count), total=count, unit="item"):

        rounds = 1
        if(resultBracket.games_remaining > 7):
            rounds = 1
        
        for i in range(rounds):
            seedString = format(seed,'b').zfill(count)
            hypotheticalBracket = HypotheticalBracket(seedString, resultBracket)

            max_score = 0
            max_scorer = ""
            for bracket in prediction_brackets:
                #treat the hypothetical bracket as truth, and compare it to the prediction bracket
                test_bracket = UserBracket(bracket.lines, hypotheticalBracket, bracket.author, roundBonuses, scoringSeeds)
                if(test_bracket.score > max_score):
                    max_score = test_bracket.score
                    max_scorer = test_bracket.author

            winning_brackets[max_scorer] += 1


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
scoringSeeds = True

if len(sys.argv) != 3:
    print("Please enter the year as second command line argument")
    print("Please enter the group as third command line argument")
    exit(-1)
year = sys.argv[1]
group = sys.argv[2]
print("\n\n\n")

participantPath = f"{os.getcwd()}/{year}/groups/{group}"

predictionBracketFiles = os.listdir(participantPath)

predictionBracketFiles.remove("participants.txt")
predictionBrackets:list[UserBracket] = []

resultPath = f"{os.getcwd()}/{year}/results.txt"
lines = generateLines(resultPath)
resultBracket = Bracket(lines)

alive = []
dead = []

eliminated = set()
winning_brackets : dict[str, int]= {}

for file in predictionBracketFiles:
    filePath = f"{os.getcwd()}/{year}/groups/{group}/{file}"
    lines = generateLines(filePath)
    author = file.removesuffix(".txt")
    author = author.replace("_", " ")
    bracket = UserBracket(lines, resultBracket, author, roundBonuses, scoringSeeds)
    
    predictionBrackets.append(bracket)

    alive.append(author)
    winning_brackets[author] = 0

predictionBrackets.sort(key=sort_key, reverse=True)
determineNumberOfWinningScenarios(resultBracket, predictionBrackets, winning_brackets)

hypothetical_generated = 0
for temp in winning_brackets:
    hypothetical_generated += winning_brackets[temp]
winning_percent_strings = {}
    

for i in range(len(predictionBrackets)):
    #determine the bracket which will be the best case scenario for this participant
    participant_bracket = predictionBrackets[i]

    winning_percent_strings[participant_bracket.author] =format( 100 * winning_brackets[participant_bracket.author] / hypothetical_generated, ".2f")
    if(winning_brackets[participant_bracket.author] == 0):
        winning_percent_strings[participant_bracket.author] = "<0"
    


    #determine the scores of everybody else if this was the final bracket
    topScore = 0
    topScorer = ""

    for j in range(len(predictionBrackets)):
        prediction_bracket = predictionBrackets[j]

        new_bracket = UserBracket(prediction_bracket.lines, participant_bracket.perfect_remaining_bracket, prediction_bracket.author, roundBonuses, scoringSeeds)
        if(new_bracket.score > topScore):
            topScore = new_bracket.score
            topScorer = prediction_bracket.author
        
    if(topScorer != participant_bracket.author):
        eliminated.add(prediction_bracket.author)
        
print(f"{year} March Madness Results")
print(f"----------------------------")
print()
print()


print("Still alive                        Score                  Max Score                   Winning Percentage")
print("-----------------------------------------------------------------------------------------------------------")
for prediction in predictionBrackets:
    if(not prediction.author in eliminated):
        author = prediction.author
        if len(author) < 20:
            for i in range(20-len(author)):
                author += " "
        # print(f"{author}                  {prediction.score}                   {prediction.maxScore}                        {"{:.2f}".format(prediction.winningScenarios*100/(2**resultBracket.gamesRemaining))} %")
        print(f"{author}                  {prediction.score}                   {prediction.max_score}                         {winning_percent_strings[prediction.author]}")


print()
print()
print("Eliminated                         Score                  Max Score                   Winning Percentage")
print("------------------------------------------------------------------------------------------------------------")
for prediction in predictionBrackets:
    if(prediction.author in eliminated):
        author = prediction.author
        if(len(author) < 20):
            for i in range(20-len(author)):
                author += " "
        # print(f"{author}                  {prediction.score}                   {prediction.maxScore}                        {"{:.2f}".format(prediction.winningScenarios*100/(2**resultBracket.gamesRemaining))} %")
        print(f"{author}                  {prediction.score}                   {prediction.max_score}                         0 %")