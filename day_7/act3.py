# Part 1: Create a BSTNode class
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


# Part 2: Create a BST class
class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = []

    def __str__(self):
        if self.root == None:
            return "The Tree is Empty"
        else:
            self.output = ""
            self.print_tree(node=self.root)
            return self.output

    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += " " * 4 * level + "-> " + str(node.data) + "\n"
            self.print_tree(node.left, level + 1)

    # Part 3: Add functionality to your BST class
    def add(self, node):
        if type(node) != int and type(node) != BSTNode:
            raise ValueError("Must be an integer or a BSTNode.")

        if type(node) == int:
            node = BSTNode(node)

        if node.data in self.contents:
            return "Node exists"

        if self.root == None:
            self.root = node
            self.contents.append(node.data)
            if node.right:
                self.contents.append(node.right.data)
            if node.left:
                self.contents.append(node.left.data)
            return "Root added"

        self.add_node(self.root, node)

    def add_node(self, current_node, new_node):
        # if new node > current node, go right
        if new_node.data > current_node.data:
            if current_node.right == None:
                current_node.right = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(current_node.right, new_node)
        else:
            if current_node.left == None:
                current_node.left = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(current_node.left, new_node)


if __name__ == "__main__":
    print(" expect 3, 4, None, 5")
    node1 = BSTNode(3)
    print(node1)
    node2 = BSTNode(4, left=node1)
    print(node2)
    node3 = BSTNode()
    print(node3)
    node3.data = 5
    print(node3)
    print("_" * 20)
    print("Expect The Tree is Empty, 4")
    bst = BST()
    print(bst)

    bst.root = node2
    print(bst)

    node2.right = node3
    print(bst)
    print("_" * 20)
    # create tree from image
    node8 = BSTNode(8)
    node3 = BSTNode(3)
    node10 = BSTNode(10)
    node1 = BSTNode(1)
    node6 = BSTNode(6)
    node14 = BSTNode(14)
    node4 = BSTNode(4)
    node7 = BSTNode(7)
    node13 = BSTNode(13)

    bst = BST()
    bst.add(node8)
    bst.add(node3)
    bst.add(node10)
    bst.add(node1)
    bst.add(node6)
    bst.add(node14)
    bst.add(node4)
    bst.add(node7)
    bst.add(node13)

    print(bst)
