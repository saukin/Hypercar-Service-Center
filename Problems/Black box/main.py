# use the function blackbox(lst) that is already defined
lst = []
if id(lst) == id(blackbox(lst)):
    print('modifies')
else:
    print('new')
