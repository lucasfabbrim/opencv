import re


def matchName(certificate_name, extract):
    regex = r'\b\w*' + re.escape(certificate_name) + r'\w*\b'
    find = re.findall(regex, extract, re.IGNORECASE)

    for results in find:
        if results == certificate_name:
            print('document_name: approved')
            return True
    print('document_name: failed')
    return False
