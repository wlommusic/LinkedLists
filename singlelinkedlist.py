class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self,):
        self.head= None
  
    def insert_at_begining(self,data):                            #insert at the top
        node = Node(data,self.head)
        self.head=node
   
    def insert_at_end(self,data):                                 #insert at the end 
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next=Node( data,None)    
    
    def create_list(self,data_list):                            #create a new list by values
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):                                       #get lenght of linked list
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
   
    def insert_at(self,index,data):                             #insert at index
       if index<0 or index>=self.get_length():
            print("Invalid Index")
       if index==0:
           self.insert_at_begining(data)
           return
       count=0
       itr=self.head
       while itr:
           if count==index-1:
               node=Node(data,itr.next)
               itr.next=node
               break
           itr=itr.next
           count+=1
       
    def remove_at(self, index):                                # remove at index
        if index<0 or index>=self.get_length():
            print("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
    
    
    def insert_after_value(self,data_after,data_to_insert):    #insert data by value
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return       
        
        itr=self.head 
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next
        
    def remove_by_value(self,data):                            #remove data by value
         if self.head is None:
            return

         if self.head.data == data:
            self.head = self.head.next
            return
         
         itr = self.head
         while itr.next:
             if itr.next.data == data:
                itr.next = itr.next.next
                break

             itr = itr.next
             
    
    
    def print(self):                                             #display linkedlist  
        if self.head is  None:
            print("linked list is empty")
            return
        
        itr=self.head
        list=''
        while itr :
            list+=str(itr.data)+'--> ' if itr.next else str(itr.data)
            itr = itr.next
        print(list)
        
        
        


ll=linkedlist()
ll.create_list([1,2,3,4,5,6,7,8])
print('lenght;',ll.get_length()) 
ll.print()
ll.remove_at(7)    
ll.remove_at(70)        
ll.print()  
ll.insert_at(3,69)
print('lenght;',ll.get_length())
ll.insert_after_value(69,70)
ll.remove_by_value(7)
print('lenght;',ll.get_length())
ll.print()   
