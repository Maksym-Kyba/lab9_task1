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
                representation += f'{head.data}; '
                head = head.next
            representation += f'{head.data} <- rear'
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
        if self._reversed_stack.is_empty():
            while self.stack.is_empty() is False:
                self._reversed_stack.add(self.stack.pop())

        return self._reversed_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self._reversed_stack.is_empty():
            while self.stack.is_empty() is False:
                self._reversed_stack.add(self.stack.pop())

        return self._reversed_stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.is_empty() and self._reversed_stack.is_empty()
