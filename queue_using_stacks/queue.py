class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.stack = None

    def is_empty(self):
        if self.stack is None:
            return True
        return False

    def push(self, item):
        new_item = Node(item)
        new_item.next = self.stack
        self.stack = new_item

    def pop(self):
        if self.is_empty():
            return 'Stack пустий'
        deleted_elem = self.stack.data
        self.stack = self.stack.next

        return deleted_elem

    def peek(self):
        if self.is_empty():
            return 'Stack пустий'
        return self.stack.data

    def __len__(self):
        if not self.is_empty():
            length = 1
            head = self.stack
            while head.next is not None:
                length += 1
                head = head.next

            return length
        return 0

    def __str__(self):
        if not self.is_empty():
            representation = ''
            head = self.stack
            while head.next is not None:
                representation += str(head.data) + ': '
                head = head.next
            representation += str(head.data)
            return representation
        return 'Stack is empty'



class MyQueue(object):

    def __init__(self):
        self.queue1 = Stack()
        self._reversed_queue = Stack()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self._reversed_queue.is_empty():
            while self.queue1.is_empty() is False:
                self._reversed_queue.push(self.queue1.pop())
        return self._reversed_queue.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self._reversed_queue.is_empty():
            while self.queue1.is_empty() is False:
                self._reversed_queue.push(self.queue1.pop())
        return self._reversed_queue.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue1.is_empty()

obj = MyQueue()
obj.push(2)
obj.push(3)
print(str(obj))
print(obj.peek())
print(obj.pop())
print(obj.empty())
