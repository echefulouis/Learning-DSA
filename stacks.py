class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
        
    def print_itself(self):
        temp=self.top
        while temp is not None:
            print(temp.val)
            temp=temp.next
        
    def push(self,value):
        new_node=Node(value)
        if not self.top:
            self.top=new_node
        else:
            temp=self.top
            self.top=new_node
            new_node.next=temp
        self.height=self.height+1
    
    def pop(self):
        if self.length==0:
            return
        temp=self.top
        self.top=temp.next
        temp.next=None
        self.height=self.height-1
        return temp
        
my_stack=Stack(2)
my_stack.push(3)

my_stack.print_itself()

