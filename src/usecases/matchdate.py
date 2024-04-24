from datetime import datetime
import re


def matchDate(certificate_date, extract):
    regex = r'\b\d{2}/\d{2}/\d{4}\b'

    matches = re.findall(regex, extract)
    result = matches[-1]

    if result == certificate_date:
        print('date: approved')
        return True
    else:
        print('date: failed')
