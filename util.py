from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

class Util:

    def stem(self, word_to_stem: str):
        ps = PorterStemmer()
        return ps.stem(word_to_stem)
