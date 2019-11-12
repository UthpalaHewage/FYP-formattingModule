import spacy
nlp = spacy.load('en_core_web_sm')
import nltk
from nltk import word_tokenize
# from nltk.corpus import stopwords
import punctuation_removal

class word_filteration:
    punctuation_removal_obj = punctuation_removal.punctuation_removal()


    def __init__(self):
        pass


    def remove_stopwords(self,text):
        words_filteration = ['hello', 'welcome','so','however,','however','greetings']
        clean_sent = []
        for w in word_tokenize(text):
            if not w in words_filteration:
                clean_sent.append(w)
        # return " ".join(clean_sent)
        filtered_text = " ".join(clean_sent)
        print("--word filtered--")
        print(filtered_text)

        # with open("output1.txt", "w") as text_file:
        #     print("{}".format(filtered_text), file=text_file)

        self.punctuation_removal_obj.remove_punct(filtered_text)









