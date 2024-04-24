import re


def matchOwner(certificate_owner, extract):
    regex = r'\b\w*' + re.escape(certificate_owner) + r'\w*\b'
    find = re.findall(regex, extract, re.IGNORECASE)

    for results in find:
        if results == certificate_owner:
            print('owner_name: approved')
            return True
    print('owner_name: failed')
    return False
