# Import spaCy and load the language library
import spacy

import contraction_removal

# load small version of english library
nlp = spacy.load('en_core_web_sm')


class sentence_segmentation:
    contraction_removal_obj = contraction_removal.contraction_removal()

    def __init__(self):
        pass

    def sent_segment(self):
        with open('sample.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
            doc = nlp(data)
            for sent in doc.sents:
                self.contraction_removal_obj.expand_contractions(str(sent))


