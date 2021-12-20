class MinStack:
    def __init__(self):
        self.arr=[]
        self.min=[]
    
    def push(self,val):
        #First push
        if(len(self.arr)==0):
            self.min.append(val)
            self.arr.append(val)
            return True
        #Update min on other than first push
        if(val<=self.min[-1]):
            self.min.append(val)
        self.arr.append(val)
        return True
    
    def pop(self):
        if (len(self.arr)==0):
            print("Stack Underflow")
            return -1
        #Otherwise pop val from min stack too, if matches
        if self.arr[-1]==self.min[-1]:
            self.min.pop()
        return self.arr.pop()
        
    def getmin(self):
        if len(self.min)!=0:
            return self.min[-1]
        else:
            print("Empty Stack with no min")
            return -1