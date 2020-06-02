class myqueue:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*self.size    
        self.left = 0
        self.right = 0
        return
    
    ### arr= [0,1,2], arr = [5,1,2], arr[0] = 5     

    # return True if val is pushed else return False
    def push(self, val): 
        if self.right < self.size:
            self.arr[self.right] = val
            self.right += 1
            return True         
        return False
    
    # remove and return value of least recently pushed element
    # return None if queue is empty
    def pop(self):
        if self.left < self.right:
            self.left += 1
            i = self.left
            if self.left == self.right:
                self.left = 0
                self.right = 0 
            return self.arr[i - 1] 
        return None



queue = myqueue(5)

print("#################\n")
# case 1: empty queue 
print(queue.pop())
print("###")
for el in [1,2,3,4,5,6,7]:
    print(queue.push(el))
print("###")
for i in range(10):
    print(queue.pop())
print("###")
for el in [1,2,3,4,5,6,7]:
    print(queue.push(el))