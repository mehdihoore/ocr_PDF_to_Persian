import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
from docx.shared import Inches
import docx
# Set the path to your PDF file
pdf_path = input( 'آدرس فایل را وارد کنید ')

# Convert the PDF to images
images = convert_from_path(pdf_path)

# Create a new Word document
doc = Document()
a= docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT
# Loop through each image and extract text using OCR
for i, image in enumerate(images):
    # Save the image as a temporary file
    image_path = f'temp_image_{i}.jpg'
    image.save(image_path, 'JPEG')

    # Extract text using OCR
    text = pytesseract.image_to_string(Image.open(image_path), lang='fas')

    # Add a new page to the Word document
    if i > 0:
        doc.add_page_break()

    # Add the extracted text to the Word document
    paragraph = doc.add_paragraph(text)
    paragraph.style = doc.styles['Normal']
    paragraph.alignment = a


# Save the Word document
doc.save('output.docx')


