from datetime import datetime
import re


def matchDate(certificate_date, extract):
    regex = r'\b\d{2}/\d{2}/\d{4}\b'

    matches = re.findall(regex, extract)
    result = matches[-1]

    if result == certificate_date:
        print('correct: ' + result)
        return True
    else:
        print('incorrect date ' + result + " is different of " + certificate_date)
