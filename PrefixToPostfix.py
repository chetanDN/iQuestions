"""
preFix to postFix conversion

No need to check operator precedence or check for ( or ) operator as prefix itself is consolidated expn.

logic:
1.Scan each character of the input from right to left.

2.If the character is operand then push it onto the stack.

3.If the character if an operator, then pop two operands from stack and concatenate them as (TOS, TOS-1, operator).

4.Push this result onto the stack.

#5.After parsing the complete input, if still any elements exit in the stack, pop them out and concatenate.

courtesy : http://qa.geeksforgeeks.org/6252/it-possible-convert-prefix-expression-postfix-expression
"""


prefixExp = list(input())

postfixStk = [] #using list as stack

for ele in prefixExp[::-1]: #iterate list backwards
    s = "" #temp string
    
    if ele in "+-*/":
        s = "".join(postfixStk.pop()+postfixStk.pop()+ele)  #logic if operator o/p-> {tos,(tos-1),operator}
        postfixStk.append(s)
    else:
        postfixStk.append(ele) #if not operator add that operand to top of stack

print("".join(postfixStk))
