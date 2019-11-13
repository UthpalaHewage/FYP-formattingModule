import fact_detection


class word_filteration:
    fact_detection_obj = fact_detection.fact_detection()

    def __init__(self):
        pass

    def remove_stopwords(self, sentence_list):

        # declare list of words that need to be filtered out directly
        words_filteration = ['hello', 'welcome', 'so', 'however,', 'however', 'greetings', 'hi,', 'dude,',
                             'good morning', 'please']

        sent_list = []
        for sentence in sentence_list:
            # remove the unnecessary whitespaces after word filteration
            list = str(sentence).split(" ")
            clean_sent = []

            for w in list:
                if not w in words_filteration:
                    clean_sent.append(w)

            # check for the sentence fragments whether it sstiafy the general conditions to be a sentence (availablity of min of 3 word)
            if len(clean_sent) > 2:
                filtered_text = " ".join(clean_sent)
                # print(filtered_text)
                sent_list.append(filtered_text)

        self.fact_detection_obj.detect_by_phrase_matching(sent_list)
