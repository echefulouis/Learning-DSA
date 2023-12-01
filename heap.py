#Lets create helper methods first
class MaxHeap:
    def __init__(self):
        self.heap=[]
    def __left_child(self,index):
        return 2 * index + 1
    def __right_child(self,index):
        return 2 * index + 2
    def _parent(self,index):
        return (index-1)//2
    def swap(self,index1,index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2],self.heap[index1]
        
    def inser(self,value):
        self.heap.append(value)
        #Inititalize current as index of the newly added value in the list
        currrent = len(self.heap) - 1  
        
        while currrent>0 and (self.heap[current] > self.heap[self._parent(currrent)]):
            #Swap the two nodes if the child is greater than the parent
            self.swap(currrent,self._parent(currrent))
            #Make current the parents index , moving up
            currrent = self._parent(currrent)
            
    def remove(self):
        
         if len(self.heap) == 0:
             return None
         if len(self.heap) == 1:
             return self.heap.pop()
         
         max_value = self.heap[0]
         self.heap[0]= self.heap.pop()
         
         return max_value