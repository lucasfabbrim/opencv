import re


def matchName(certificate_name, extract):
    regex = r'\b\w*' + re.escape(certificate_name) + r'\w*\b'
    find = re.findall(regex, extract, re.IGNORECASE)

    for results in find:
        if results == certificate_name:
            print('correct: ' + certificate_name)
            return True
    print('incorrect name of document!')
    return False
