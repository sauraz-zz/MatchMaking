import utils
import json


'''
get_possible_groups : Returns all possible groups of size M
Time-complexity: O(2^N - 1)
'''
def get_possible_teams(players_list, M):
    
    print("\n------------ Players List ----------\n")
    for i, x in enumerate(players_list):
        print("{} - {}".format(i+1, x))

    # get_teams_combinations for players_list
    teams = utils.get_teams_combinations(players_list, M)
    
    print("\n------------ Teams Combinations ----------\n")
    for i, x in enumerate(teams):
        print("{} - {}".format(i+1, x))
    return teams

'''
calculate_match_making - Calculates match_making based on teams
    Prints down best-worst match_making 
'''
def calculate_match_making(teams):
    
    match_making_list = utils.get_team_diff_list(teams)
    
    print("\n------------ Match Making ----------\n")
    for i, x in enumerate(match_making_list):
        print("{} - {}".format(i+1, x))
    print("\n")

def init(config):
    
    # Inputs
    if config["useRandomInput"]:
        players_list, M = utils.get_random_inputs(config["defaultPlayers"], config["defaultTeamSize"])
    else:
        players_list, M = utils.get_user_inputs()
    
    # Possible combinations of teams
    teams = get_possible_teams(players_list, M)

    # Possible combinations of teams
    calculate_match_making(teams)



if __name__ == '__main__':
    
    with open('config.json') as f:
        config = json.load(f)
    if not config:
        raise("Configuration File not found")

    init(config) 