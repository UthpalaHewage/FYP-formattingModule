import inflect

inflect = inflect.engine()


def replace_pronoun(sentence, subject_idx):
    if inflect.singular_noun(str(sentence[subject_idx])) is False:
        new_sentence = str(sentence[:subject_idx]).strip() + " it " + str(sentence[subject_idx + 1:]).strip()
        return new_sentence.strip()
    else:
        new_sentence = str(sentence[:subject_idx]).strip() + " they " + str(sentence[subject_idx + 1:]).strip()
        return new_sentence.strip()
