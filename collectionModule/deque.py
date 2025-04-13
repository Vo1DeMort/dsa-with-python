from collections import deque

#NOTE: double ended que that supports append 
# and pop from both sides
s = deque()
print(s)

my_queue = deque([1,2,'name'])

# append at the right
my_queue.append('age')

# append at the left
my_queue.appendleft('hello')

#  pop the right value
my_queue.pop()

# pop the left value
my_queue.popleft()

