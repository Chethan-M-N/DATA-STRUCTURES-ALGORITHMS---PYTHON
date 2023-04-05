# Big O : O(n^2) -> Line in the graph much steeper than O(n) it means lot less efficient from a time complexity standpoint
# Whenever nested for loop is present then it's O(n^2) = n * n * n ()

def printItems(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
            
printItems(10)