class Dog:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('Гав!')

    def __str__(self):
        return self.name


class NotSleeping:
    def __init__(self, name, sheep=0):
        self.name = name
        self.sheep = sheep


    def add_sheep(self):
        self.sheep += 1

    def lost(self):
        self.sheep = 0


    @property
    def count_sheeps(self):
        return self.sheep


class User:
    '''
    обязательными параметрами являются:
    id - уникальный номер пользователя;
    nick_name - псевдоним пользователя;
    first_name - имя пользователя.

    Необязательными параметрами являются:
    last_name - фамилия;
    middle_name - отчество;
    gender - пол.
    '''

    def __init__(self, id, nick_name, first_name,
                 last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, id=None, nick_name=None, first_name=None, last_name=None,
               middle_name=None, gender=None):
        if id is not None:
            self.id = id
        if nick_name is not None:
            self.nick_name = nick_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        if gender is not None:
            self.gender = gender

    def __str__(self):
        return f'ID: {self.id} LOGIN: {self.nick_name} NAME: {self.first_name} {self.middle_name} {self.last_name}'

