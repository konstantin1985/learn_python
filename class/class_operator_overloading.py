

print "-"*20 + "#1 Indexing and Slicing: __getitem__ and __setitem__" + "-"*20

class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print X[2]               #4

for i in range(5):
    print(X[i])          #0 1 4 9 16

