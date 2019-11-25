import Model.fact_dict as dict
import re
import spacy

nlp = spacy.load('en_core_web_sm')
import sent_modify_fact_detection
from spacy.matcher import PhraseMatcher


class fact_detection:
    sent_modify_fact_detection_obj = sent_modify_fact_detection.sent_modify_fact_detection()

    # define the pattern for the identification of quoted text
    pattern = re.compile(r"['\"](.*?)['\"]")

    def __init__(self):
        pass

    def detect_by_colon(self, sent_list):

        for i in range(len(sent_list)):

            if ":" in sent_list[i]:
                index = sent_list[i].index(":")
                # dictionary is updated with the index respect to the fact identified with colon
                dict.facts_on_colon.update({i: sent_list[i][index:]})
                sent_list[i] = sent_list[i][:index]

        self.detect_by_semicolon(sent_list)

        # # printing the dict
        # for key in dict.facts_on_colon:
        #     print(dict.facts_on_colon[key])

    def detect_by_semicolon(self, sent_list):

        for i in range(len(sent_list)):

            if ";" in sent_list[i]:
                index = sent_list[i].index(";")
                # dictionary is updated with the index respect to the fact identified with semicolon
                dict.facts_on_semicolon.update({i: sent_list[i][index:]})
                sent_list[i] = sent_list[i][:index]

        self.detect_by_quotes(sent_list)

        # printing the dict
        # for key in dict.facts_on_semicolon:
        #     print("semicolon dict")
        #     print(dict.facts_on_semicolon[key])

    def detect_by_quotes(self, sent_list):

        for i in range(len(sent_list)):
            # search for the pattern defined above
            result = self.pattern.search(sent_list[i])
            if result is not None:
                # print(sent_list[i])
                # dictionary is updated with the index respect to the fact identified with quotes
                dict.facts_on_quotes.update({i: sent_list[i][result.start():]})
                # if the sentence(output) begins with a quote it will completely replaced with ## for later use
                if result.start() == 0:
                    sent_list[i] = "##"
                else:
                    sent_list[i] = sent_list[i][:result.start()]

        for sentence in sent_list:
            print(sentence)
            print(" ")

        # self.sent_modify_fact_detection_obj.sent_modify(sent_list)

    def detect_by_phrase_matching(self, sent_list):

        matcher = PhraseMatcher(nlp.vocab)
        # Create a list of match phrases:
        # phrase_list = ['as an example', 'for an example', 'such as', 'other examples', 'some of them', 'for instance',
        #                'to give you an idea', 'as proof', 'suppose that', 'for example']

        # need to declare different patterns
        phrase_list = ['for example', 'examples are', 'examples include', 'another example', 'is an example', 'in this example', 'take the example of ', 'take this example', 'further examples are', 'some common examples of', 'such as', 'examples of']

        # Convert each phrase to a Doc object:
        phrase_patterns = [nlp(text) for text in phrase_list]
        matcher.add('Fact_Matcher', None, *phrase_patterns)

        for i in range(len(sent_list)):
            sentense = nlp(sent_list[i])
            matches = matcher(sentense)

            if len(matches) > 0:
                end_index = matches[0][2]
                # dictionary is updated with the index respect to the fact identified with defined phrases
                dict.facts_on_phrases.update(({i: str(sentense[end_index:])}))
                sent_list[i] = str(sentense[:end_index])

        self.detect_by_colon(sent_list)
