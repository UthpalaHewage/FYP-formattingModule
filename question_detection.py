class question_detection:
    def __init__(self):
        pass

    def identify_questions(self, sentence):
        if "?" in sentence:
            return True
        else:
            return False
