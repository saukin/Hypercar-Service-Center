def tallest_people(**people):
    _max = max(people.values())
    for man in sorted(people.keys()):
        if people[man] == _max:
            print(f'{man} : {_max}')
