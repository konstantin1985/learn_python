

def countLines(name):
    count = 0
    for _ in open(name):
        count += 1
    return count

def countChars(name):
    count = 0
    for line in open(name):
        count += len(line)
    return count

def test(name):
    return(countLines(name), countChars(name))
    
    
if __name__ == "__main__":
    test("mymod.py")