queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full")
    else:
        element=int(input("enter the element"))
        queue.append(element)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        element=queue.pop(0)
        print("removed element",element)
        print(queue)
n=int(input("enter limit of queue"))
while(1):
      print("select operation 1.enqueue 2.dequeue")
      choice=int(input("enter choice:"))
      if choice==1:
        enqueue()
      elif choice==2:
        dequeue()
      elif choice==3:
        break
      else:
        print("enter correct operation")   
