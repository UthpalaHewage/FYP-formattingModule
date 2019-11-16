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
        with open('files/kachal.txt', 'r') as file:
        # with open('files/test1.txt', 'r') as file:
        # with open('files/informal collection.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
            # print(data)

            with open("formattedFile.txt", "w") as text_file:
                print("{}".format(data), file=text_file)

            doc = nlp(data)
            sent_list = []
            # obtain sentences
            for sent in doc.sents:
                # make the first letter of the sentence into lower case
                sentence = str(sent)[0].lower() + str(sent)[1:]
                # make the array with list of sentences
                sent_list.append(sentence)

            self.contraction_removal_obj.expand_contractions(sent_list)
