# Pair users by attributes
# You are building a social network site where each user specifies
# a set of attributes. You would like to pair each user with another
# unpaired user that specified exactly the same set of attributes.

# Problem 12.5: You are given a sequence of users where each user
# has a unique 32-bit integer key and a set of attributes specified
# as strings. When you read a user, you should pair that user with
# another previously read user with identical attributes who is 
# currently unpaired, if such user exists. If the user can't be paired,
# you should keep him in the unpaired set. How would you implement this
# matching process efficiently?

import unittest


class User():
    
    def __init__(self, ID, attributes):
        self.ID = ID
        self.attributes = attributes       # list of strings
        self.pairID = None
        self.hash = None
    
    def __CalculateHashOrder(self):
        # Calculate hash when order of attributes is important
        h = 0
        for i, attribute in enumerate(self.attributes):
            for k, letter in enumerate(attribute):
                h = (h + (i + 1) * (k + 1) * ord(letter)) % 2**10
        return h
        
    def __CalculateHash(self):
        # Calculate hash when order of attributes is not important
        self.attributes.sort()
        s = ''.join(self.attributes)
        h = 0
        for i, letter in enumerate(s):
            h = (h + (i + 1) * ord(letter)) % 2**10
        return h
        
    def GetAttributes(self):
        return self.attributes
    
    def GetID(self):
        return self.ID
    
    def GetAttributesHash(self):
        if self.hash == None:
            self.hash = self.__CalculateHash()
        return self.hash

    def SetPairID(self, pairID):
        self.pairID = pairID
        
    def GetPairID(self):
        return self.pairID


class SocialNetwork():
    
    def __init__(self):
        self.paired = []
        self.nonpaired = []

    def AddUser(self, user):
        
        for npuser in self.nonpaired:
            if user.GetAttributesHash() == npuser.GetAttributesHash():
                # Set pair IDs
                npuser.SetPairID(user.GetID())
                user.SetPairID(npuser.GetID())
                
                # Put users in correct lists
                self.nonpaired.remove(npuser)
                self.paired.append(npuser)
                self.paired.append(user)
                
                # We are done with the user
                return
        
        # Pair wasn't found
        self.nonpaired.append(user)
        return

class Ex12_05Test(unittest.TestCase):
    
    def test_FindPairSimple(self):
        
        sn = SocialNetwork()
        
        user1 = User(101, ['student', '20'])
        sn.AddUser(user1)
        self.assertEqual(sn.paired, [])
        self.assertEqual(sn.nonpaired, [user1])
        
        user2 = User(202, ['worker', '30'])
        sn.AddUser(user2)
        self.assertEqual(sn.paired, [])
        self.assertEqual(sn.nonpaired, [user1, user2])

        user3 = User(303, ['student', '20'])
        sn.AddUser(user3)
        self.assertEqual(sn.paired, [user1, user3])
        self.assertEqual(sn.nonpaired, [user2])

        # When order of attributes isn't important
        user4 = User(404, ['30', 'worker'])                
        sn.AddUser(user4)
        self.assertEqual(sn.paired, [user1, user3, user2, user4])
        self.assertEqual(sn.nonpaired, [])

        self.assertEqual(user1.GetID(), user3.GetPairID())
        self.assertEqual(user3.GetID(), user1.GetPairID())
        self.assertEqual(user2.GetID(), user4.GetPairID())
        self.assertEqual(user4.GetID(), user2.GetPairID())


if __name__ == "__main__":
    unittest.main() 