class MyAVLTreeNode:
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.parent = parent
        self.right = None
        self.left = None
        self.depth = 0
        self.height = 0
        self.balance_factor = 0
        self.maintain_height_and_depth()

    def maintain_height_and_depth(self):
        pointer = self
        while pointer is not None:
            pointer.depth = 1 if pointer.parent is None else pointer.parent.depth + 1

            right_height = -1 if pointer.right is None else pointer.right.height
            left_height = -1 if pointer.left is None else pointer.left.height
            pointer.height = max(left_height, right_height) + 1
            pointer.calculate_balance_factor()
            pointer = pointer.parent

    def top_down_find_depth(self, depth):
        self.depth = depth + 1
        if self.right:
            self.right.top_down_find_depth(self.depth)
        if self.left:
            self.left.top_down_find_depth(self.depth)

    def top_down_find_height(self):
        if self.left is None:
            left_height = 0
        else:
            self.left.top_down_find_height()
            left_height = self.left.height
        if self.right is None:
            right_height = 0
        else:
            self.right.top_down_find_height()
            right_height = self.right.height
        self.height = max(left_height, right_height) + 1

    def calculate_balance_factor(self):
        left_height = -1 if self.left is None else self.left.height
        right_height = -1 if self.right is None else self.right.height
        self.balance_factor = left_height - right_height

    def left(self):
        return self.left

    def right(self):
        return self.right

    def parent(self):
        return self.parent

    def value(self):
        return self.value

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.right is None and self.left is None

    def min(self):  # return the minimum node in self's subtree
        pointer = self
        while pointer.left is not None:
            pointer = pointer.left
        return pointer

    def max(self):  # return the maximum node in self's subtree
        pointer = self
        while pointer.right is not None:
            pointer = pointer.right
        return pointer

    def insert(self, node):
        if node.key > self.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
        elif node.key < self.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        node.maintain_height_and_depth()
        node.maintain_balance()
        node.maintain_height_and_depth()

    def __str__(self):
        return "[" + str(self.key) + "," + str(self.value) + "]"

    def find(self, key):
        if self.key == key:
            return self.value
        elif self.key < key:
            if self.right is None:
                return None
            else:
                return self.right.find(key)
        else:
            if self.left is None:
                return None
            else:
                return self.left.find(key)

    def maintain_balance(self):
        if self.balance_factor == -2:
            if self.right.balance_factor == -1:
                self.RR()
            elif self.right.balance_factor == 1:
                self.RL()
        elif self.balance_factor == 2:
            if self.left.balance_factor == -1:
                self.LR()
            elif self.left.balance_factor == 1:
                self.LL()
        if self.parent is not None:
            self.parent.maintain_balance()

    def LL(self):
        former_parent = self.parent
        print("former parent is", str(former_parent))
        new_parent = self.left
        print("new parent is", str(new_parent))
        self.left = new_parent.right
        new_parent.right = self
        new_parent.parent = former_parent
        self.parent = new_parent
        if former_parent is not None:
            if former_parent.left == self:
                former_parent.left = new_parent
            else:
                former_parent.right = new_parent

    def LR(self):  # A-B-C notation is according to a lesson from TAU data structures
        A = self.left
        B = A.right
        C = self
        former_parent = self.parent

        A.right = B.left
        A.right.parent = A

        C.left = B.right
        C.left.parent = C

        B.right = C
        B.left = A
        A.parent = B
        C.parent = B

        B.parent = former_parent
        if former_parent is not None:
            if B.parent.left == self:
                B.parent.left = B
            else:
                B.parent.right = B

    def RL(self):
        A = self.right
        B = A.left
        C = self
        former_parent = C.parent


        A.left = B.right
        if A.left is not None:
            A.left.parent = A  # got an attributeError here, need fixing. TODO

        C.right = B.left
        if C.right is not None:
            C.right.parent = C

        B.left = C
        B.right = A
        A.parent = B
        C.parent = B

        B.parent = former_parent
        if former_parent is not None:
            if B.parent.left == self:
                B.parent.left = B
            else:
                B.parent.right = B

    def RR(self):
        former_parent = self.parent
        new_parent = self.right
        self.right = new_parent.left
        new_parent.left = self
        new_parent.parent = former_parent
        self.parent = new_parent
        if former_parent is not None:
            if former_parent.left == self:
                former_parent.left = new_parent
            else:
                former_parent.right = new_parent

    def print_node(self, level=0):
        if self.right is not None:
            self.right.print_node(level + 1)
        print(' ' * 4 * level + '-> ' + str(self))
        if self.left is not None:
            self.left.print_node(level + 1)

    def traversal(self, arr: list):
        if self.left is not None:
            self.left.traversal(arr)
        arr.append(self.key)
        if self.right is not None:
            self.right.traversal(arr)



class MyAVLTree:
    def __init__(self):
        self.root_node = None

    def min(self):
        return self.root_node.min()

    def max(self):
        return self.root_node.max()

    def insert(self, key, value):
        if self.root_node is None:
            self.root_node = MyAVLTreeNode(key, value, None)
        else:
            self.root_node.insert(MyAVLTreeNode(key, value, None))
        while self.root_node.parent is not None:
            self.root_node = self.root_node.parent
        self.root_node.top_down_find_height()

    def delete(self, key):  # TODO
        pass

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.root_node.find(key)

    def print_tree_visual(self):
        self.root_node.print_node(0)

    def tree_traversal(self):
        arr = []
        self.root_node.traversal(arr)
        return arr
