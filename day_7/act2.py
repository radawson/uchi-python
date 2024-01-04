class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        current = self.head
        if self.head is None:
            print("Linked list is empty")
        else:
            while current is not None:
                #print(current.data)
                print(f"{current.data}", end="")
                if current.reference is not None:
                    print(" -> ", end="")
                current = current.reference
        print()

    def add_to_start(self, data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node

    def add_item_after(self, data, value):
        new_node = Node(data)
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                new_node.reference = current_node.reference
                current_node.reference = new_node
                break
            else:
                current_node = current_node.reference

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.reference is not None:
                current_node = current_node.reference
            current_node.reference = new_node

    def remove_item(self, value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == value:
                if previous_node is None:
                    self.head = current_node.reference
                else:
                    previous_node.reference = current_node.reference
                break
            else:
                previous_node = current_node
                current_node = current_node.reference


if __name__ == "__main__":
    node1 = Node(5)
    print(node1.data)
    print(node1.reference)
    print("_" * 20)
    node2 = Node(11)
    node1.reference = node2
    print(node1.reference)
    print("_" * 20)
    linked_list1 = LinkedList()
    linked_list1.print_linked_list()
    print("_" * 20)
    linked_list1 = LinkedList()
    linked_list1.add_to_start(82)
    linked_list1.add_to_start(15)
    linked_list1.print_linked_list()
    print("_" * 20)
    linked_list1.append(8)
    linked_list1.append(23)
    linked_list1.print_linked_list()
    print("_" * 20)
    linked_list1.add_item_after(100, 15)
    linked_list1.add_item_after(42, 8)
    linked_list1.print_linked_list()
    print("_" * 20)
    linked_list1.remove_item(8)
    linked_list1.print_linked_list()
