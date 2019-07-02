import unittest
import utils


class TestMatchMaking(unittest.TestCase):
    def test_get_teams_combinations(self):
        """
        Test get_teams_combinations
        """
        data, M = utils.get_random_inputs(10,2)
        result = utils.get_teams_combinations(data, M)
        self.assertEqual(len(result), 45)

    def test_get_team_diff_list(self):
        """
        Test get_team_diff_list
        """
        data = [utils.Team(set(['Dorothy']), 1), utils.Team(set(['David']), 7)]
        result = utils.get_team_diff_list(data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].diff, 6)

if __name__ == '__main__':
    unittest.main()