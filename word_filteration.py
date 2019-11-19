# Perform standard imports
import spacy

nlp = spacy.load('en_core_web_sm')

# Import the Matcher library
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

import fact_detection
import Model.rule_based_word_patterns as pattern_dict


class word_filteration:
    fact_detection_obj = fact_detection.fact_detection()

    def __init__(self):
        pass

    def remove_stopwords(self, sentence_list):

        # declare list of words that need to be filtered out directly-stop words
        words_filteration = ['welcome', 'so', 'greetings', 'hi', 'dude,',
                             'good morning', 'please', 'solar power']

        sent_list = []
        for sentence in sentence_list:
            # remove the unnecessary whitespaces after word filteration
            list = str(sentence).split(" ")
            clean_sent = []

            for w in list:
                if not w in words_filteration:
                    clean_sent.append(w)
            # print(list)

            # check for the sentence fragments whether it sstiafy the general conditions to be a sentence (availablity of min of 3 word)
            if len(clean_sent) > 2:
                filtered_text = " ".join(clean_sent)
                # print(filtered_text)
                sent_list.append(filtered_text)

        self.remove_words_by_ruleBasedMatching(sent_list)

    # added the word patterns of same word that need to be filtered out
    def remove_words_by_ruleBasedMatching(self, sent_list):

        for pattern in pattern_dict.dict:
            matcher.add(pattern, None,  pattern_dict.dict[pattern])

        for i in range(len(sent_list)):
            doc = nlp(sent_list[i])
            found_matches = matcher(doc)

            sentence = ""
            previous_end = None
            if len(found_matches) != 0:
                for matches in found_matches:
                    #     print(matches)
                    if previous_end == None:
                        sentence = sentence + " " + str(doc[:matches[1]]).strip()
                        previous_end = matches[2]

                    else:

                        sentence = sentence + " " + str(doc[previous_end:matches[1]]).strip()
                        previous_end = matches[2]

                sentence = sentence + " " + str(doc[previous_end:]).strip()
                sent_list[i] = sentence.strip()

        # for sent in sent_list:
        #     print(sent)

        self.fact_detection_obj.detect_by_phrase_matching(sent_list)