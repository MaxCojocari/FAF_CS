import random
import string

class TextNormalizer:
    def __init__(self, text):
        self.text = text
        self.pairs = []

    def normalise(self):
        result_str = ''
        for char in self.text:
            if char == ' ':
                continue
            if char.isalpha():
                char = char.upper()
                if char == 'J':
                    char = 'I'
            result_str += char
        
        self.text = result_str

        return result_str

    def split_into_pairs(self):
        self.pairs = [self.text[i : i + 2] for i in range(0, len(self.text), 2)]

    def reshuffle_identical_letters(self):
        pairs = list(self.pairs)
        i = 0
        while i < len(pairs):
            if len(pairs[i]) > 1 and pairs[i][0] == pairs[i][1]:
                random_char = random.choice(['X', 'Q', 'Z'])
                pairs[i] = pairs[i][0] + random_char + pairs[i][1]
                word = ''.join(pairs)
                pairs = [word[i : i + 2] for i in range(0, len(word), 2)]
                i = 0
                continue
            i += 1

        self.pairs = pairs

    def augment(self):
        last_pair = self.pairs[len(self.pairs) - 1]
        if len(last_pair) == 1:
            random_char = last_pair[0]
            while last_pair[0] == random_char:
                random_char = random.choice(string.ascii_letters).capitalize()
            self.pairs[len(self.pairs) - 1] += random_char
    
    def get_standardized(self):
        self.normalise()
        self.split_into_pairs()
        self.reshuffle_identical_letters()
        self.augment()

        return self.pairs
