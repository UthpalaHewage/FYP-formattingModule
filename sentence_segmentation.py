# Import spaCy and load the language library
import spacy
import nltk
from nltk import tokenize
import contraction_removal
import question_detection

# load small version of english library
nlp = spacy.load('en_core_web_sm')


class sentence_segmentation:
    contraction_removal_obj = contraction_removal.contraction_removal()
    question_detection_obj = question_detection.question_detection()

    def __init__(self):
        pass

    def sent_segment(self):
        # with open('files/kachal.txt', 'r') as file:
        # with open('files/test1.txt', 'r') as file:
        with open('files/informal collection.txt', 'r') as file:
            data = file.read()
            list = tokenize.sent_tokenize(data.replace("\n", " "))

            sent_list = []
            # obtain sentences
            for sent in list:
                sent = str(sent)
                # filter out the questions available
                check_question = self.question_detection_obj.identify_questions(sent)
                if check_question:
                    pass
                else:
                    # make the first letter of the sentence into lower case
                    sentence = sent[0].lower() + sent[1:]
                    # make the array with list of sentences
                    sent_list.append(sentence.strip())
                    # print(sent)

            self.contraction_removal_obj.expand_contractions(sent_list)
