import copy
from random import Random
from Game import Game
from Team import Team

class Bracket:

    @staticmethod
    def get_game_mapping():
        gameMapping: dict[int,int] = {}
        add = 32
        count = 0
        for i in range(32):
            gameMapping[count] = i//2 + add
            count += 1

        add += 16
        for i in range(16):
            gameMapping[count] = i//2 + add
            count += 1

        add += 8
        for i in range(8):
            gameMapping[count] = i//2 + add
            count += 1

        add += 4
        for i in range(4):
            gameMapping[count] = i//2 + add
            count += 1
        
        add += 2
        for i in range(2):
            gameMapping[count] = i//2 + add
            count += 1

        add += 1
        for i in range(1):
            gameMapping[count] = i//2 + add
            count += 1
        return gameMapping

    @staticmethod
    def build_bracket(lines: list[str]):
        gameMapping = Bracket.get_game_mapping()
        games: list[Game] = []

        for i in range(64):
            games.append(Game(id=i))

        for i,line in enumerate(lines):
            parts = line.split(" ")
            gamesPlayed = [i//2]

            team_name_parts = []
            for i,part in enumerate(parts):
                if(i == 0):
                    continue
                if(part == "X" or part == "XX" or part == "XXX" or part == "XXXX" or part == "XXXXX" or part == "XXXXXX"):
                    continue
                team_name_parts.append(part)
            
            team_name = " ".join(team_name_parts)

            team_seed = int(parts[0])


            gamesWon = 0

            if(parts[-1] == "X" or parts[-1] == "XX" or parts[-1] == "XXX" or parts[-1] == "XXXX" or parts[-1] == "XXXXX" or parts[-1] == "XXXXXX"):
                gamesWon = len(parts[-1])

            team = Team(team_name, team_seed, gamesWon)
            games[gamesPlayed[-1]].teams.append(team)

            for j in range(gamesWon):
                games[gamesPlayed[-1]].winner = team
                gamesPlayed.append(gameMapping[gamesPlayed[-1]])
                games[gamesPlayed[-1]].teams.append(team)
        
        return games

    @staticmethod
    def valid_bracket(lines:list[str], complete:bool):
        gameMapping = Bracket.get_game_mapping()
        games: list[Game] = []

        games = Bracket.build_bracket(lines)

        for game in games:
            if(len(game.teams) > 2):
                return False

        if(complete):
            for i,game in enumerate(games):
                if(len(game.teams) != 2 and i != 63):
                    return False
        
        return True

    def __init__(self, lines:list[str]):
        lines = [line.replace("\n","") for line in lines]
        self.lines = lines
        self.game_mapping = Bracket.get_game_mapping()
        if(not Bracket.valid_bracket(lines, False)):
            exit -1

        self.games = Bracket.build_bracket(lines)

        self.games_remaining = 63
        for game in self.games:
            if game.winner != None:
                self.games_remaining -= 1

class HypotheticalBracket(Bracket):
    def __init__(self, seed:str, current_result:Bracket):
        random = Random()
        incomplete_games = []
        for i,game in enumerate(current_result.games):
            if(i == 63):
                continue
            if game.winner == None:
                incomplete_games.append(i)
        
        self.games = copy.deepcopy(current_result.games)
        self.game_mapping = Bracket.get_game_mapping()

        seeds_consumed = 0
        for i,index in enumerate(incomplete_games):
            winning_index = random.randint(0,1)

            if(index > 47):
                winning_index = int(seed[seeds_consumed])
                seeds_consumed += 1

            self.games[index].winner = self.games[index].teams[winning_index]
            self.games[self.game_mapping[index]].teams.append(self.games[index].winner)

        self.games_remaining = 63
        for game in self.games:
            if game.winner != None:
                self.games_remaining -= 1

class UserBracket(Bracket):
    def __init__(self, lines:list[str], result:Bracket, author: str, round_points: list[int], seed_points:bool):
        self.author = author
        self.round_points = round_points
        self.seed_points = seed_points

        lines = [line.replace("\n","") for line in lines]
        self.lines = lines
        self.game_mapping = Bracket.get_game_mapping()
        if(not Bracket.valid_bracket(lines, True)):
            exit -1

        self.games = Bracket.build_bracket(lines)

        self.perfect_remaining_bracket = self.build_perfect_remaining_bracket(lines,result)

        self.score = self.get_score(result)
        self.max_score = self.get_max_score(self.perfect_remaining_bracket)


    def build_perfect_round(self, result:Bracket, number_of_games: int, add:int, eliminated_teams:set, perfect_remaining:Bracket):
        for i in range(number_of_games):
            prediction_game = self.games[i+add]
            actual_game = result.games[i+add]
            if(actual_game.winner != None and len(actual_game.teams) == 2):
                #game has a winner and a loser
                loser_index = -1
                if(actual_game.teams[0].team == actual_game.winner.team):
                    loser_index = 1
                if(actual_game.teams[1].team == actual_game.winner.team):
                    loser_index = 0
                loser = actual_game.teams[loser_index]
                eliminated_teams.add(loser.team)

            if(actual_game.winner == None and prediction_game.winner.team not in eliminated_teams):
                #actual game does not have a winner, and our predicted winner has not been eliminated
                perfect_remaining.games[i+add].winner = prediction_game.winner

    def build_perfect_remaining_bracket(self,lines:list[str], result:Bracket):
        perfect_remaining = copy.deepcopy(result)
        eliminated_teams = set()

        add = 0
        self.build_perfect_round(result, 32, add, eliminated_teams, perfect_remaining)

        add += 32
        self.build_perfect_round(result, 16, add, eliminated_teams, perfect_remaining)
        
        add += 16
        self.build_perfect_round(result, 8, add, eliminated_teams, perfect_remaining)

        add += 8
        self.build_perfect_round(result, 4, add, eliminated_teams, perfect_remaining)

        add += 4
        self.build_perfect_round(result, 2, add, eliminated_teams, perfect_remaining)

        add += 2
        self.build_perfect_round(result, 1, add, eliminated_teams, perfect_remaining)
        return perfect_remaining

    
    def points_for_game(self, actual:Game, prediction:Game, round:int):
        score = 0
        if(actual.winner == None):
            return 0

        if(prediction.winner == None):
            return 0

        if(actual.winner.team == prediction.winner.team):
            score += self.round_points[round]
            if(self.seed_points):
                score += actual.winner.seed
        return score


    def get_score(self, result:Bracket):
        add = 0
        score = 0
        for i in range(32):
            result_game = result.games[i]
            prediction_game = self.games[i]

            score += self.points_for_game(result_game, prediction_game, 0)
        
        add += 32
        for i in range(16):
            result_game = result.games[i+add]
            prediction_game = self.games[i+add]
            score += self.points_for_game(result_game, prediction_game, 1)

        add += 16
        for i in range(8):
            result_game = result.games[i+add]
            prediction_game = self.games[i+add]
            score += self.points_for_game(result_game, prediction_game, 2)

        add += 8
        for i in range(4):
            result_game = result.games[i+add]
            prediction_game = self.games[i+add]
            score += self.points_for_game(result_game, prediction_game, 3)

        add += 4
        for i in range(2):
            result_game = result.games[i+add]
            prediction_game = self.games[i+add]
            score += self.points_for_game(result_game, prediction_game, 4)

        add += 2
        for i in range(1):
            result_game = result.games[i+add]
            prediction_game = self.games[i+add]
            score += self.points_for_game(result_game, prediction_game, 5)


        return score
    
    def get_max_score(self, perfect_remaining_bracket:Bracket):
        return self.get_score(perfect_remaining_bracket)

        

# with open("2025/results.txt", "r") as file:
#     lines = file.readlines()

# resultBracket = Bracket(lines)

# with open("2025/groups/family/Anna_Singewald.txt", "r") as file:
#     lines = file.readlines()

# bracket = UserBracket(lines, resultBracket, "Ben Moorlach", [1,5,10,15,20,25], True)
# print("done")