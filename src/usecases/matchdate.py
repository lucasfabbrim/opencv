import re


def matchDate(certificate_date, extract):
    escaped_date = re.escape(certificate_date)
    regex = r'\b' + escaped_date + r'\b'

    if re.search(regex, extract, re.IGNORECASE):
        print('correct: ' + regex)
        return True
    else:
        print('incorrect date: ' + regex)
        return False
