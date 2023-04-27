from PyPDF2 import PdfReader


def read_pdf(dir):
    # creating a pdf reader object
    reader = PdfReader(dir)

    #
    extracted_pages = [page.extract_text() for page in reader.pages]

    return '/n/n'.join(extracted_pages)

