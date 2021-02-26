# the list "meals" is already defined
amount = 0
for _list in meals:
    amount += _list.get('kcal')

print(amount)
