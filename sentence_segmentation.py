# Import spaCy and load the language library
import spacy
import re
import contraction_removal

# load small version of english library
nlp = spacy.load('en_core_web_sm')


class sentence_segmentation:
    contraction_removal_obj = contraction_removal.contraction_removal()

    def __init__(self):
        pass

    def sent_segment(self):
        with open('sampletranscript.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
            print(data)

            # formatted_text = re.sub(" +", " ", data)
            # print(formatted_text)

            with open("formattedFile.txt", "w") as text_file:
                print("{}".format(data), file=text_file)

            doc = nlp(data)
            for sent in doc.sents:
                self.contraction_removal_obj.expand_contractions(str(sent))


