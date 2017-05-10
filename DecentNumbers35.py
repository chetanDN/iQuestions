"""
A Decent Number has the following properties:
Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
"""
num = int(input())

tCount=fCount=0
s=""

if num%3 ==0 :
    tCount = num//3
    for _ in range(tCount):
        s+="555"
elif num%5 ==0:
    fCount = num//5
    for _ in range(fCount):
        s+="33333"

print(s);

"""
Output
3333333333
Input
10
"""
