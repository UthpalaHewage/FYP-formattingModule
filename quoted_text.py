# not yet connected
import re


class quoted_text:

    def extract_quoted_text(self, text):
        result = re.findall(r"['\"](.*?)['\"]", text)

        # result = re.findall(r'"([^"]*)"', text)
        print("--quoted text--")
        print(result)
