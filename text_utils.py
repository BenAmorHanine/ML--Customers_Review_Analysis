import string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk
import pandas as pd

nltk.download('stopwords')

stop_words_fr = set(stopwords.words('french'))
stop_words_ar = set(['في', 'على', 'و', 'من', 'أن', 'إلى'])
stemmer = SnowballStemmer('french')

def process_review(text):
    """Nettoyage, suppression ponctuation, stopwords, stemming"""
    if(pd.isnull(text) or not isinstance(text, str) or len(text.strip()) == 0):
        return []
    # minuscules
    text = text.lower()
    # suppression ponctuation et chiffres
    text = ''.join([c for c in text if c not in string.punctuation and not c.isdigit()])
    # tokenisation et suppression stopwords
    tokens = [t for t in text.split() if t not in stop_words_fr and t not in stop_words_ar]
    # stemming
    tokens = [stemmer.stem(t) for t in tokens]
    return tokens
