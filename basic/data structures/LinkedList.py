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
            self.head = None
            return None
        else:
            cur = self.head
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
            return self.head
    
    
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
       


ll = LinkedList()
for el in [10,15,5,20]:
    ll.append(el)
ll.printlist()

ll.popleft()
ll.printlist()       

for i in range(5):
    ll.pop()
    ll.printlist()

# 10 ->15 ->5 ->20 ->

# 15 ->5 ->20 ->     

# 15 ->5 ->


# 15 ->