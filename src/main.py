import os

from src.entities.certificate import Certificate

from src.usecases.matchowner import matchOwner
from src.usecases.matchname import matchName
from src.usecases.matchdate import matchDate

import cv2
import pytesseract

from pdf2image import convert_from_path

certificate = Certificate('../certificate.pdf', 'Node.js', 'Lucas Fabbri', '05/02/2024')

pdf = convert_from_path(certificate.document)

for i, page in enumerate(pdf):

    image_path = f'certificate_{i + 1}.png'
    img = cv2.imread(image_path)
    page.save(image_path, 'PNG')

    extract = pytesseract.image_to_string(img, lang='por')

    if matchOwner(certificate.owner, extract) and matchName(certificate.name, extract) and matchDate(certificate.date,
                                                                                                     extract):
        print('approved')
    else:
        print('not approved')
