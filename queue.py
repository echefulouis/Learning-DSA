class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
    
    def print_itself(self):
        temp=self.first
        while temp:
            print(temp.val)
            temp=temp.next
    
    def enqueue(self,value):
        new_node=Node(value)
        self.last.next=new_node
        self.last=new_node