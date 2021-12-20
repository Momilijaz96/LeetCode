import numpy as np

class ThreeStacks:
    def __init__(self,size=1000):
        self.arr = np.ones(shape=(size,1))*-1
        self.s1len = size//3
        self.s2len = 2*self.s1len
        self.s3len = (3*self.s1len) + 1
        self.s1idx = 0
        self.s2idx = self.s1len
        self.s3idx = self.s2len
    
    def push1(self,val):
        if (self.s1idx<self.s1len):
            self.arr[self.s1idx] = val
            self.s1idx+=1
            return True
        else:
            print("Stack 1 OverFlow!")
            return False

    def pop1(self):
        if (self.s1idx==0):
            print("Stack 1 Underflow!")
            return -1
        else:
            data=self.arr[self.s1idx]
            self.s1idx-=1
            self.arr[self.s1idx]=-1
            return data
    
    def push2(self,val):
        if (self.s2idx<self.s2len):
            self.arr[self.s2idx] = val
            self.s2idx+=1
            return True
        else:
            print("Stack 2 OverFlow!")
            return False

    def pop2(self):
        if (self.s2idx==self.s1len):
            print("Stack 2 Underflow!")
            return -1
        else:
            data=self.arr[self.s2idx]
            self.s2idx-=1
            self.arr[self.s2idx]=-1
            return data

    def push3(self,val):
        if (self.s3idx<self.s3len):
            self.arr[self.s3idx] = val
            self.s3idx+=1
            return True
        else:
            print("Stack 3 OverFlow!")
            return False

    def pop3(self):
        if (self.s3idx==self.s2len):
            print("Stack 3 Underflow!")
            return -1
        else:
            data=self.arr[self.s3idx]
            self.s3idx-=1
            self.arr[self.s3idx]=-1
            return data

if __name__=='__main__':
    stacks=ThreeStacks(50)
    stacks.push1(1)
    stacks.push2(2)
    stacks.push2(2)
    stacks.push3(3)
    stacks.push3(3)
    stacks.push3(3)
    print("AFTER PUSH: ",stacks.arr)
    stacks.pop1()
    stacks.pop2()
    stacks.pop3()
    print("AFTER POP: ",stacks.arr)

    
    