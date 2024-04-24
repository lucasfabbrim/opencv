import re


def matchContent(extract):
    regex = r'\b\w*Conteúdo\w*\b'
    matches = re.findall(regex, extract, re.IGNORECASE)

    if matches:
        print('content: approved')
        return True
    else:
        print('content: failed')
        return False
