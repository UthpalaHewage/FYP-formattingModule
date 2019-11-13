import Model.fact_dict as dict

class sent_modify_fact_detection:

    def __init__(self):
        pass

    def sent_modify(self, sent_list):
        keys_list =  self.get_list_of_facts(sent_list)

        for key in keys_list :
            print(sent_list[key])

    def get_list_of_facts(self,sent_list):
        keys = []

        all_dict = {**dict.facts_on_phrases, **dict.facts_on_quotes, **dict.facts_on_colon}

        for key in all_dict :
            keys.append(key)

        return keys
