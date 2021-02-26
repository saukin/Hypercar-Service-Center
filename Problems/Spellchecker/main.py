dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

text = input().split()
flag = True
for x in text:
    if x not in dictionary:
        print(x)
        flag = False
if flag:
    print("OK")

