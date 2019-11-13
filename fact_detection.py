import Model.fact_dict as dict
import re
import spacy
import sent_modify_fact_detection
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import PhraseMatcher


class fact_detection:
    sent_modify_fact_detection_obj = sent_modify_fact_detection.sent_modify_fact_detection()

    pattern = re.compile(r"['\"](.*?)['\"]")

    def __init__(self):
        pass

    def detect_by_colon(self, sent_list):

        for i in range(len(sent_list)):

            if ":" in sent_list[i]:
                index = sent_list[i].index(":")
                dict.facts_on_colon.update({i: sent_list[i][index:]})
                sent_list[i] = sent_list[i][:index]

        self.detect_by_quotes(sent_list)

        # for key in dict.facts_on_colon:
        #     print(dict.facts_on_colon[key])

    def detect_by_quotes(self, sent_list):

        for i in range(len(sent_list)):
            result = self.pattern.search(sent_list[i])
            if result is not None:
                # print(sent_list[i])
                dict.facts_on_quotes.update({i: sent_list[i][result.start():]})
                sent_list[i] = sent_list[i][:result.start()]

        # for sentence in sent_list:
        #     print(sentence)
        #     print(" ")

        self.sent_modify_fact_detection_obj.sent_modify(sent_list)

    def detect_by_phrase_matching(self, sent_list):

        matcher = PhraseMatcher(nlp.vocab)
        # First, create a list of match phrases:
        phrase_list = ['as an example', 'for an example', 'such as', 'other examples', 'some of them', 'for instance',
                       'to give you an idea', 'as proof', 'suppose that', 'for example']

        # Next, convert each phrase to a Doc object:
        phrase_patterns = [nlp(text) for text in phrase_list]
        matcher.add('Fact_Matcher', None, *phrase_patterns)

        for i in range(len(sent_list)):
            sentense = nlp(sent_list[i])
            matches = matcher(sentense)

            if len(matches) > 0:
                end_index = matches[0][2]
                dict.facts_on_phrases.update(({i: str(sentense[end_index:])}))
                sent_list[i] = str(sentense[:end_index])

        self.detect_by_colon(sent_list)
