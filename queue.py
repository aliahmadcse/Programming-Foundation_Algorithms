#import dequeu object,which is optimized for queue functionality
from collections import deque

#create an empty quue
queue=deque()

#append items to the queu
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

#removing the item from the front(begining) of the queue
x=queue.popleft()
print(x)
print(queue)