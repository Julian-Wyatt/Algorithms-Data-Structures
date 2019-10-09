class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

#######  


def good_expression(Eq):
    
    depth = 0

    symbols = Stack()

    #assign starting bools
    
    goodPlusInsideBracket=None
    goodTimesBeforeBracket=None
    goodTimesAfterBracket=None
    tempCheckForPlusInBrackets=False

    prev=""

    for i in range (0,len(Eq)):
        tempCheckForPlusInBrackets=False

        ##Add all symbols to stack
        if Eq[i].isdigit()==False:
            symbols.push(Eq[i])


        if symbols.isEmpty() == False:
            
            if symbols.top()=="(":
                depth+=1


            #when it gets to a close bracket it works backwards towards the opening bracket
            elif symbols.top()==")":
                prev = symbols.pop()

                #if there are no expressions between the two brackets theyre redundant
                if symbols.top()=="(":
                    return False

                #while loops through undefined number of symbols between brackets
                while symbols.top() !="(":

                    #applies good plus in brackets rule - ie there has to be at least one plus in each bracket depth for them to be useful
                    #which is required as + has lower dominance over * in BIDMAS 
                    if symbols.top() == "+":
                        goodPlusInsideBracket = True
                        tempCheckForPlusInBrackets=True
                        
                    prev = symbols.pop()

                #pops the final open bracket
                prev = symbols.pop()

                #if the stack isnt empty it checks whether the operation before the open bracket is *.
                #Between brackets, either side of the bracket needs at least one multiply directly next to the bracket
                if (symbols.isEmpty()==False):
                    
                    if symbols.top()=="*":
                        goodTimesBeforeBracket = True
                    else:
                        goodTimesBeforeBracket = False

                #the temp check, checks whether the plus value was changed to true when checking through the last load of brackets
                # if it isnt then there wasnt a plus in that bracket and therefore its redundant
                if goodPlusInsideBracket != True or tempCheckForPlusInBrackets == False:
                    return False
                
                continue;
            
            #finally checks whether there is a times after the close bracket
            #prev is open bracket as stack looks through objects in reverse
            if prev=="(":
                if symbols.top()=="*":

                    goodTimesAfterBracket =True
                    prev=""
                    continue
                else:
                    goodTimesAfterBracket = False

    if depth == 0:
        return True
    if (goodTimesAfterBracket or goodTimesBeforeBracket) and goodPlusInsideBracket:
        return True



def test():
    assert good_expression("1+(2+3)*(4+5)")
    assert not good_expression("5*(3*2)*1")
    assert good_expression("2*3")
    assert not good_expression("((2+3)+2)")     
    assert not good_expression("6*(3*(2+3))")
    assert good_expression("(1+2)*3+4")        
    assert not good_expression('((2+3)*3)*6')                
    assert good_expression('1*(2+3)+4')  # Good expression
    assert not good_expression('1+(2+3)+4')  # Bad expression
    assert not good_expression('1+(2*3)+4')  # Bad expression
    assert not good_expression("1*2+(3+4)")  # Bad expression
    assert not good_expression('((1+2))*3+4')  # Bad expression
    assert not good_expression('(1+2+3+4)')  # Bad expression
    assert good_expression('1+2+3+4')  # Good expression
    assert not good_expression('((2+3)*3)*6')  # Bad expression
    assert good_expression('3+(4+5)*(6+7)')  # Good expression
    assert good_expression('3*(4+5)*(6+7)')  # Good expression
    assert not good_expression('3+(4+5)+(6+7)')  # Bad expression
    assert not good_expression('1*(2*3)*(4*5)')  # Bad expression
    assert not good_expression('(1+((2*3)*4)+5)+(6)*7*8+9)')  # Bad expression
    assert good_expression('1+2+(2+(4+2)*(4*4+2))*5')  # Good expression    
    assert not good_expression('(2)*2')  # Bad expression
    assert good_expression("1+2+3+4")  # Good expression
    assert not good_expression("(1+2+3+4)")  # Bad expression
    assert good_expression("(1+2)*3+4")  # Good expression     
    assert not good_expression("((1+2))*3+4")  # Bad expression
    assert good_expression("1+2*3+4")  # Good expression
    assert not good_expression("1+(2*3)+4")  # Bad expression
    assert good_expression("1*2+3+4")  # Good expression
    assert not good_expression("1*2+(3+4)")  # Bad expression
    assert not good_expression('1+(2*(3+(4*(5+(6*(7+(8*(9+(9+1)))))))))')  # Bad expression
    assert good_expression('1*(2+3)*(4+5)*(6+7)')  # Good expression
    assert not good_expression('1*(2*3)')  # Bad expression
    assert good_expression("1+2+3+4") 
    assert not good_expression("(1+2+3+4)") 
    assert good_expression("(1+2)*3+4") 
    assert not good_expression("((1+2))*3+4") 
    assert good_expression("1+2*3+4") 
    assert not good_expression("1+(2*3)+4") 
    assert good_expression("1*2+3+4") 
    assert not good_expression("1*2+(3+4)")
    assert not good_expression("6*(3*(2+3))")
    assert good_expression("(1+2*3*((4+5)*6+7)+8)*9")
    assert not good_expression("1+(2+3)+3")
    assert not good_expression("((2+3)+2)")

    print('All tests passed!!')



#test()
