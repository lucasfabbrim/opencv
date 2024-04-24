import re


def matchContent(extract):
    regex = r'\b\w*Conteúdo\w*\b'
    matches = re.findall(regex, extract, re.IGNORECASE)

    if matches:
        print('have content')
        return True
    else:
        print('not have content')
        return False
