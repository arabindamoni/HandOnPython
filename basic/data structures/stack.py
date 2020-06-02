class mystack:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*self.size    # [None,None,None,..,None]    
        self.pos = 0
        return
    
    ### arr= [0,1,2], arr = [5,1,2], arr[0] = 5     

    # return True if val is pushed else return False
    def push(self, val):
        if self.pos < self.size:
            self.arr[self.pos] = val
            self.pos += 1    
            return True    
        return False
    
    # remove and return value of most recently pushed element
    # return None if stack is empty
    def pop(self):
        # print(self.arr[self.pos - 1])
        if self.pos > 0:
            self.pos -= 1
            return self.arr[self.pos]
        return None



stack = mystack(5)

# case 1: empty stack 
print(stack.pop())

for el in [1,2,3,4,5,6,7]:
    print(stack.push(el))

for i in range(10):
    print(stack.pop())