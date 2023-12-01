class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length=self.length+1
        return True

    def prepend(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length=self.length+1
        return True
    
    def pop(self):
        if not self.head:
            return None
        temp=self.tail
        if self.head.next is None:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length=self.length-1
        return temp
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.head.next is None:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length=self.length-1
        return temp
    
    def get(self,index):
        if index<0 or self.length<=index:
            return None
        temp=self.head
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.val=value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or self.length<=index:
            return None
        new_node=Node(value)
        temp=self.get(index)
        if temp:
            new_node.next=temp.next
            new_node.prev=temp
            temp.next.prev=new_node
            return True
        return False
    
linked_list=DoublyLinkedList(1)

linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.insert(3,56)

linked_list.pop()
print(linked_list.get(3).val)

        
    
        