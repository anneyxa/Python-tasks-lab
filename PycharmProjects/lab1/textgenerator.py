import nltk


# nltk.download('punkt')
class TextParser:

    @staticmethod
    def get_tokens_txt(path):
        try:
            with open(path, "r+") as txt_file:
                for line in txt_file:
                    for word in line.split():
                        for token in nltk.word_tokenize(word):
                            yield token
        finally:
            txt_file.close()

    @staticmethod
    def get_sentences_txt(path):
        try:
            with open(path, "r+") as txt_file:
                text = txt_file.read()
                for sentence in nltk.sent_tokenize(text):
                    yield sentence
        finally:
            txt_file.close()

    @staticmethod
    def get_tokens_conll(path):
        try:
            with open(path, "r+") as conll_file:
                for line in conll_file:
                    token = line.split()[0][1:-1]
                    yield token
        finally:
            conll_file.close()

    @staticmethod
    def get_sentences_conll(path):
        tokens = []
        try:
            with open(path, "r+") as conll_file:
                for line in conll_file:
                    token = line.split()[0][1:-1]
                    if token not in ('.', '?', '!'):  # dopoki zdanie sie nie konczy ktoryms z tych znakow,
                        tokens.append(token)          # dodawaj tokeny
                    else:
                        sentence = ' '.join(tokens)
                        yield sentence
                        tokens = []  # 'zrestartuj' tablice tokenow
                yield ' '.join(tokens)
        finally:
            conll_file.close()
