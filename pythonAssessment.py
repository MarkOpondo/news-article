import re
from pathlib import Path
from collections import Counter

article = Path("NewsArticleforPythonAssessment.txt").read_text(encoding="utf-8")
if not article:
    None
else:
    all_words = re.findall(r"\b\w+\b", article.lower())
    word_count = Counter(all_words)


def count_specific_word(target_word, article):
    target_count = word_count[target_word.lower()]

    if not target_count:
        print(0)
    else:
        print(target_count)
    

def identify_most_common_word(article):
    most_common_word, frequency = word_count.most_common(1)[0]

    if not most_common_word:
        None
    else:
        print(most_common_word, frequency)


def calculate_average_word_length(article):
    total_words = len(all_words)
    total_letters = sum(len(word) for word in all_words)

    average_word_length = total_letters / total_words

    if not average_word_length:
        print(0)
    else:
        print(average_word_length)


# count_specific_word('you', article)
# identify_most_common_word(article)
calculate_average_word_length(article)