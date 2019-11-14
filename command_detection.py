import spacy
nlp = spacy.load('en_core_web_sm')

class command_detection:

    def __init__(self):
        pass

    def command_det(self,sent_list):

        for i in range(len(sent_list)):
            # make the first letter of the selected sentence into upper case because if not named entities will also be detect as base verbs
            sentence = (sent_list[i])[0].upper() + str(sent_list[i])[1:]
            sentence = nlp(sentence)
            # print(f'{sentense[0].text:{10}} {sentense[0].tag_}')

            if str(sentence[0].tag_) == 'VB' :
                print(sent_list[i]) 


