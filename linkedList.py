#Create a sperate class to create nodes and set next to be none
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

#Create a linked list class with head,tail and length. Also add new node with the create node class
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

#To print all the items in the linked list, start from the head(temp), c
#Check if its not none, print the value and assign temp to self.head.next(temp.next
    def print_itself(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node = Node(value)

        if self.length==0:
            self.head=new_node
            self.tail=new_node

        self.tail.next=new_node
        self.tail=new_node
        self.length+=1

    def pop(self):
        if self.length==0:
            return None;
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre=temp
                temp=temp.next
            pre.next=None
            self.tail=pre
            self.length=self.length-1
            return temp;
    def prepend(self, value):
        new_node = Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length=+self.length+1
        return True

    def pop_first(self):
        temp = self.head
        if self.length==1:
            self.head=None
            self.tail=None
        if self.length==0:
            return None
        else:
            self.head=temp.next
            temp.next=None
        self.length-=1
        return temp
    def get(self,index):
        if self.length<=0 or self.length<=index:
            return None
        temp = self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        new_node=Node(value)
        if index==0:
            return self.prepend(value)
        temp=self.get(index-1)
        if temp:
            new_node.next=temp.next
            temp.next=new_node
            self.length=self.length+1
            return True
        return False

    def remove(self,index):
        if self.length<=0 or self.length<=index:
            return None
        if index==0:
            self.pop_first()
        if index==self.length:
            self.pop()
        pre=self.get(index-1)
        temp =pre.next
        if pre and temp:
            pre.next=temp.next
            temp.next=None
            self.length-1
            return temp

    def reverse(self):
        temp = self.head
        self.head=self.tail
        self.tail=temp

        after =temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after





my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.insert(0,8)
my_linked_list.reverse()
my_linked_list.print_itself()

a= {1:"Erica",2:"James"}
b=a
b[1]="Cynthia"
print(a)


