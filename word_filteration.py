# import spacy
# nlp = spacy.load('en_core_web_sm')
import punctuation_removal
import fact_detection


class word_filteration:
    # punctuation_removal_obj = punctuation_removal.punctuation_removal()
    fact_detection_obj = fact_detection.fact_detection()

    def __init__(self):
        pass

    def remove_stopwords(self, sentence_list):

        words_filteration = ['hello', 'welcome', 'so', 'however,', 'however', 'greetings', 'hi,', 'dude,',
                             'good morning', 'please']

        sent_list = []
        for sentence in sentence_list:
            list = str(sentence).split(" ")
            clean_sent = []

            for w in list:
                if not w in words_filteration:
                    clean_sent.append(w)

            if len(clean_sent) > 2:
                filtered_text = " ".join(clean_sent)
                # print("--word filtered--")
                # print(filtered_text)
                sent_list.append(filtered_text)

        self.fact_detection_obj.detect_by_phrase_matching(sent_list)
        # self.punctuation_removal_obj.remove_punct(filtered_text)
