def create_stack():
    stck = []
    return stck

def is_empty(stck):
    return len(stck) == 0

def push(stck, ele):
    stck.append(ele)
    print("Pushed item into stack")

def pop(stck):
    if is_empty(stck):
        return "Stack underflow"
    return stck.pop()

stack = create_stack()
x = pop(stack)
print("Pop result : ",x)
push(stack, 1)
push(stack, 5)
push(stack, 19)
ele = pop(stack)
print("Popped element = ",ele)
print("Stack after popping : ", stack)
