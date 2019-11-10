import re
import nltk
# to install contractions - pip install contractions
from contractions import contractions_dict
import word_filteration

class contraction_removal:
    word_filteration_obj = word_filteration.word_filteration()

    def __init__(self):
        pass

    def expand_contractions(self, text):

        contractions_pattern = re.compile('({})'.format('|'.join(contractions_dict.keys())))

        def expand_match(contraction):

            # print(contraction)
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contractions_dict.get(match) \
                if contractions_dict.get(match) \
                else contractions_dict.get(match.lower())
            expanded_contraction = expanded_contraction
            # print(expanded_contraction)
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, text)
        print(expanded_text)
        self.word_filteration_obj.remove_stopwords(text)
        # self.tokenize_sentence(expanded_text)


    def tokenize_sentence(self,text):
        sentence = nltk.sent_tokenize(text)
        tokenized_sentences = [nltk.word_tokenize(sentences) for sentences in sentence]
        print(tokenized_sentences)