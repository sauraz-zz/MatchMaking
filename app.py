import utils


'''
get_possible_groups : Returns all possible groups of size M
Time-complexity: O(2^N - 1)
'''
def get_possible_teams(players_list, M):

    print("get_possible_groups")
    teams = utils.get_teams_combinations(players_list, M)
    for obj in teams:
        print("Team - {}  Score - {}".format(obj.team, obj.score))
    return teams

'''
calculate_match_making - Calculates match_making based on teams
    Prints down best-worst match_making 
'''
def calculate_match_making(teams):
    match_making_list = utils.get_team_diff_list(teams)
    for i, x in enumerate(match_making_list):
        print("{} - {}".format(i+1, x))


def init():
    # Inputs
    players_list, M = utils.get_user_inputs()
    # players_list, M = utils.get_random_inputs(4, 2)
    
    # Possible combinations of teams
    teams = get_possible_teams(players_list, M)

    # Possible combinations of teams
    calculate_match_making(teams)



if __name__ == '__main__':
    init() 