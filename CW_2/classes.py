from typing import List


class BasicWord:
    def __init__(self, word: str, subwords: List):
        self.word = word
        self.subwords = subwords

    def total_words(self):
        return len(self.subwords)

    def is_in_subwords(self, word: str):
        return word in self.subwords

    def __repr__(self):
        return self.word


class PLayer:
    def __init__(self, name):
        self.name = name
        self.words = []

    def total_answer(self):
        return len(self.words)

    def add_word(self, word):
        self.words.append(word)

    def is_word_used(self, word):
        return word in self.words

    def __repr__(self):
        return self.name
