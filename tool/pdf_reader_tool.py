import os
import PyPDF2
import re

# 过滤PDF论文中APA格式的参考文献的正则表达式
regex_apa = r"^\s*\[\d+\]\s*([A-Z][a-z]+,?\s*){1,3}\(\d{4}\)\.\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+," \
            r"?\s*\d+\(\d+\),\s*\d+\-\d+\.\s*$"

# 过滤PDF论文中MLA格式的参考文献的正则表达式
regex_mla = r"^\s*\[\d+\]\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+,\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+," \
            r"?\s*\d+\(\d+\),\s*\d+\-\d+\.\s*$"

# 过滤PDF论文中Chicago格式的参考文献的正则表达式
regex_chicago = r"^\s*\[\d+\]\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+,\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+," \
                r"?\s*\d+\.\s*$"

# 过滤PDF论文中IEEE格式的参考文献的正则表达式
regex_ieee = r"^\s*\[\d+\]\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+,\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+," \
             r"?\s*\d+\(\d+\),\s*\d+\-\d+\.\s*$"

# 过滤PDF论文中ACM格式的参考文献的正则表达式
regex_acm = r"^\s*\[\d+\]\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+,\s*([A-Z][a-z]+,?\s*){1,3}\.\s*[A-Z][a-z]+," \
            r"?\s*\d+\.\s*$"

regex_list = [re.compile(regex_apa), re.compile(regex_mla), re.compile(regex_chicago), re.compile(regex_chicago),
              re.compile(regex_acm)]


def read_pdf(file_path):
    # Extract the filename and extension from the file path
    _, ext = os.path.splitext(file_path)

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


# 使用regex_apa、regex_mla、regex_chicago、regex_ieee、regex_acm过滤输入的文本内容，并将过滤后的内容写到文件中
def filter_text_with_regex(text: str, file_path: str):
    for regex in regex_list:
        # 使用正则表达式过滤输入的文本内容
        filtered_text = regex.findall(text)

        # 将过滤后的内容写到文件中
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in filtered_text:
                file.write(line + '\n')
