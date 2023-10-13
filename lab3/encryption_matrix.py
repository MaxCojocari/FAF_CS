from alphabet import alphabet

ROWS, COLUMNS = 6, 5

class EncryptionMatrix:
    def __init__(self, key: str):
        self.key = key
        self.alphabet = alphabet
        self.matrix = [['' for _ in range(COLUMNS)] for _ in range(ROWS)]
    
    def normalize_key(self):
        s = self.key.upper()
        result = ""
        seen = set()

        for char in s:
            if char not in seen and char.isalpha():
                result += char
                seen.add(char)

        self.key = result
    
    def construct_matrix(self):
        i, j = 0, 0
        visited = {char: False for char in alphabet}

        for char in self.key:
            if j == COLUMNS:
                j = 0
                i += 1
            self.matrix[i][j] = char
            visited[char] = True
            j += 1
        
        k, m = i, j
 
        for char in visited.keys():
            if not visited[char]:
                if m == COLUMNS and k < ROWS:
                    m = 0
                    k += 1
                self.matrix[k][m] = char
                visited[char] = True
                m += 1
    
    def get_location(self, char):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if char == self.matrix[i][j]:
                    return i, j
        return 0, 0
    
    def get_matrix(self):
        self.normalize_key()
        self.construct_matrix()
        return self.matrix