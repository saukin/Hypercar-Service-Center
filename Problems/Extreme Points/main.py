# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
_min = ''
_max = ''

for x in test_dict.keys():
    if _max == '' and _min == '':
        _max = x
        _min = x
        continue
    if test_dict.get(x) > test_dict.get(_max):
        _max = x
    if test_dict.get(x) < test_dict.get(_min):
        _min = x

print(f"""min: {_min}
max: {_max}""")
