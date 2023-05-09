import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
from docx.shared import Inches
import docx

# Function to convert PDF to Word document
def convert_pdf_to_word(pdf_path):
    # Convert the PDF to images
    images = convert_from_path(pdf_path)

    # Create a new Word document
    doc = Document()
    a = docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT

    # Loop through each image and extract text using OCR
    for i, image in enumerate(images):
        # Save the image as a temporary file
        image_path = f'temp_image_{i}.jpg'
        image.save(image_path, 'JPEG')

        # Extract text using OCR
        text = pytesseract.image_to_string(Image.open(image_path), lang='fas+equ')

        # Add a new page to the Word document
        if i > 0:
            doc.add_page_break()

        # Add the extracted text to the Word document
        paragraph = doc.add_paragraph(text)
        paragraph.style = doc.styles['Normal']
        paragraph.alignment = a

    # Save the Word document with the same name as the PDF file
    docx_path = os.path.splitext(pdf_path)[0] + '.docx'
    doc.save(docx_path)
path_folder= 
# Set the path to the folder containing the PDF files
pdf_folder_path = r'{}'.format(input('لطفا آدرس فولدر را وارد کنيد: '))


# Traverse through the directory and subdirectories
for root, dirs, files in os.walk(pdf_folder_path):
    for file in files:
        # Check if the file is a PDF file
        if file.endswith('.pdf'):
            pdf_path = os.path.join(root, file)
            print(f'Converting {pdf_path} to Word document...')
            convert_pdf_to_word(pdf_path)

