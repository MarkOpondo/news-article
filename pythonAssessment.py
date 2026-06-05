import re
from pathlib import Path

article = Path("NewsArticleforPythonAssessment.txt").read_text(encoding="utf-8")

print(article)

def count_specific_word():
    None