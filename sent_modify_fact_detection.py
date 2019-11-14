import Model.fact_dict as dict
import spacy
import command_detection

nlp = spacy.load('en_core_web_sm')


# the sentence segment of the identified facts' sentence will be modified into present tense if available with any other tense
class sent_modify_fact_detection:

    command_detection_obj = command_detection.command_detection()

    def __init__(self):
        pass

    def sent_modify(self, sent_list):
        keys_list = self.get_list_of_facts(sent_list)

        for key in keys_list:
            # print(sent_list[key])
            tokenized_sent = nlp(sent_list[key])

            # tokenized and get the root-verb and check the tense.
            for token in tokenized_sent:
                if str(token.dep_) == 'ROOT' and str(token.tag_) == 'VBD':
                    # print(token.i)
                    # If it is any other tense convert to base form - (lemma_)
                    new_sent = str(tokenized_sent[:token.i]) + " " + str(token.lemma_) + " " + str(
                        tokenized_sent[token.i + 1:])
                    sent_list[key] = new_sent
                    # to get out of the conversion process
                    break

        # for key in keys_list:
        #     print(sent_list[key])
        # print("--------------")
        # for sent in sent_list:
        #     print(sent)

        self.command_detection_obj.command_det(sent_list)

    def get_list_of_facts(self, sent_list):
        keys = []

        # unit the 3 dict obtained through the fact collection
        all_dict = {**dict.facts_on_phrases, **dict.facts_on_quotes, **dict.facts_on_colon}

        for key in all_dict:
            keys.append(key)

        return keys
