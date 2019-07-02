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
    
def get_match_making_list(teams):
    diff_list = utils.get_score_diff(teams)
    return diff_list


def init():
    # Inputs
    # players_list, M = utils.get_user_inputs()
    players_list, M = utils.get_random_inputs(6, 3)
    
    # Possible combinations of teams
    teams = get_possible_teams(players_list, M)

    # Possible combinations of teams
    match_making_list = get_match_making_list(teams)



if __name__ == '__main__':
    init() 