import re
from pathlib import Path
from collections import Counter

article = Path("NewsArticleforPythonAssessment.txt").read_text(encoding="utf-8")


def count_specific_word(target_word, article):
    all_words = re.findall(r"\b\w+\b", article.lower())
    word_count = Counter(all_words)
    target_count = word_count[target_word.lower()]

    if not target_count:
        print(0)
    else:
        print(target_count)
    

count_specific_word('you', article)