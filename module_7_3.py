class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for i in args:
            self.file_names.append(i)

    def __str__(self):
        return self
    def get_all_words(self):

        get_all_words_ = {}

        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding='utf-8') as file:
                file_ = file.read().lower()
                dots_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for j in dots_:
                    file_ = file_.replace(j, ' ')
                file_ = file_.split()
            get_all_words_[self.file_names[i]] = file_
        return get_all_words_

    def find(self, word):
        dict_with_word = {}
        items_ = self.get_all_words().items()
        word = word.lower()
        for i in items_:
            if word in i[1]:
                dict_with_word[i[0]] = i[1].index(word) + 1 # Какое по счету слово
        return dict_with_word

    def count(self, word):
        dict_with_word_1 = {}
        items_ = self.get_all_words().items()
        word = word.lower()
        for i in items_:
            if word in i[1]:
                dict_with_word_1[i[0]] = i[1].count(word)
        return dict_with_word_1


