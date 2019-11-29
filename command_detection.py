import spacy
import informal_word_replacement

nlp = spacy.load('en_core_web_sm')


class command_detection:
    informal_word_replacement_obj =informal_word_replacement.informal_word_replacement()

    # replacement =  {"####"}
    def __init__(self):
        pass

    def command_det(self, sent_list):

        for i in range(len(sent_list)):
            # make the first letter of the selected sentence into upper case because if not named entities will also be detect as base verbs
            sentence = str(sent_list[i])[0].upper() + str(sent_list[i])[1:]
            sentence = nlp(sentence)
            # print(f'{sentence[0].text:{10}} {sentence[0].tag_}')

            if str(sentence[0].tag_) == 'VB':
                # replace the position with # for later use
                sent_list[i] = '#'

        # for sent in sent_list:
        #     print(sent)

        self.informal_word_replacement_obj.informal_word_detection(sent_list)