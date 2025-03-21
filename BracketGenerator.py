import sys
import os
from Bracket import Bracket
print()

if len(sys.argv) < 3:
    print("Please enter the year as second command line argument")
    print("Please enter the type of bracket creation: \"perfect\" or \"all\" as the third command line argument")
    exit(-1)

if(sys.argv[2] == "all" and len(sys.argv) < 4):
    print("Please enter the group as fourth command line argument")
    exit(-1)


year = sys.argv[1]

perfect = False
if sys.argv[2] == "perfect":
    print("Perfect")
    perfect = True
if sys.argv[2] == "all":
    print("all")
    perfect = False

print(f"The year will be {year}")
teams = []
t_file_path = year + "/teams.txt"

with open(t_file_path) as f:
    teams = f.readlines()

teams = [name.replace("\n","") for name in teams]

participants = []



na = "NA"

group = sys.argv[3]
baseDir = f"{year}/groups/{group}"
p_file_path = f"{baseDir}/participants.txt"

with open(p_file_path) as f:
    participants = f.readlines()

participants = [name.replace("\n","") for name in participants]
for participant in participants:
    while(True):

        teams32 = []
        teams16 = []
        teams8 = []
        teams4 = []
        teams2 = []
        winner = []

        filename = f"{baseDir}/{participant}.txt"
        print(filename)
        test = input("continue?\n")
        if test == "n":
            continue

        
        with open(filename, "w") as file:

            numberOfWins = 0
            winningTeam = -1
            for i in range(len(teams)//2):

                team1 = teams[2*i]
                team2 = teams[2*i + 1]

                team1Seed = int(team1.split(" ")[0])
                team2Seed = int(team2.split(" ")[0])

                winningTeam = -1
                while(winningTeam != team1Seed and winningTeam != team2Seed):
                    winningTeam = int(input(f"\n{team1} or {team2}?\n"))

                winningTeam = 0 if winningTeam == team1Seed else 1

                numberOfWins = 0
                while(numberOfWins < 1 or numberOfWins > 6):
                    print(f"How many games does {teams[2*i+winningTeam]} win (1-6)?\n")
                    numberOfWins = input()
                    try:
                        numberOfWins = int(numberOfWins)
                    except:
                        numberOfWins = 0

                if(numberOfWins > 0):
                    teams32.append(teams[2*i+winningTeam])
                if(numberOfWins > 1):
                    teams16.append(teams[2*i+winningTeam])
                if(numberOfWins > 2):
                    teams8.append(teams[2*i+winningTeam])
                if(numberOfWins > 3):
                    teams4.append(teams[2*i+winningTeam])
                if(numberOfWins > 4):
                    teams2.append(teams[2*i+winningTeam])
                if(numberOfWins > 5):
                    winner.append(teams[2*i+winningTeam])

                firstTeamLine = teams[2*i]
                secondTeamLine = teams[2*i + 1]

                if(winningTeam == 0):
                    firstTeamLine += f" {'X'*numberOfWins}"
                
                if(winningTeam == 1):
                    secondTeamLine += f" {'X'*numberOfWins}"

                firstTeamLine += "\n"
                secondTeamLine += "\n"
                file.write(firstTeamLine)
                file.write(secondTeamLine)


        error = False
        with open(filename, "r") as file:
            lines = file.readlines()
            lines = [line.replace("\n","") for line in lines]
            if(not Bracket.valid_bracket(lines, True)):
                error = True

        if(error == False):
            break

                