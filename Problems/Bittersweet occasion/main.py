# finish the function
def find_the_parent(child):
    for t in [Drinks, Pastry, Sweets]:
        if issubclass(child, t):
            print(t.__name__)
