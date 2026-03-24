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
        if id is not (None or ''):
            self.id = id
        if nick_name is not (None or ''):
            self.nick_name = nick_name
        if first_name is not (None or ''):
            self.first_name = first_name
        if last_name is not (None or ''):
            self.last_name = last_name
        if middle_name is not (None or ''):
            self.middle_name = middle_name
        if gender is not (None or ''):
            self.gender = gender

    def __str__(self):
        ret_str = f'ID: {self.id} LOGIN: {self.nick_name} NAME: {self.first_name} '
        if self.middle_name:
            ret_str += f'{self.middle_name} '
        if self.last_name:
            ret_str += f'{self.last_name} '
        if self.gender:
            ret_str += f'GENDER: {self.gender}'
        return ret_str

    def __repr__(self):
        return self.nick_name


class Game:
    def __init__(self, team_dict):
        self.team_1 = team_dict['command1']
        self.team_2 = team_dict['command2']
        self.score_1 = 0
        self.score_2 = 0

    def ball_thrown(self, command, points):
        if command == 1:
            self.score_1 += points
        if command == 2:
            self.score_2 += points

    def get_score(self):
        return (self.score_1, self.score_2)

    def get_winner(self):
        if self.score_1 > self.score_2:
            return self.team_1
        if self.score_2 > self.score_1:
            return self.team_2
        return 'Ничья'


class Point:
    def __init__(self, place=(0, 0)):
        self.x = place[0]
        self.y = place[1]

    def __str__(self):
        return str((self.x, self.y))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        '''Вычисляет расстояние между текущей точкой и другой точкой.'''
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5  # возведение в степень 0.5 = квадратный корень

    def sum(self, other):
        '''Возвращает новую точку с координатами, равными сумме координат.'''
        return Point((self.x + other.x, self.y + other.y))


class TrafficLight:
    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']  # атрибут класса

    def __init__(self):
        self.sig_is = 0  # индекс текущего сигнала (начинаем с зеленого)

    def next_signal(self):
        '''Переключает светофор на следующий сигнал'''
        self.sig_is = (self.sig_is + 1) % len(self.permissible_values)

    @property
    def current_signal(self):
        '''Возвращает текущий сигнал светофора'''
        return self.permissible_values[self.sig_is]


class MorseMsg:
    # Словарь для декодирования в латиницу
    MORSE_TO_ENG = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
    }

    # Словарь для декодирования в кириллицу
    MORSE_TO_RU = {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
        '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
        '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
        '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
        '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
        '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '...-...': 'Э',
        '..--': 'Ю', '.-.-': 'Я',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
    }

    ENG_VOWELS_LIST = ['A', 'E', 'I', 'O', 'U', 'Y']
    ENG_CONSONANTS_LIST = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                           'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    RUS_VOWELS_LIST = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
    RUS_CONSONANTS_LIST = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М',
                           'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']

    def __init__(self, encoded_msg):
        '''
        Инициализация экземпляра класса закодированным сообщением.
        Буквы разделяются пробелом.
        '''
        self.encoded_msg = encoded_msg

    def eng_decode(self):
        '''
        Декодирует сообщение в латинские буквы.
        Возвращает строку с декодированным сообщением.
        '''
        words = self.encoded_msg.split(' ')  # Слова разделены пробелами
        decoded_words = ''

        for word in words:
            letters = word.split(' ')  # Буквы разделены одним пробелом
            decoded_word = ''
            for letter in letters:
                if letter in self.MORSE_TO_ENG:
                    decoded_word += self.MORSE_TO_ENG[letter]
            decoded_words += decoded_word

        return decoded_words

    def ru_decode(self):
        '''
        Декодирует сообщение в кириллицу.
        Возвращает строку с декодированным сообщением.
        '''
        words = self.encoded_msg.split(' ')  # Слова разделены пробелами
        decoded_words = ''

        for word in words:
            letters = word.split(' ')  # Буквы разделены одним пробелом
            decoded_word = ''
            for letter in letters:
                if letter in self.MORSE_TO_RU:
                    decoded_word += self.MORSE_TO_RU[letter]
            decoded_words += decoded_word

        return decoded_words


    def get_vowels(self, lang):
        vowels_lst = []
        match lang:
            case 'ru':
                word = self.ru_decode()
                for letter in word:
                    if letter in self.RUS_VOWELS_LIST:
                        vowels_lst.append(letter)
            case 'eng':
                word = self.eng_decode()
                for letter in word:
                    if letter in self.ENG_VOWELS_LIST:
                        vowels_lst.append(letter)
        return vowels_lst

    def get_consonants(self, lang):
        consonants_lst = []
        match lang:
            case 'ru':
                word = self.ru_decode()
                for letter in word:
                    if letter in self.RUS_CONSONANTS_LIST:
                        consonants_lst.append(letter)
            case 'eng':
                word = self.eng_decode()
                for letter in word:
                    if letter in self.ENG_CONSONANTS_LIST:
                        consonants_lst.append(letter)
        return consonants_lst



    def __str__(self):
        '''
        Возвращает строковое представление объекта с автоматическим определением языка.
        Определяет язык по первому декодированному слову.
        '''
        return self.encoded_msg

    def __repr__(self):
        '''
        Возвращает представление объекта для отладки.
        '''
        return self.encoded_msg


class StrandsDNA:
    def __init__(self):
        self.all_strands = []


    def add_strands(self, strands):
        self.all_strands += strands.split()
        self.all_strands = list(set(self.all_strands))
        self.all_strands.sort(key=lambda x: x)


    def __str__(self):
        return str(' '.join(self.all_strands))


    def get_max_strands(self):
        max_len = max([len(x) for x in self.all_strands])
        max_len_chain = []
        for chain in self.all_strands:
            if len(chain) == max_len:
                max_len_chain.append(chain)
        return str(' '.join(max_len_chain))