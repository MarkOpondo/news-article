import re
from collections import Counter

with open('NewsArticleforPythonAssessment.txt', 'r', encoding='utf-8') as file:
    article = file.read()


def count_specific_word(target_word, article):
    all_words = re.findall(r"\b\w+\b", article.lower())
    word_count = Counter(all_words)
    target_count = word_count[target_word.lower()]

    print(target_count)
    

count_specific_word('the', article)