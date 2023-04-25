import os
import PyPDF2


def read_pdf(file_path):
    # Extract the filename and extension from the file path
    filename, ext = os.path.splitext(file_path)

    # Open the PDF file
    with open(file_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Create a new TXT file for each page
            txt_filename = "{}_{}.txt".format("PDFFile", page_num + 1)
            with open(txt_filename, 'w', encoding='utf-8') as txt_file:
                # Extract the text from the page
                page_text = pdf_reader.pages[page_num].extract_text()

                # Split the page text into paragraphs
                paragraphs = page_text.split('\n\n')

                # Loop through each paragraph and write it to the TXT file
                for i, paragraph in enumerate(paragraphs):
                    # Add any title to the previous paragraph and remove any leading/trailing whitespace
                    paragraph = paragraph.strip()
                    if i > 0 and paragraph[0].isupper():
                        paragraphs[i - 1] += ' ' + paragraph
                    else:
                        # Write the paragraph to the TXT file
                        txt_file.write(paragraph + '\n')
