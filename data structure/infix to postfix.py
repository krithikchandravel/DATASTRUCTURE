class Intopfix:
    def __init__(self):
        self.stack = []

    def push(self,char):
        self.stack.append(char)

    def pop(self):
        return self.stack.pop() 
    
    def priority(self,char):
        if char == "^":
            return 3
        elif char == "*" or char == "/":
            return 2
        elif char ==  "+" or char == "-":
            return 1
        else:
            return 0
        
def intopo(expr):
    postfix = []     
    s = Intopfix()
    for char in expr:
        if char == "(":
            s.push(char)   
        elif char.isalnum():
            postfix.append(char) 
        elif char == ")":
            x = s.pop()
            while(x != "("):
                postfix.append(x)
                x = s.pop()      
        else:
            while s.stack and s.priority(char)<=s.priority(s.stack[-1]):
                postfix.append(s.pop())
            s.push(char)
    
    while s.stack:
        x = s.pop()
        postfix.append(x)

    return ''.join(postfix)

if __name__ == "__main__":
    expr = input("Enter the expression :")
    result = intopo(expr)
    print(result)
