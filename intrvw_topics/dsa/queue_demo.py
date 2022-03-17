class Queue:
    def __init__(self, size):
        self.que = []
        self.front = -1
        self.rear = -1
        self.capacity = size

    def isEmpty(self):
        if self.front == -1:
            return True
        return False

    def isFull(self):
        if(self.front >= 0 and self.rear == (self.capacity - 1)):
            return True
        return False

    def enqueue(self, item):
        if(self.isFull()):
            print("Queue is full. Cannot insert any more elements.")
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            self.rear = self.rear + 1
            self.que.append(item)
            print(f"Item {item} inserted succesfully.")

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty. First insert some elements.")
        else:
            ele = self.que[self.front]
            if self.front >= self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = self.front + 1
            print(f"Element {ele} removed.")
            return ele
    
    def display_queue(self):
        if self.isEmpty():
            print("Queue is empty. Nothing to display.")
        else:
            print("Front index -> ",self.front)
            print("The items -->")
            for i in range(self.front, self.rear+1):
                print(self.que[i-1], end=" ")
            print()
            print("Rear index -> ",self.rear)

que = Queue(5)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)

que.display_queue()

que.dequeue()

print("After removing an element")
que.display_queue()
