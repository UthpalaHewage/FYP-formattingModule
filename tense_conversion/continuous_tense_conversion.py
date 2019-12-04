"""Identify the sentences in continuous form and make the tense conversion """
import spacy
import inflect
# used to get the singular form of verb
from pyinflect import getInflection
import tense_conversion.Models.verb_sub_container as dict_container
import tense_conversion.past_tense_conversion as past_tense_conversion

nlp = spacy.load('en_core_web_sm')


class ContinuousTenseConversion(object):
    """class for the tense conversion of continuous sentences"""

    # import the method for the conversion of past tense sentences
    past_tense_conversion_obj = past_tense_conversion.PastTenseConversion()

    # check for the singular nature of noun..
    # if the given noun is singular result- False. If not gives the singular form
    inflect = inflect.engine()
    # declare the aux_list need for the  conversion of tenses
    aux_list = ["is", "are", "am", "was", "were"]

    def __init__(self):
        pass

    def continuous_tense_con(self, sent_list):
        """conversion of continuous tense sentences to simple tense"""

        for i in range(len(sent_list)):
            # the sent not marked with #-(for command det) and ###-(for future tense det) earlier
            # as index is checked # is enough to filter out both
            if sent_list[i][0] is not "#":
                content = dict_container.verb_sub_dict.get(i)

                if content is not None:
                    root_verb = content[0]
                    subject = content[1]
                    sentense = nlp(sent_list[i][0].upper() + sent_list[i][1:])

                    if str(sentense[root_verb].tag_) == "VBG":

                        # out of the aux identified specifically select the
                        # aux matches to aux_list declared
                        # 'str(sentense[idx]) in self.aux_list'
                        aux_index = [idx for idx in range(len(sentense)) if
                                     str(sentense[idx].dep_) == "aux" and subject < idx <
                                     root_verb and str(sentense[idx]) in self.aux_list]
                        # get the base form of the verb
                        base_verb = sentense[root_verb].lemma_

                        if len(aux_index) != 0:
                            aux_idx = aux_index[0]
                            # check the availability of 'not' in the sentence - negation
                            negation_availability = True if str(sentense[aux_idx + 1]) == "not" else False

                            # continuous sent with 'I' is converted
                            if str(sentense[subject]) is "I":
                                sent_list[i] = self.i_based_sent(negation_availability, sentense, aux_idx, root_verb,
                                                                 base_verb)

                            # singular continuous sent is converted
                            elif self.inflect.singular_noun(str(sentense[subject])) is False:
                                sent_list[i] = self.singular_sent(negation_availability, sentense, aux_idx, root_verb,
                                                                  base_verb)

                            # plural continuous sent is converted
                            else:
                                sent_list[i] = self.plural_sent(negation_availability, sentense, aux_idx, root_verb,
                                                                base_verb)

        for i in range(len(sent_list)):
            sent_list[i] = sent_list[i][0].lower() + sent_list[i][1:]
            # print(sent_list[i])

        self.past_tense_conversion_obj.past_tense_con(sent_list)

    @staticmethod
    def i_based_sent(negation_availability, sentense, aux_idx, root_verb, base_verb):
        """conversion of sent with 'I'"""
        if negation_availability:
            return str(sentense[:aux_idx]).strip() + " do " + str(
                sentense[aux_idx + 1:root_verb]).strip() + " " + base_verb + " " + str(
                sentense[root_verb + 1:]).strip()

        return str(sentense[:aux_idx]).strip() + " " + str(
            sentense[aux_idx + 1:root_verb]).strip() + base_verb + " " + str(
            sentense[root_verb + 1:]).strip()

    @staticmethod
    def singular_sent(negation_availability, sentense, aux_idx, root_verb, base_verb):
        """conversion of singular sent """
        if negation_availability:
            return str(sentense[:aux_idx]).strip() + " does " + str(
                sentense[aux_idx + 1:root_verb]).strip() + " " + base_verb + " " + str(
                sentense[root_verb + 1:]).strip()

        # VBZ - verb, 3rd person singular present
        return str(sentense[:aux_idx]).strip() + " " + str(
            sentense[aux_idx + 1:root_verb]).strip() + getInflection(base_verb, tag='VBZ')[0] + " " + str(
            sentense[root_verb + 1:]).strip()

    @staticmethod
    def plural_sent(negation_availability, sentense, aux_idx, root_verb, base_verb):
        """conversion of plural sent"""
        if negation_availability:
            return str(sentense[:aux_idx]).strip() + " do " + str(
                sentense[aux_idx + 1:root_verb]).strip() + " " + base_verb + " " + str(
                sentense[root_verb + 1:]).strip()

        return str(sentense[:aux_idx]).strip() + " " + str(
            sentense[aux_idx + 1:root_verb]).strip() + base_verb + " " + str(
            sentense[root_verb + 1:]).strip()
