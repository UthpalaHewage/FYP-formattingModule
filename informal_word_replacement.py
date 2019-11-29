import spacy
import string

nlp = spacy.load('en_core_web_sm')
from spacy.matcher import PhraseMatcher


class informal_word_replacement:

    def __init__(self):
        pass

    def informal_word_detection(self, sent_list):
        punctuation_list = string.punctuation
        matcher = PhraseMatcher(nlp.vocab)

        # need to declare informal-formal word list for replacement
        phrase_list = []
        with open('Model/informal_word_list.txt', 'r') as file:
            informal_word_list = ["" + line.strip() + "" for line in file]
        with open('Model/formal_word_list.txt', 'r') as file:
            formal_word_list = ["" + line.strip() + "" for line in file]

        # Convert each phrase to a Doc object:
        phrase_patterns = [nlp(text) for text in informal_word_list]
        matcher.add('Informal word matcher', None, *phrase_patterns)

        for i in range(len(sent_list)):
            sentense = nlp(sent_list[i])
            matches = matcher(sentense)

            if len(matches) != 0:
                # print(sentense[matches[0][1]:matches[0][2]])
                new_sent = ""
                previous_end = None
                for match in matches:
                    informal_word = str(sentense[match[1]:match[2]])
                    index = informal_word_list.index(informal_word)
                    formal_word = formal_word_list[index]

                    if previous_end == None:
                        new_sent = new_sent + str(sentense[:match[1]]).strip() + " " + formal_word
                        if str(sentense[match[2]]) not in punctuation_list:
                            new_sent = new_sent + " "
                            previous_end = match[2]
                        else:
                            previous_end = match[2]

                    else:

                        new_sent = new_sent + str(sentense[previous_end:match[1]]).strip() + " " + formal_word

                        if str(sentense[match[2]]) not in punctuation_list:
                            new_sent = new_sent + " "
                            previous_end = match[2]
                        else:
                            previous_end = match[2]

                new_sent = new_sent + str(sentense[previous_end:]).strip()
                print(new_sent.strip())

        # for sent in sent_list:
        #     print(sent)
