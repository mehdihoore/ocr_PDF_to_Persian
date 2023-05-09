# ocr_PDF_to_Persian
OCR a PDF in Persian language. required libraries - pytesseract, Pillow, and pdf2image
# Prerequisites
Python 3.6 or above  
pytesseract Python module (for OCR)  
PIL Python module (for image processing)  
pdf2image Python module (for converting PDF to images)  
docx Python module (for creating Word documents)  
# Installation
Install Python 3.6 or above.  
Install the required Python modules using pip: pip install pytesseract pillow pdf2image python-docx  
# Usage
Open a terminal or command prompt.  
Navigate to the directory where the script is located.  
Run the script by typing python OcrInFolders.py.  
When prompted, enter the path to the folder containing the PDF files you want to convert.  
The script will traverse through the directory and subdirectories, convert all PDF files to Word documents, and save them in the same directory as the original PDF file.  
# Notes
The script uses OCR to extract text from the PDF files, so the accuracy of the converted text depends on the quality of the PDF files and the OCR engine used.  
The script uses the default OCR language of English. To change the OCR language, modify the lang parameter in the convert_pdf_to_word function.  
The script assumes that the PDF files have a .pdf extension. To convert files with a different extension, modify the if file.endswith('.pdf'): statement in the for loop.  
The script will overwrite any existing Word files with the same name as the PDF files.  
The script will create a new Word file for each page of the PDF file.  
The script will add a page break between each page of the Word document.  
