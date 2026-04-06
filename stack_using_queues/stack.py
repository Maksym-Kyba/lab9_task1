class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.queue = None
        self._rear = None

    def is_empty(self):
        if self.queue is None:
            return True
        return False


    def add(self, item):
        if self.is_empty():
            self.queue = Node(item)
            self._rear = self.queue
        else:
            new_item = Node(item)
            self._rear.next = new_item
            self._rear = self._rear.next

    def pop(self):
        if self.is_empty():
            return 'Queue пуста'
        if len(self) == 1:
            deleted_elem = self.queue.data
            self._rear = None
            self.queue = None
            return deleted_elem

        deleted_elem = self.queue.data
        self.queue = self.queue.next

        return deleted_elem

    def peek(self):
        if self.is_empty():
            return 'Queue пуста'
        return self.queue.data

    def __len__(self):
        if not self.is_empty():
            length = 1
            head = self.queue
            while head.next is not None:
                length += 1
                head = head.next

            return length
        return 0

    def __str__(self):
        if not self.is_empty():
            representation = 'front -> '
            head = self.queue
            while head.next is not None:
                representation += str(head.data0) + '; '
                head = head.next
            representation += str(head.data) + '<- rear'
            return representation
        return 'Queue is empty'


class MyStack(object):
    def __init__(self):
        self.stack = Queue()
        self._reversed_stack = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.add(x)

    def pop(self):
        """
        :rtype: int
        """
        while(len(self.stack)) > 1:
            deleted_elem = self.stack.pop()
            self._reversed_stack.add(deleted_elem)

        deleted_elem = self.stack.pop()
        self.stack, self._reversed_stack = self._reversed_stack, self.stack
        return deleted_elem

    def top(self):
        """
        :rtype: int
        """
        while(len(self.stack)) > 1:
            deleted_elem = self.stack.pop()
            self._reversed_stack.add(deleted_elem)
        deleted_elem = self.stack.pop()
        self._reversed_stack.add(deleted_elem)
        self.stack, self._reversed_stack = self._reversed_stack, self.stack
        return deleted_elem

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.is_empty() and self._reversed_stack.is_empty()


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
