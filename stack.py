class Stack(list): 
    def isEmpty(self):
        '''判断栈是否为空'''
        return self == []

    def top(self):
        '''返回栈顶'''
        return self[-1]
    
    def bottom(self):
        '''返回栈底'''
        return self[0]
    
    def size(self):
        '''返回栈的大小'''
        return len(self)
    
    def push(self, x):
        '''入栈'''
        self.append(x)

    def __repr__(self):
        l = self.size() * 7
        s = "|" + "-" * l + ")\n|"
        for a in self:
            s += "| %-5s" % a
        s += "\n|" + "-" * l + ")"
        return s
    __str__ = __repr__

'''st = Stack()
st.push(45)
st.push(56)
st.push(123)
st.push(999)
st.push("yes")
print(st)'''