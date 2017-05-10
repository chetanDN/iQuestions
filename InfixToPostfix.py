"""
1)Create an empty stack called opstack for keeping operators. Create an empty list for output.
2)Convert the input infix string to a list by using the string method split if seperated by space.
3)Scan the token list from left to right.
    If the token is an operand, append it to the end of the output list.
    If the token is a left parenthesis, push it on the opstack.
    If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
    If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
4)When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.

http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html#lst-intopost
"""

print("Infix to PostFix Operation\n")

inputExpr = input("Enter the infix expression :")

#functions to be defined before called
def InfixToPostfix(inputExpr):
    #dictionary to store precedence value of operator
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    oprStack = [] # operator Stack  to store operator and  ')' & '(', or import Stack
    outList = []    #output list 
    
    ipExpList = list(inputExpr) # string expression to single char list
    for ele in ipExpList:       #  Step 3 scan from left to right
        if ele in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or ele in "abcdefghijklmnopqrstuvwxyz" or ele in "0123456789":
            outList.append(ele)
        elif ele == '(' :   
            oprStack.append(ele)    # if stack push(ele) operation
        elif ele == ')' :   #itterate and pop oprStack till you get (
            while oprStack[-1] != '(' : # oprStack[-1] is equivalent to peek() operation
                outList.append(oprStack.pop())
        else : #if you get other operators, push higher precedence opr or pop two operator , if lower precedence occured
            while (oprStack) and (prec[ele] <= prec[oprStack[-1]]):  #when stack is not empty then when ele precedence is < stack last element, pop stack last element and append ele to o/p list
                outList.append(oprStack.pop())
            oprStack.append(ele) #add compared, lower precedence "ele" also

    #after parsing input string, operators left in stack to be popped
    while oprStack:  #while stack is not empty === while( not oprStack.isEmpty()) is Stack used
        outList.append(oprStack.pop())
    
    return "".join(outList) # make list to string, joined by "" char
             
outputStrExpr = InfixToPostfix(inputExpr)  
print("\n Postfix Expression is : "+outputStrExpr);  

"""
Output
Infix to PostFix Operation

Enter the infix expression :
 Postfix Expression is : ABC*+D+
Input
A+B*C+D
"""
            
    
    
    
    
    
