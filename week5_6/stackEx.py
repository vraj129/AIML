from collections import deque


class Stack: 
    def __init__(self):
        self.container = deque()
    
    def push(self,value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()
    
    def peep(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def reverseString(self,value):
        for char in value:
            self.push(char)
        str = ""
        for char in reversed(self.container):
            str += char
        return str

def balanceString(value):
    s = Stack()
    for c in value:
        if(c == "(" or c == "{" or c =="["):
            s.push(c)
        if( c ==")" or c == "}" or c == "]"):
            if(s.size() == 0):
                return False
            if not matchBracket(c,s.pop()):
                return False
    return s.size() == 0

def matchBracket(ch1,ch2):
    match = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    return match[ch1] == ch2
 
if __name__ == "__main__":
    s = Stack()
    print(s.reverseString("We will conquere COVID-19"))
    print(balanceString("({a+b})"))
    print(balanceString("))((a+b}{"))
    print(balanceString("((a+b))"))
    print(balanceString("((a+g))"))
    print(balanceString("))"))
    print(balanceString("[a+b]*(x+2y)*{gg+kk}"))