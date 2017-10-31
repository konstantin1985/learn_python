# Problem 8.6: Design an algorithm that processes buildings as they are presented to it and tracks
# the building that have a view of the sunset. The number of buildings is not known in advance.
# Buildings are given in EAST-TO-WEST order and are specified by their heights. The amount of memory
# your algorithm uses should depend solely on the number of buildings that have a view;
# in particular it should not depend on the number of buildings processed.


import unittest

class SimpleAlgorithm:
    # It should use a stack but there is no one
    
    def __init__(self):
        self.buildingsView = []
    
    def AddBuilding(self, b):
        
        # IMPORTANT: there is a problem if you try to pop elements in the for loop
        # IndexError: list index out of range
        # for i in range(len(someList)):
        #    if someList[i] > b 
        #        someList.pop(i)
        
        # Prune buildings with view
        self.buildingsView = [x for x in self.buildingsView if x > b]
                
        # Append the new building, it always has view
        self.buildingsView.append(b)
    
    def GetBuildingsView(self):
        return self.buildingsView


class Ex8_6Test(unittest.TestCase):
    
    def test_SimpleAlgorithm(self):
        s = SimpleAlgorithm()
        s.AddBuilding(19)
        s.AddBuilding(10)
        s.AddBuilding(20)
        s.AddBuilding(11)
        s.AddBuilding(5)
        s.AddBuilding(6)
        self.assertEqual(s.GetBuildingsView(), [20, 11, 6])


if __name__ == "__main__":
    unittest.main()