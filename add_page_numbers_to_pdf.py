from PyPDF2 import PdfReader
import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def add_page_numbers(input_pdf, output_pdf):
    if not os.path.exists(input_pdf):
        print("Input PDF file not found.")
        return

    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        writer = PyPDF2.PdfWriter()

        for page_number, page in enumerate(reader.pages, start=1):
            if page_number > 1:  # Start numbering from the second page
                packet = canvas.Canvas("temp.pdf", pagesize=(page.mediabox[2], page.mediabox[3]))  # Use page width and height
                packet.setFont("Helvetica", 10)
                text = f"Page {page_number - 1} of {total_pages - 1}"  # Adjusted page number and total pages
                
                # Convert FloatObject to float
                width = float(page.mediabox[2])
                
                x = (width - packet.stringWidth(text, "Helvetica", 10)) / 2  # Center horizontally
                y = 20  # Fixed vertical position
                packet.drawString(x, y, text)
                packet.save()

                watermark = PyPDF2.PdfReader("temp.pdf")
                watermark_page = watermark.pages[0]
                page.merge_page(watermark_page)
            writer.add_page(page)

        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    input_path = r"C:\Users\js105\Documents\Work\Dad's Work\Merged File\Merged File PDF.pdf"
    output_path = r"C:\Users\js105\Documents\Work\Dad's Work\Merged File\Merged PDF with Page Numbers.pdf"
    add_page_numbers(input_path, output_path)
