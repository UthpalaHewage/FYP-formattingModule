import re
# to install contractions - pip install contractions
from contractions import contractions_dict
import word_filteration


class contraction_removal:
    # when 'I' losses its capitalization when at first place then wont detect as pronoun so need to forcefully give the expansion form
    contractions_dict.update({'i\'m': 'i am'})
    word_filteration_obj = word_filteration.word_filteration()

    def __init__(self):
        pass

    # to get the expanded form of contraction with expand_match
    def expand_contractions(self, sentence_list):
        contractions_pattern = re.compile('({})'.format('|'.join(contractions_dict.keys())))

        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            # make the selection for expanded form
            expanded_contraction = contractions_dict.get(match) \
                if contractions_dict.get(match) \
                else contractions_dict.get(match.lower())
            # assign the expanded form into expanded_contraction
            expanded_contraction = expanded_contraction
            return expanded_contraction

        removed_contractions_sentence_list = []
        for sentense in sentence_list:
            # sub-for replacing the contraction with expanded form
            expanded_text = contractions_pattern.sub(expand_match, sentense)
            # join the expanded text into the original sentence
            removed_contractions_sentence_list.append(str(expanded_text))

        self.word_filteration_obj.remove_words_by_ruleBasedMatching(removed_contractions_sentence_list)
