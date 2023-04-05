# Big O : O(n) 
# O(n) -> Is always Propotional & also Strigth line
# first for loop  = n
# Second for loop = n
# together        = n + n = 2n (drop constant value 2) then it will be O(n)

def printItem(n):
    for i in range(n):
        print(i)
        
    for j in range(n):
        print(j)
        
printItem(10)