"""final output of the formatting module"""
import Model.fact_dict as fact_dict


class FinalOutput(object):
    """class for the final output"""

    final_sent_list = []
    final_para = ""

    def __init__(self):
        pass

    def final_output(self, sent_list):
        for i in range(len(sent_list)):
            if sent_list[i][0] is not "#":
                if i in fact_dict.facts_on_quotes:
                    sent_list[i] = sent_list[i].strip() + " " + fact_dict.facts_on_quotes[i].strip()
                if i in fact_dict.facts_on_semicolon:
                    sent_list[i] = sent_list[i].strip() + " " + fact_dict.facts_on_semicolon[i].strip()
                if i in fact_dict.facts_on_colon:
                    sent_list[i] = sent_list[i].strip() + " " + fact_dict.facts_on_colon[i].strip()
                if i in fact_dict.facts_on_phrases:
                    sent_list[i] = sent_list[i].strip() + " " + fact_dict.facts_on_phrases[i].strip()
                self.final_sent_list.append(sent_list[i][0].upper() + sent_list[i][1:])

        for sent in self.final_sent_list:
            self.final_para = self.final_para + " " + sent
            print(sent)

        print("---------------------------------------------")
        print(self.final_para.strip())
