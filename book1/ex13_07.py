
# You are a photographer for a soccer meet. You will be taking pictures of pairs
# of opposing teams. All teams have the same number of players. A team photo
# consist of a front row of players and a back row of players. A player
# in the back row must be taller than the player in front of him. All players
# in a row must be from the same team.

# Problem 13.6: Design an algorithm that takes as input two teams and the
# height of the players in the teams and checks if it is possible to place
# players to take the photo subject to the placement constraints.

import unittest


def IsPhotoPossible(teamA, teamB):
    
    n = len(teamA)
    m = len(teamB)
    assert n == m
    
    # Soft teams by height
    teamA.sort()
    teamB.sort()
    
    temp = 0
    for (a, b) in zip(teamA,teamB):
        if a > b: temp += 1
    
    # So in the loop above we simultaneously handled both cases
    # when teamA is smaller and when teamB is smaller
    if (temp == 0) or (temp == n): 
        return True  # can do the photo
    else:
        return False
    

class Ex13_07(unittest.TestCase):
    
    def test_SimpleTeamCheck(self):
        teamA = [180, 170, 190, 175, 200]
        teamB = [200, 201, 180, 195, 175]
        self.assertTrue(IsPhotoPossible(teamA, teamB))
        
        teamA = [180, 170, 190, 175, 200]
        teamB = [200, 201, 180, 195, 165]
        self.assertFalse(IsPhotoPossible(teamA, teamB))

if __name__ == "__main__":
    unittest.main()