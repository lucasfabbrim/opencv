from src.entities.certificate import Certificate
from pdf2image import convert_from_path

import os
import cv2
import pytesseract

certificate = Certificate('../certificate.pdf', 'Node.js', 'Lucas Fabbri', '09/02/2024')

pdf = convert_from_path(certificate.document)

for i, page in enumerate(pdf):

    image_path = f'certificate_{i + 1}.png'
    page.save(image_path, 'PNG')
    img = cv2.imread(image_path)

    extract = pytesseract.image_to_string(img, lang='por')
    certificate.hasRight(extract)
    os.remove(image_path)
