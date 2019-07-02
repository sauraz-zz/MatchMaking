
import names
import random
import string

'''
# Player Class -
    name   - Name of the Player ( Should be unique )
    score  - score of the Player ( Can be zero )
'''
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return "Name - {}  Score - {}".format(self.name, self.score)

'''
# Team Class -
    team  - Set of Players
    score - cummulative score of Players in team
'''
class Team:
    def __init__(self, team, score):
        self.team = team
        self.score = score
    
    def __str__(self):
        return "Team - {}  Score - {}".format(list(self.team), self.score)

'''
# MatchMaking Class -
    teamA - Team 1
    teamB - Team 2
    diff  - difference bewteen the scores of Team 1 and Team 2
'''
class MatchMaking:
    def __init__(self, teamA, teamB, diff):
        self.teamA = teamA
        self.teamB = teamB
        self.diff = diff
    
    def __repr__(self):
        return {'Team1':self.teamA, 'Team2':self.teamB, 'diff':self.diff}
    
    def __str__(self):
        return 'Team1:{0} Team2:{1} diff:{2}'.format(list(self.teamA), list(self.teamB), self.diff)

'''
get_user_inputs : Gets the input for
    N - no of players
    M - no of players in a team i.e M vs M 
'''
def get_user_inputs():
    N, M = map(int, raw_input().split())

    if M > int(N/2):
        raise("Not enough players for match making.")
    
    players_list = []
    
    for _ in range(N):
        name , score = raw_input().split()
        players_list.append(Player(name, int(score)))
    
    return players_list, M


'''
get_random_inputs : Returns random inputs for
    N - no of players
    M - no of players in a team i.e M vs M 
'''
def get_random_inputs(N, M):
    
    if M > int(N/2):
        raise("Not enough players for match making.")

    players_list = []
    
    for _ in range(N):
        rand_name = names.get_first_name()
        rand_score = random.randrange(10)
        players_list.append(Player(rand_name, rand_score))
    
    return players_list, M

'''
get_teams_combinations : Uses backtracking to get all combinations of possible teams
    team - arr of players
    score - cummulative scores of players in team
    @returns [] Team
'''
def get_teams_combinations(players_list, M):

    teams = []
    reference_arr = [False]*len(players_list)
    
    # Returns the combinations of teams with their scores
    def combinations(actual_arr, max_size, start, curr_len, used_arr):
        
        if curr_len == max_size:
            sum = 0 
            obj = Team(set(), 0)
            for i in range(len(actual_arr)):
                if used_arr[i] == True:
                    obj.team.add(actual_arr[i].name)
                    sum += actual_arr[i].score
            obj.score = sum
            teams.append(obj)
            return
        
        if start == len(actual_arr):
            return

        used_arr[start] = True
        combinations(actual_arr, max_size, start + 1, curr_len + 1, used_arr)
        used_arr[start] = False
        combinations(actual_arr, max_size, start + 1, curr_len, used_arr)
    
    # recursive call to get all combinations
    combinations(players_list, M, 0, 0, reference_arr)

    return teams

'''
get_team_diff_list - Returns the match_making_list in ascending order of diff
    @returns [] MatchMaking
'''           
def get_team_diff_list(teams):
    
    match_making_list = []
    for i, t1 in enumerate(teams):
        for j, t2 in enumerate(teams):
            # skip for players present in both the teams
            if i <= j:
                continue
            # skip player present in both the teams
            if len((t1.team).intersection((t2.team))) > 0:
                continue
            
            match = MatchMaking(t1.team, t2.team, abs(t1.score - t2.score))
            match_making_list.append(match)

    # sort the match_making_list to ascending order of diff
    match_making_list.sort(key=lambda match: match.diff, reverse=False)

    return match_making_list