class MyUnionFind:
    def __init__(self, value):
        self.value = value
        self.parent = self

    def union(self, other: MyUnionFind):
        self.parent = other.find()

    def find(self):
        while self.parent is not self.parent.parent:
            self.parent = self.parent.parent
        return self.parent
