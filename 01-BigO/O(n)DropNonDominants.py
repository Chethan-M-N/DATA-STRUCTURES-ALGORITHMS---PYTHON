# BigO = Drop Non-Dominants
# Nested for loop   = n^2
# for loop          = n
# Sum of 2 for loop = O(n^2 + n), So in this equation, n^2 is the dominant term and that stand alone n is the non-dominant term. so just drop the n
# Final BigO        = O(n^2)

def printItems(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
            
    for k in range(n):
        print(k)
            
printItems(10)