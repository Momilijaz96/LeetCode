class SetOfStacks:
    def __init__(self,thresh=100):
        self.parent=[]
        self.child=[]
        self.thresh=thresh
    
    def push(self,val):
        if(len(self.child)<self.thresh):
            self.child.append(val)
            return True
        else:
            stack = self.child
            self.parent.append(stack)
            self.child= [val]
    
    def pop(self):
        if (0>len(self.child) and len(self.child)>=self.thresh):
            return self.child.pop()
        elif(len(self.child)==0 and len(self.parent)>0):
            self.child=self.parent.pop()
            return self.child.pop()
        elif(len(self.child)==0 and len(self.parent)==0):
            print("Stack Underflow!")
            return -1
