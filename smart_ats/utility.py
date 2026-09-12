import PyPDF2


def extract_text_from_pdf(pdf_file):
    """
    Extracts text content from an uploaded PDF file.

    Args:
        pdf_file: An uploaded file object from st.file_uploader.

    Returns:
        str: The concatenated text from all pages of the PDF.
        Returns None if the file cannot be read.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text_content = ""

        for page in pdf_reader.pages:
            text_content += page.extract_text()

        return text_content

    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return None
