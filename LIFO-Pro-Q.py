import queue
q = queue.LifoQueue()
number = [1,2,3,4,5,6]
for x in number:
    q.put(x)

print(q.get())
print(q.get())

print("\n \n Prioty Queue\n\n")
print("==========================")

q1= queue.PriorityQueue()
q1.put((2,"Hello world"))
q1.put((11,44))
q1.put((1,"Testing Queue"))

while not q1.empty():
    print(q1.get())

q2= queue.PriorityQueue()
q2.put((2,"Hello world"))
q2.put((11,44))
q2.put((1,"Testing Queue"))


while not q2.empty():
    print(q2.get()[1])
