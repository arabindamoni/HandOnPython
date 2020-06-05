# Node -> {value, next_pointer}
# Node1 -> Node2 -> Node3

# 10, 15, 5, 20
# (10)->(15)->(5)->(20) ->   25

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    
    # append a new node with value = val
    def append(self, val):
        if self.head == None:
            new_node = ListNode(val)
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(val)        
         
    
    # print the linked list
    def printlist(self):
        print("\n")
        cur = self.head
        while cur is not None:
            print(cur.val,'->',end="")
            cur = cur.next
    
    # remove rightmost node
    # (10)->(15)->(5)->(20) 
    # (10)->(15)->(5)
    # i: (10)
    # o: None
    # i: None
    # o: None
    def pop(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            val2 = self.head.val
            self.head = None
            return val2
        else:
            cur = self.head
            while cur.next.next is not None:
                cur = cur.next
            val3 = cur.next.val
            cur.next = None
            return val3
    
    
    # remove leftmost node and assign new head
    # (10)->(15)->(5)->(20)
    # (15)->(5)->(20)
    # None
    # None
    def popleft(self):
        if self.head == None:
            return None
        else:
            val1 = self.head.val
            self.head = self.head.next            
            return val1
       
    
    # insert val at position node
    # i: (10)->(15)->(5)->(20) , insert(3,55)
    # o: (10)->(15)->(5)->(55)->(20)
    # i: (10)->(15)->(5)->(20) , insert(0,33)
    # o: (33)->(10)->(15)->(5)->(20)
    # i: (10)->(15)->(5)->(20) , insert(5,100)
    # o: (10)->(15)->(5)->(20)->(100)
    # assume inputs are valid
    def insert(self, position, val):
        if self.head == None:
            new_node = ListNode(val)
            self.head = new_node
        else:
            cur = self.head
            for i in range(position-1):# 0,1,2 
                cur = cur.next
            new_node = ListNode(val)
            new_node.next = cur.next
            cur.next = new_node
            # cur = 2
        return self.head
            


ll = LinkedList()
for el in [10,15,5,20]:
    ll.append(el)
ll.printlist()
ll.insert(3,55)
ll.printlist()

# print('popleft',ll.popleft())
# ll.printlist()       

# for i in range(5):
#     print('pop',ll.pop())
#     ll.printlist()



# 10 ->15 ->5 ->20 ->

# 15 ->5 ->20 ->     

# 15 ->5 ->


# 15 ->

