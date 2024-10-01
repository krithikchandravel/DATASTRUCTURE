class BalancingofSymbol:

    def __init__(self,size):
        self.stack=[]
        self.size=size

    def checkexpression(self,expr):
        for char in expr:
            if char in "({[":
                self.push(char)
            elif char in ")}]":
                if not self.stack:
                    print("right is more than left")
                    return False
                else:
                    temp=self.pop()
                    if not self.match(temp,char):
                        print("mismatched paranthesis")
                        return False
        if not self.stack:
            return True
        else:
            print("left paranthesis is more than left")
            return False
    def push(self,char):
        if len(self.stack)==self.size:
            print("overflow")
        else:
            self.stack.append(char)
    def pop(char,self):
        if not self.stack:
            print("underflow")
        else:
            return self.stack.pop()

    def match(self,temp,char):
        if temp=="{" and char=="}":
            return True
        if temp=="(" and char==")":
            return True
        if temp=="[" and char=="]":
            return True
        
        return False




if __name__=="__main__":
    expr=input("enter expression:")
    size=int(input("enter the size:"))
    bs=BalancingofSymbol(size)
    valid=bs.checkexpression(expr)
    if valid:
        print("balance")
    else:
        print("unbalanced")
    
