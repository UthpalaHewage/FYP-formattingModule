import Model.fact_dict as dict
import re


class fact_detection:
    pattern = re.compile(r"['\"](.*?)['\"]")

    def __init__(self):
        pass

    def detect_by_colon(self, sent_list):

        for i in range(len(sent_list)):

            if ":" in sent_list[i]:
                index = sent_list[i].index(":")
                dict.facts_on_colon.update({i: sent_list[i][index:]})
                sent_list[i] = sent_list[i][:index]
                # print(sent_list[i])

        # for key in dict.facts_on_colon:
        #     print(dict.facts_on_colon[key])

        for i in range(len(sent_list)):
            result = self.pattern.search(sent_list[i])
            if result is not None:
                # print(sent_list[i])
                dict.facts_on_quotes.update({i: sent_list[i][result.start():]})
                sent_list[i] = sent_list[i][:result.start()]
        # for key in dict.facts_on_quotes:
        #     print(dict.facts_on_quotes[key])
        #     print(" ")

        for sentence in sent_list :
            print(sentence)