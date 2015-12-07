

#String inside fullList
def InclusionStringComparison(fullList, string):
        for subList in fullList:
            if string[0] == subList:
                return True
        return False 

#Standart application in Sphinx
print InclusionStringComparison(['Kozel', 'Osel'], ['Koze']) #False

print InclusionStringComparison(['Kozel', 'Osel'], ['Kozel']) #True

#Case doesn't work, yes, because we compare lists everywhere
print InclusionStringComparison(['Kozel', 'Osel'], 'Kozel') #False

#To make it works, for example

def InclusionStringComparisonNew(fullList, string):
        if isinstance(string, list):
            string = string[0]
    
        for subList in fullList:
            if string == subList:
                return True
        return False 
    
print InclusionStringComparisonNew(['Kozel', 'Osel'], ['Koze']) #False

print InclusionStringComparisonNew(['Kozel', 'Osel'], ['Kozel']) #True

print InclusionStringComparisonNew(['Kozel', 'Osel'], 'Kozel') #True