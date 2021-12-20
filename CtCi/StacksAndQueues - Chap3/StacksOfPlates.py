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
    
    def popAt(self,idx):
        if idx==len(self.parent):
            if len(self.child)>0:
                return self.child.pop()
            else:
                print("Substack at idx ",idx," is empty!")
                return -1
        elif idx < len(self.parent):
            d=self.parent[idx].pop()
            #If current child stack is partially filled pass it on
            if len(self.child)>0:
                shift_stack=self.parent + [self.child]
                temp=self.shiftLeft(shift_stack,idx)
                self.child=temp.pop()
                self.parent=temp
            #Otherwise dont pass it along with parent stack for left shift
            elif len(self.child==0):
                shift_stack=self.parent
                self.parent=self.shiftLeft(shift_stack,idx)
                if len(self.parent[-1]<self.thresh):
                    #If after shifting final stack has space make it current stack
                    self.child=self.parent.pop()
            return d
    
    #Function to shift all sub stacks in parent to be filled to full capacity
    def shiftLeft(self,stack,idx):
        for i in range(idx,len(stack)):
            if i!=len(stack)-1:
                stack[i].append(stack[i+1].pop(0))
        return stack

