class MyTreeNode:
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.parent = parent
        self.right = None
        self.left = None
        self.depth = 0
        self.height = 0
        self.maintain_height_and_depth()

    def maintain_height_and_depth(self):
        pointer = self
        while pointer is not None:
            pointer.depth = 1 if pointer.parent is None else pointer.parent.depth + 1

            right_height = -1 if pointer.right is None else pointer.right.height
            left_height = -1 if pointer.left is None else pointer.left.height
            pointer.height = max(left_height, right_height) + 1
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

    def __str__(self):
        return "[" + str(self.key) + "," + str(self.value) + "]"

    def find_node(self, key):
        if self.key == key:
            return self
        elif self.key < key:
            if self.right is None:
                return None
            else:
                return self.right.find_node(key)
        else:
            if self.left is None:
                return None
            else:
                return self.left.find_node(key)

    def find(self, key):
        found_node = self.find_node(key)
        if found_node is None:
            return None
        return found_node.value

    def print_node(self, level=0):
        if self.left is not None:
            self.left.print_node(level + 1)
        print(' ' * 4 * level + '-> ' + str(self))
        if self.right is not None:
            self.right.print_node(level + 1)
    
    def successor(self):
        if self.right is not None:
            pointer = self.right
            while pointer.left is not None:
                pointer = pointer.left
            return pointer
        elif self.parent.right is self:
            pointer = self.parent
            while pointer.parent is not None and pointer.parent.right is pointer:
                pointer = pointer.parent
            if pointer.parent is None:
                return None
            return pointer.parent



class MyBinarySearchTree:
    def __init__(self):
        self.root_node = None

    def min(self):
        return self.root_node.min()

    def max(self):
        return self.root_node.max()

    def insert(self, key, value):
        if self.root_node is None:
            self.root_node = MyTreeNode(key, value, None)
        else:
            self.root_node.insert(MyTreeNode(key, value, None))
        while self.root_node.parent is not None:
            self.root_node = self.root_node.parent
        self.root_node.top_down_find_height()

    def delete(self, key):  # TODO
        to_delete = self.root_node.find_node(key)
        if to_delete is None:
            return

        # if it's a leaf, simply detach it.
        if to_delete.is_leaf(): 
            print("We are to delete a leaf!")
            if self.root_node is to_delete:
                self.root_node = None
            else:
                if to_delete.parent.left is to_delete:
                    to_delete.parent.left = None
                else:
                    to_delete.parent.right = None
            return

        # In case it isn't a leaf, it has children. now, let's take care of the case where there's one child.
        if to_delete.left is None:  # Meaning there's only a right child
            to_delete.right.parent = to_delete.parent
            if self.root_node is to_delete:
                self.root_node = to_delete.right
            elif to_delete.parent.left is to_delete:
                to_delete.parent.left = to_delete.right
            else:
                to_delete.parent.right = to_delete.right
            return
        if to_delete.right is None:  # Meaning there's only a left child
            to_delete.left.parent = to_delete.parent
            if self.root_node is to_delete:
                self.root_node = to_delete.right
            elif to_delete.parent.left is to_delete:
                to_delete.parent.left = to_delete.left
            else:
                to_delete.parent.right = to_delete.left
            return
        
        # If we got here, it means there are two children. 
        successor = to_delete.successor()
        if successor is None:  # Then it's the max node - simply detach it.
            if self.root_node is to_delete:
                self.root_node = self.root_node.left  # This works both for self.size == 1 and self.size > 1
            else:
                to_delete.parent.right = to_delete.left
        else:  # replace successor and to_delete's value and key, then detach successor
            if to_delete.right is successor:
                successor.parent = to_delete.parent
                successor.left = to_delete.left
                if self.root_node is to_delete:
                    self.root_node = successor
                elif to_delete.parent.left is to_delete:
                    to_delete.parent.left = successor
                else:
                    to_delete.parent.right = successor
            else: 
                successor.left = to_delete.left
                if successor.left is not None:
                    successor.left.parent = successor
                successor.parent.left = successor.right
                successor.right = to_delete.right
                successor.parent = to_delete.parent
                if to_delete.parent is None:
                    self.root_node = successor
                elif to_delete.parent.right is to_delete:
                    to_delete.parent.right = successor
                else:
                    to_delete.parent.left = successor
            


    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.root_node.find(key)

    def print_tree(self):
        self.root_node.print_node(0)



def test():
    my_tree = MyBinarySearchTree()
    my_tree.insert(4,5)
    my_tree.insert(2,5)
    my_tree.insert(6,5)
    my_tree.insert(1,5)
    my_tree.insert(5,5)
    my_tree.insert(7,5)
    my_tree.insert(3,5)
    my_tree.print_tree()
    print()
    my_tree.delete(4)
    my_tree.print_tree()
    print()
    my_tree.delete(2)
    my_tree.print_tree()

test()