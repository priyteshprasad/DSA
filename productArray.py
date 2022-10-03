
from cgitb import reset


arr = [1,2,3,4,5]
print(arr)

def productArray (arr=[]):
    '''
    this is a document
    '''
    result = [1,1,1,1,1]
    for i in range(len(arr)):
        element = 1
        for j in range(len(arr)):
            
            if j != i:
                element = element * arr[j]
            result[i] = element
    return result

print(productArray.__doc__)