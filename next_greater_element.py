# Python program to print next greater element using stack

# Stack Functions to be used by printNGE()
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

'''prints element and NGE pair for all elements of 
arr[] '''
def printNGE(arr):
    s = createStack()
    element = 0
    next = 0

    # push the first element to stack
    push(s, arr[0])

    # iterate for rest of the elements
    for i in range(1, len(arr)):
        next=arr[i]
        if isEmpty(s) == False:
            element=pop(s)
            while next>element:
                print(str(element)+"--> "+str(next))
                if isEmpty(s) == True:
                    break
                element=pop(s)
            if element>next:
                push(s,element)
        push(s, next)
    while isEmpty(s) == False:
        element = pop(s)
        next = -1
        print(str(element) + "--> " + str(next))
arr = [11, 13, 21, 3]
printNGE(arr)