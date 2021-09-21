#First in First Out Stack implementation
class MyQueue(object):

    def __init__(self):
        """
        Initialize data structure.
        """
        self.queue = []
        self.queue2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        val = self.queue[0]
        del self.queue[0]
        return val

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()