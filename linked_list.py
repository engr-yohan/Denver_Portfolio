<<<<<<< HEAD
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data!r})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"

    # insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # remove at beginning (alias remove_beginning)
    def remove_at_beginning(self):
        if not self.head:
            raise IndexError("remove_at_beginning from empty list")
        removed = self.head
        self.head = self.head.next
        removed.next = None
        self.size -= 1
        return removed.data

    def remove_beginning(self):
        return self.remove_at_beginning()

    # insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    # remove at end
    def remove_at_end(self):
        if not self.head:
            raise IndexError("remove_at_end from empty list")
        current = self.head
        if not current.next:
            # only one node
            data = current.data
            self.head = None
            self.size -= 1
            return data
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        self.size -= 1
        return current.data

    # insert at index (0-based)
    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.insert_at_beginning(data)
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    # remove at index (0-based)
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_at_beginning()
        current = self.head
        prev = None
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        current.next = None
        self.size -= 1
        return current.data

    # search for value, return first index or -1
    def search(self, data):
        current = self.head
        idx = 0
        while current:
            if current.data == data:
                return idx
            current = current.next
            idx += 1
        return -1

    # remove by value (first occurrence)
    def remove_by_value(self, data):
        if not self.head:
            raise ValueError("remove from empty list")
        current = self.head
        prev = None
        idx = 0
        while current:
            if current.data == data:
                if prev is None:
                    # head
                    self.head = current.next
                else:
                    prev.next = current.next
                current.next = None
                self.size -= 1
                return idx
            prev = current
            current = current.next
            idx += 1
        raise ValueError("value not found")

    # For compatibility: alias remove_at(self, data) expected by user? We'll provide remove_at_value
    def remove_at_by_value(self, data):
        return self.remove_by_value(data)


if __name__ == "__main__":
    ll = LinkedList()
    for x in [1,2,3]:
        ll.insert_at_end(x)
    print(ll)
=======
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data!r})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"

    # insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # remove at beginning (alias remove_beginning)
    def remove_at_beginning(self):
        if not self.head:
            raise IndexError("remove_at_beginning from empty list")
        removed = self.head
        self.head = self.head.next
        removed.next = None
        self.size -= 1
        return removed.data

    def remove_beginning(self):
        return self.remove_at_beginning()

    # insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    # remove at end
    def remove_at_end(self):
        if not self.head:
            raise IndexError("remove_at_end from empty list")
        current = self.head
        if not current.next:
            # only one node
            data = current.data
            self.head = None
            self.size -= 1
            return data
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        self.size -= 1
        return current.data

    # insert at index (0-based)
    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.insert_at_beginning(data)
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    # remove at index (0-based)
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_at_beginning()
        current = self.head
        prev = None
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        current.next = None
        self.size -= 1
        return current.data

    # search for value, return first index or -1
    def search(self, data):
        current = self.head
        idx = 0
        while current:
            if current.data == data:
                return idx
            current = current.next
            idx += 1
        return -1

    # remove by value (first occurrence)
    def remove_by_value(self, data):
        if not self.head:
            raise ValueError("remove from empty list")
        current = self.head
        prev = None
        idx = 0
        while current:
            if current.data == data:
                if prev is None:
                    # head
                    self.head = current.next
                else:
                    prev.next = current.next
                current.next = None
                self.size -= 1
                return idx
            prev = current
            current = current.next
            idx += 1
        raise ValueError("value not found")

    # For compatibility: alias remove_at(self, data) expected by user? We'll provide remove_at_value
    def remove_at_by_value(self, data):
        return self.remove_by_value(data)


if __name__ == "__main__":
    ll = LinkedList()
    for x in [1,2,3]:
        ll.insert_at_end(x)
    print(ll)
>>>>>>> 05e004d (Add linked list implementation, tests, and README improvements)
