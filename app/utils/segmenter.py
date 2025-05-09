import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def split_segments(text: str, lang: str = "en") -> list[str]:
    return sent_tokenize(text.strip())
