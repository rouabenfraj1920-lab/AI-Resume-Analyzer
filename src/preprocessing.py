import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):

    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # Lemmatization
    doc = nlp(" ".join(tokens))

    lemmatized_tokens = [
        token.lemma_
        for token in doc
    ]

    return lemmatized_tokens