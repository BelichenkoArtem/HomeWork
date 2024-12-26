import string


class WordsFinder:
    def __init__(self, *args):
        self.topics = args

    def get_all_words(self):
        all_words = {}
        for topic in self.topics:
            with open(topic, 'r', encoding='utf-8') as file:
                words_in_file = []
                for line in file:
                    line = line.lower()
                    for char in string.punctuation + ' - ':
                        line = line.replace(char, ' ')
                    words = line.split()
                    words_in_file.extend(words)
                all_words[topic] = words_in_file
        return all_words

    def find(self, word):
        found_positions = {}
        all_words = self.get_all_words()
        for topic, words in all_words.items():
                index = words.index(word.lower())
                found_positions[topic] = index + 1
        return found_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()
        for topic, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                word_counts[topic] = count
        return word_counts














finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('Captain')) # 3 слово по счёту
print(finder2.count('Captain')) # 4 слова teXT в тексте всего