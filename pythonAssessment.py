import re
from pathlib import Path
from collections import Counter

article = Path("NewsArticleforPythonAssessment.txt").read_text(encoding="utf-8")


def count_specific_word(article, target_word):
    all_words = re.findall(r"\b\w+\b", article.lower())
    word_count = Counter(all_words)
    
    target_count = word_count[target_word.lower()]

    if not target_count:
        print(0)
    else:
        print(target_count)
    

def identify_most_common_word(article):
    all_words = re.findall(r"\b\w+\b", article.lower())
    word_count = Counter(all_words)
    
    most_common_word, frequency = word_count.most_common(1)[0]

    if not most_common_word:
        None
    else:
        print(most_common_word, frequency)


def calculate_average_word_length(article):
    all_words = re.findall(r"\b\w+\b", article.lower())
    
    if not all_words:
        print(0)
    else:
        total_words = len(all_words)
        total_letters = 0
        for word in all_words:
            total_letters += len(word)
            

        average_word_length = total_letters / total_words

        if not average_word_length:
            print(0)
        else:
            print(average_word_length)


def count_paragraphs(article):
    paragraphs = re.split(r"\n\n", article)
    paragraph_count = len([p.strip() for p in paragraphs if p.strip()])
    
    if not paragraph_count:
        print(1)
    else:
        print(paragraph_count)


def count_sentences(article):
    sentences = re.findall(r"(?<=[.!?])+", article)

    while sentences:

        total_sentences = len(sentences)
    
    if not total_sentences:
        print(1)
    else: 
        print(total_sentences)

count_specific_word("This is a test. This is only a test.", "test")
count_specific_word("apple apple banana banana banana", "banana")
count_specific_word("", "test")
# identify_most_common_word(article)
# calculate_average_word_length(article)
# count_paragraphs(article)
# count_sentences(article)