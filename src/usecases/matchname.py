import re


def matchName(certificate_name, extract):
    regex = r'\b\w*' + re.escape(certificate_name) + r'\w*\b'
    find = re.findall(regex, extract, re.IGNORECASE)

    for results in find:
        if results == certificate_name:
            print('correct: ' + results)
            return True
    print('incorrect document name ' + regex)
    return False
