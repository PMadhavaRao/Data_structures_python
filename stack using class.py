class Stack:
    def __init__(self):
        self.stack=list()
    def push(self,data):
        self.stack.append(data)
        print('the data:(data)pushed successfully into the stack')
        print("now the stack",self.stack)
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
            return None
        data=self.stack.pop()
        print("now the stack is:",self.stack)
        return data
def main():
    stack=Stack()
    while True:
        print('1.Menu')
        print('2.push')
        print('3.pop')
        print('4.exit')
        operation=int(input("enter operation"))
        if operation==1:
            data=int(input("entr data to push"))
            stack.push(data)
        elif operation==2:
            data=stack.pop()
            if data!=None:
                print(f'(data)is popped from stack')
        elif operation==3:
            break
        else:
            print("enter correct operation")
main()
