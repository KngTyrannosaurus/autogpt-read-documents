from PyPDF2 import PdfReader


def read_pdf(pdf_directory: str) -> str:
    """ Extract text from a PDF
    Args:
        pdf_directory(str): The diectory the PDF is located in.

    Returns:
        str containing all text extracted from the PDF. New pages are formatted with '/n/n'
    """

    # creating a pdf reader object
    reader = PdfReader(dir)

    #
    extracted_pages = [page.extract_text() for page in reader.pages]

    return '/n/n'.join(extracted_pages)

