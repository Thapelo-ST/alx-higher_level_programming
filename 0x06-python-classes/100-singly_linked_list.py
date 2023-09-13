#!/usr/bin/python3
"""
this class holds a node of a singly linked list
"""


class Node:
    """
    initializes data and next node
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    """modules that are getters and setters starts here"""
    @property
    def data(self):
        """
        data getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data setter checks if the value passed is an integer or not
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next node getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next node setter checks if value is none or a node before assigning
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value

    """modules that are getters and setters ends here"""


"""
this class is for ordered singly linked lists
"""


class SinglyLinkedList:
    """
    initialises the head pointer
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        insert the new node in the correct order
        -first checks if the list is empty or the value is less or above the
        ones in the list
        -goes in the list and find the correct position to insert at
        - insert the new node after it finds the correct position
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and value >= current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        printing the list in the stdout, one node number per line
        """
        if self.head is None:
            return "Empty list"

        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
