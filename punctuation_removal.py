# not yet connected
import spacy
nlp = spacy.load('en_core_web_sm')
from string import punctuation


class punctuation_removal:

    def remove_punct(self, text):
        punct_removed = ''.join(c for c in text if c not in punctuation)
        print("--remove punctuations--")
        print(punct_removed)




