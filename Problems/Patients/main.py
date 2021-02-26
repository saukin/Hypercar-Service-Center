class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self):
        return f'Object of the class Patient. ' \
               f'name: {self.name}, last_name: {self.last_name}, age: {self.age}'

    def __str__(self):
        return f'{self.name} {self.last_name}. {self.age}'

# m = Patient('Mary', 'Watson', 33)
#
# print(m.__repr__())
# print(m.__str__())
