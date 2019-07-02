
import random
import string

# Player Class 
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# Team Class 
class Team:
    def __init__(self, team, score):
        self.team = team
        self.score = score

'''
get_inputs : Gets the input for
    N - no of players
    M - no of players in a team i.e M vs M 
'''
def get_user_inputs():
    N, M = map(int, raw_input().split()) 
    print(N,M)

    players_list = []
    for _ in range(N):
        name , score = raw_input().split()
        players_list.append(Player(name, int(score))) 
        print(name, score)
    return players_list, M


'''
get_inputs : Returns random inputs for
    N - no of players
    M - no of players in a team i.e M vs M 
'''
def get_random_inputs(N, M):
    players_list = []
    for _ in range(N):
        rand_name = ''.join(random.choice(string.lowercase) for x in range(M))
        rand_score = random.randrange(10)
        players_list.append(Player(rand_name, rand_score)) 
        print(rand_name, rand_score)
    return players_list, M

'''
get_teams_combinations : Uses backtracking to get all combinations of possible teams
    team - arr of players
    score - cummulative scores of players in team
'''
def get_teams_combinations(players_list, M):

    teams = []
    reference_arr = [False]*len(players_list)
    
    # Returns the combinations of teams with their scores
    def combinations(actual_arr, max_size, start, curr_len, used_arr):
        if curr_len == max_size:
            sum = 0 
            obj = Team([], 0)
            for i in range(len(actual_arr)):
                if used_arr[i] == True:
                    obj.team.append(actual_arr[i].name)
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
    
    combinations(players_list, M, 0, 0, reference_arr)

    return teams
            
def get_score_diff(teams):
    return teams