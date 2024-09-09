import random

class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []
        
    def enqueue(self, d):
        self.a_in.append(d)
        
    def dequeue(self):
        if (self.a_out == []):
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = []
        return self.a_out.pop(0)

def main():
    queue = Queue()

    #making sure queue stays balanced & getting enqueue ratio
    while True:
        enqueue_ratio = float(input("Please enter the enqueue operations probability (choose a number between 50-100.): "))
        if 50 <= enqueue_ratio <= 100:
            break
        print("Please enter a number between 50 - 100 ONLY.")

    #calculating dequeue ratio
    dequeue_ratio = 100 - enqueue_ratio

    #initiating counters for cheap and costly ops
    cheap_ops = 0
    costly_ops = 0

    #beginning for loop to see if to do the enqueue or dequeue
    for i in range(100000):
        #using random.random to get a number between 0 and 1
        if random.random() < enqueue_ratio/100:
            queue.enqueue(random.randint(1, 1000)) #enqueuing a random int value to the queue
            cheap_ops += 1 #incrementing cheap ops count
        elif random.random() < dequeue_ratio/100: #determining if to dequeue or not
            queue.dequeue() #dequeueing from queue
            costly_ops += 1 #incrementing costly ops

    #printing cheap and costly ops
    print("Cheap Operations: ", cheap_ops)
    print("Costly Operations: ", costly_ops)

main()
        
        
        
        
