from src.usecases.matchowner import matchOwner
from src.usecases.matchname import matchName
from src.usecases.matchdate import matchDate
from src.usecases.matchcontent import matchContent


class Certificate:
    def __init__(self, document, name, owner, date):
        self.document = document
        self.owner = owner
        self.name = name
        self.date = date

    def hasRight(self, extract):
        if (matchDate(self.date, extract)
                and matchOwner(self.owner, extract)
                and matchName(self.name, extract)
                and matchContent(extract)):
            print('certificate: approved')
            return True
        print('certificate: failed')
        return False
