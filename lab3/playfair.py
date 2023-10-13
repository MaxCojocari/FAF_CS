from encryption_matrix import EncryptionMatrix
from text_normalizer import TextNormalizer

class Playfair:
    def __init__(self, key: str):
        self.key = key
        self.em = EncryptionMatrix(self.key)
        self.matrix = self.em.get_matrix()
        self.ROWS = len(self.matrix)
        self.COLUMNS = len(self.matrix[0])

    def encrypt(self, plaintext: str) -> str:
        normalizer = TextNormalizer(plaintext)
        pairs = normalizer.get_standardized()
        
        ciphertext = ''

        for pair in pairs:
            i0, j0 = self.em.get_location(pair[0])
            i1, j1 = self.em.get_location(pair[1])

            a, b = '', ''

            if i0 != i1 and j0 != j1:
                a, b = self.matrix[i0][j1], self.matrix[i1][j0]
            elif i0 == i1:
                a = self.matrix[i0][(j0 + 1) % self.COLUMNS]
                b = self.matrix[i1][(j1 + 1) % self.COLUMNS]
            elif j0 == j1:
                a = self.matrix[(i0 + 1) % self.ROWS][j0]
                b = self.matrix[(i1 + 1) % self.ROWS][j1]

            ciphertext += a + b
        
        return ciphertext


    def decrypt(self, ciphertext: str) -> str:
        normalizer = TextNormalizer(ciphertext)
        pairs = normalizer.get_standardized()
        
        plaintext = ''

        for pair in pairs:
            i0, j0 = self.em.get_location(pair[0])
            i1, j1 = self.em.get_location(pair[1])

            a, b = '', ''

            if i0 != i1 and j0 != j1:
                a, b = self.matrix[i0][j1], self.matrix[i1][j0]
            elif i0 == i1:
                a = self.matrix[i0][(j0 - 1) % self.COLUMNS]
                b = self.matrix[i1][(j1 - 1) % self.COLUMNS]
            elif j0 == j1:
                a = self.matrix[(i0 - 1) % self.ROWS][j0]
                b = self.matrix[(i1 - 1) % self.ROWS][j1]

            plaintext += a + b
        
        return plaintext
    
    def print_matrix(self):
        for row in self.matrix:
            print(' '.join(row))
