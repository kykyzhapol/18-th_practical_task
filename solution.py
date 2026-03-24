'''
Module containing several classes for various tasks:
- Dog: simple dog class
- NotSleeping: counts sheep to fall asleep
- User: user data management
- Game: team game score tracking
- Point: 2D point with operations
- TrafficLight: traffic light state machine
- MorseMsg: Morse code decoding with vowel/consonant extraction
- StrandsDNA: managing DNA strands
- Segment: line segment between two points, with axis intersection detection
- CoordinateSystem: collection of segments and analysis
'''


class Dog:
    '''A simple dog class.'''

    def __init__(self, name):
        '''Initialize a dog with a name.'''
        self.name = name

    def say(self):
        '''Make the dog bark.'''
        print('Гав!')

    def __str__(self):
        '''Return the dog's name as string representation.'''
        return self.name


class NotSleeping:
    '''Counts sheep to help falling asleep.'''

    def __init__(self, name, sheep=0):
        '''
        Initialize a not-sleeping person.

        Args:
            name: The person's name.
            sheep: Initial number of sheep counted (default 0).
        '''
        self.name = name
        self.sheep = sheep

    def add_sheep(self):
        '''Increment the sheep count by one.'''
        self.sheep += 1

    def lost(self):
        '''Reset the sheep count to zero.'''
        self.sheep = 0

    @property
    def count_sheeps(self):
        '''Return the current number of counted sheep.'''
        return self.sheep


class User:
    '''
    User information container.

    Attributes:
        id: Unique user identifier.
        nick_name: User nickname.
        first_name: User first name.
        last_name: User last name (optional).
        middle_name: User middle name (optional).
        gender: User gender (optional).
    '''

    def __init__(self, id, nick_name, first_name,
                 last_name=None, middle_name=None, gender=None):
        '''
        Initialize a user.

        Args:
            id: Unique user identifier.
            nick_name: User nickname.
            first_name: User first name.
            last_name: User last name (optional).
            middle_name: User middle name (optional).
            gender: User gender (optional).
        '''
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, id=None, nick_name=None, first_name=None, last_name=None,
               middle_name=None, gender=None):
        '''
        Update user attributes.

        Only attributes that are provided (not None and not empty string) are updated.

        Args:
            id: New user ID.
            nick_name: New nickname.
            first_name: New first name.
            last_name: New last name.
            middle_name: New middle name.
            gender: New gender.
        '''
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
        '''
        Return a formatted string representation of the user.

        Includes ID, nickname, first name, and optional middle name, last name, and gender.
        '''
        ret_str = f'ID: {self.id} LOGIN: {self.nick_name} NAME: {self.first_name} '
        if self.middle_name:
            ret_str += f'{self.middle_name} '
        if self.last_name:
            ret_str += f'{self.last_name} '
        if self.gender:
            ret_str += f'GENDER: {self.gender}'
        return ret_str

    def __repr__(self):
        '''Return the user nickname as representation.'''
        return self.nick_name


class Game:
    '''Tracks scores for a two-team game.'''

    def __init__(self, team_dict):
        '''
        Initialize the game with two teams.

        Args:
            team_dict: Dictionary with keys 'command1' and 'command2' containing team names.
        '''
        self.team_1 = team_dict['command1']
        self.team_2 = team_dict['command2']
        self.score_1 = 0
        self.score_2 = 0

    def ball_thrown(self, command, points):
        '''
        Add points to a team.

        Args:
            command: Team identifier (1 or 2).
            points: Points to add.
        '''
        if command == 1:
            self.score_1 += points
        if command == 2:
            self.score_2 += points

    def get_score(self):
        '''Return the current score as a tuple (team1_score, team2_score).'''
        return (self.score_1, self.score_2)

    def get_winner(self):
        '''
        Determine the winner.

        Returns:
            Name of the winning team or 'Ничья' (tie) if scores are equal.
        '''
        if self.score_1 > self.score_2:
            return self.team_1
        if self.score_2 > self.score_1:
            return self.team_2
        return 'Ничья'


class Point:
    '''A point in 2D space.'''

    def __init__(self, place=(0, 0)):
        '''
        Initialize a point.

        Args:
            place: Tuple (x, y) with coordinates, default (0,0).
        '''
        self.x = place[0]
        self.y = place[1]

    def __str__(self):
        '''Return string representation as (x, y).'''
        return str((self.x, self.y))

    def get_x(self):
        '''Return the x-coordinate.'''
        return self.x

    def get_y(self):
        '''Return the y-coordinate.'''
        return self.y

    def distance(self, other):
        '''
        Calculate the Euclidean distance to another point.

        Args:
            other: Another Point object.

        Returns:
            Float distance.
        '''
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def sum(self, other):
        '''
        Return a new point that is the sum of this point and another.

        Args:
            other: Another Point object.

        Returns:
            New Point with coordinates (self.x + other.x, self.y + other.y).
        '''
        return Point((self.x + other.x, self.y + other.y))


class TrafficLight:
    '''
    Traffic light with a cyclic sequence: green → yellow → red → yellow → green ...
    '''

    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']  # Class attribute

    def __init__(self):
        '''Initialize traffic light with green as starting signal.'''
        self.sig_is = 0  # index of current signal, starting at green (index 0)

    def next_signal(self):
        '''Switch to the next signal in the cycle.'''
        self.sig_is = (self.sig_is + 1) % len(self.permissible_values)

    @property
    def current_signal(self):
        '''Return the current signal as a string.'''
        return self.permissible_values[self.sig_is]


class MorseMsg:
    '''
    Morse code message decoder with vowel/consonant extraction for Russian and English.
    '''

    # Dictionary for decoding Morse to English
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

    # Dictionary for decoding Morse to Russian
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
    ENG_CONSONANTS_LIST = [
        'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
        'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z'
    ]
    RUS_VOWELS_LIST = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
    RUS_CONSONANTS_LIST = [
        'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М',
        'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ'
    ]

    def __init__(self, encoded_msg):
        '''
        Initialize with an encoded Morse message.

        Words are separated by spaces, letters within a word by a single space.

        Args:
            encoded_msg: String containing Morse code.
        '''
        self.encoded_msg = encoded_msg

    def eng_decode(self):
        '''
        Decode the message into English letters.

        Returns:
            String of decoded message in English.
        '''
        words = self.encoded_msg.split(' ')  # Words separated by spaces
        decoded_words = ''

        for word in words:
            letters = word.split(' ')  # Letters separated by one space
            decoded_word = ''
            for letter in letters:
                if letter in self.MORSE_TO_ENG:
                    decoded_word += self.MORSE_TO_ENG[letter]
            decoded_words += decoded_word

        return decoded_words

    def ru_decode(self):
        '''
        Decode the message into Russian Cyrillic.

        Returns:
            String of decoded message in Russian.
        '''
        words = self.encoded_msg.split(' ')  # Words separated by spaces
        decoded_words = ''

        for word in words:
            letters = word.split(' ')  # Letters separated by one space
            decoded_word = ''
            for letter in letters:
                if letter in self.MORSE_TO_RU:
                    decoded_word += self.MORSE_TO_RU[letter]
            decoded_words += decoded_word

        return decoded_words

    def get_vowels(self, lang):
        '''
        Extract vowels from the decoded message.

        Args:
            lang: Language to use ('ru' or 'eng').

        Returns:
            List of vowels found in the decoded message.
        '''
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
        '''
        Extract consonants from the decoded message.

        Args:
            lang: Language to use ('ru' or 'eng').

        Returns:
            List of consonants found in the decoded message.
        '''
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
        '''Return the original encoded message.'''
        return self.encoded_msg

    def __repr__(self):
        '''Return the original encoded message for debugging.'''
        return self.encoded_msg


class StrandsDNA:
    '''Manage a collection of unique DNA strand strings.'''

    def __init__(self):
        '''Initialize with an empty list of strands.'''
        self.all_strands = []

    def add_strands(self, strands):
        '''
        Add strands to the collection, keeping only unique strings.

        Args:
            strands: Space-separated string of DNA strands.
        '''
        self.all_strands += strands.split()
        self.all_strands = list(set(self.all_strands))
        self.all_strands.sort(key=lambda x: x)

    def __str__(self):
        '''Return the sorted unique strands as a space-separated string.'''
        return ' '.join(self.all_strands)

    def get_max_strands(self):
        '''
        Return the longest strands (if multiple have the same length).

        Returns:
            Space-separated string of the longest strands.
        '''
        max_len = max([len(x) for x in self.all_strands]) if self.all_strands else 0
        max_len_chain = []
        for chain in self.all_strands:
            if len(chain) == max_len:
                max_len_chain.append(chain)
        return ' '.join(max_len_chain)


class Segment:
    '''A line segment defined by two points, with axis intersection detection.'''

    def __init__(self, point1, point2):
        '''
        Initialize a segment with two points.

        Args:
            point1: First Point object.
            point2: Second Point object.
        '''
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = self._check_one_axis_intersection()

    def _check_one_axis_intersection(self):
        '''
        Determine if the segment crosses exactly one coordinate axis.

        Returns:
            True if the segment crosses exactly one axis (X or Y), False otherwise.
        '''
        x1, y1 = self.point1.get_x(), self.point1.get_y()
        x2, y2 = self.point2.get_x(), self.point2.get_y()

        crosses_x = self._crosses_axis_x(x1, y1, x2, y2)
        crosses_y = self._crosses_axis_y(x1, y1, x2, y2)

        # XOR: exactly one is true
        return crosses_x ^ crosses_y

    def _crosses_axis_x(self, x1, y1, x2, y2):
        '''
        Check if the segment crosses the X-axis (y=0).

        Args:
            x1, y1: Coordinates of first point.
            x2, y2: Coordinates of second point.

        Returns:
            True if the segment crosses the X-axis between the points.
        '''
        # If both y have the same sign, no crossing
        if y1 * y2 > 0:
            return False

        # If endpoint lies on axis, not counted as crossing
        if y1 == 0 or y2 == 0:
            return False

        # Check if intersection point lies between endpoints
        if y1 != y2:  # Avoid division by zero
            t = -y1 / (y2 - y1)  # Parameter where y = 0
            if 0 < t < 1:
                return True
        return False

    def _crosses_axis_y(self, x1, y1, x2, y2):
        '''
        Check if the segment crosses the Y-axis (x=0).

        Args:
            x1, y1: Coordinates of first point.
            x2, y2: Coordinates of second point.

        Returns:
            True if the segment crosses the Y-axis between the points.
        '''
        # If both x have the same sign, no crossing
        if x1 * x2 > 0:
            return False

        # If endpoint lies on axis, not counted as crossing
        if x1 == 0 or x2 == 0:
            return False

        # Check if intersection point lies between endpoints
        if x1 != x2:  # Avoid division by zero
            t = -x1 / (x2 - x1)  # Parameter where x = 0
            if 0 < t < 1:
                return True
        return False

    def __repr__(self):
        '''Return a string representation for debugging.'''
        return f'({self.point1}, {self.point2})'

    def __str__(self):
        '''Return a string representation of the segment.'''
        return f'({self.point1}, {self.point2})'


class CoordinateSystem:
    '''Collection of segments on a coordinate plane with axis intersection analysis.'''

    def __init__(self):
        '''Initialize an empty coordinate system.'''
        self.segments = []

    def add_segment(self, segment):
        '''
        Add a segment to the coordinate system.

        Args:
            segment: A Segment object.

        Raises:
            TypeError: If the argument is not a Segment instance.
        '''
        if isinstance(segment, Segment):
            self.segments.append(segment)
        else:
            raise TypeError('Argument must be an instance of Segment')

    def axis_intersection(self):
        '''
        Count segments that cross exactly one coordinate axis.

        Returns:
            Number of such segments.
        '''
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count

    def get_segments_with_one_intersection(self):
        '''
        Get a list of segments that cross exactly one axis.

        Returns:
            List of string representations of those segments.
        '''
        return [str(segment) for segment in self.segments if segment.one_intersection]

    def __str__(self):
        '''Return a summary string.'''
        return f'CoordinateSystem with {len(self.segments)} segments'