class Node(object):
    """
    Object for storing a single node of a link list
    Models 2 attributes:
        data
        next node to the list
    """
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node Data>: %s" % self.data


class LinkedList(object):
    """
    singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        takes O(n) time
        :return: the size of the linkedList
        """

        current = self.head
        counter = 0
        while current:
            current = current.next_node
            counter += 1
        return counter

    def add(self, data):
        """
        Add a node to the head
        :param data: value to be added into a Node
        :return: updates the LinkedList with a new Node added to the head
        takes O(n) time

        """
        new_node = Node(data)
        current = self.head
        self.head = new_node
        self.head.next_node = current

    def search(self, target):
        """
        Method to return the first node with the desired target else None
        :param target: value to look for
        :return: Node or None
        Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == target:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, position):
        """
        Method to insert a node at any given position
        :param data: Int value
        :param position: Index to add it in
        :return: True is LinkedList was update, else False
        Takes O(n) time
        """
        if position == 0:
            self.add(data)
            return True
        new_data = Node(data)
        current = self.head
        index = 1
        while index != position:
            index += 1
            if current.next_node:
                current = current.next_node
            else:
                return False
        new_data.next_node = current.next_node
        current.next_node = new_data
        return True

    def removeData(self, data):
        """
        Removed the Node specified
        :param data: data to remeove
        :return: removed Node or None
        """
        current = self.head
        previous = None

        while current and current.data != data:
            previous = current
            current = current.next_node

        if not current:
            return None

        if previous is None:
            self.head = current.next_node
            current.next_node = None
        else:
            previous.next_node = current.next_node
        return current


    def __repr__(self):
        current = self.head
        nodes = ["[head:%s]" % current.data]

        while current.next_node:
            current = current.next_node

            if current.next_node:
                nodes.append("[%s]" % current.data)
            else:
                nodes.append("[tail:%s]" % current.data)

        return "-> ".join(nodes)


def main():
    l = LinkedList()
    print(l.is_empty())
    l.add(10)
    l.add(20)
    l.add(30)
    l.add(40)
    l.add(50)
    l.add(60)
    print("Size: %s" % l.size())
    print(l)
    print(l.is_empty())
    print(l.search(20))
    print(l.search(80))
    print(l.insert(45, 2))
    print(l)
    print(l.removeData(300))
    print(l)



if __name__ == '__main__':
    main()
