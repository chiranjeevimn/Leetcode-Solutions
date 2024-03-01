
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Add the new element to queue1
        self.queue1.append(x)
        
        # Move all elements back to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        # Pop the element from the top of the stack (front of queue1)
        return self.queue1.popleft()

    def top(self) -> int:
        # Return the element from the top of the stack (front of queue1)
        return self.queue1[0]

    def empty(self) -> bool:
        # Check if the stack is empty
        return not bool(self.queue1)