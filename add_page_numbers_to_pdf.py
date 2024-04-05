
def add_page_numbers(folder_path):
  from PyPDF2 import PdfReader, PdfWriter
  from reportlab.lib.pagesizes import A4
  from reportlab.pdfgen import canvas
  import os
  if not os.path.exists(folder_path):
    print("Folder path not found.")
    return

  input_pdf = os.path.join(folder_path, "Merged File", "Merged File PDF.pdf")

  if not os.path.exists(input_pdf):
    print("Input PDF file not found within the specified folder.")
    return

  with open(input_pdf, 'rb') as file:
    reader = PdfReader(file)
    total_pages = len(reader.pages)
    writer = PdfWriter()

    for page_number, page in enumerate(reader.pages, start=1):
      if page_number > 1:  # Start numbering from the second page
        packet = canvas.Canvas("temp.pdf", pagesize=(page.mediabox[2], page.mediabox[3]))
        packet.setFont("Helvetica", 10)
        text = f"Page {page_number - 1} of {total_pages - 1}"  # Adjusted page number and total pages
        width = float(page.mediabox[2])
        x = (width - packet.stringWidth(text, "Helvetica", 10)) / 2  # Center horizontally
        y = 18  # Fixed vertical position
        packet.drawString(x, y, text)
        packet.save()

        watermark = PdfReader("temp.pdf")
        watermark_page = watermark.pages[0]
        page.merge_page(watermark_page)
      writer.add_page(page)

  # Directly define the output path within the function (modified)
  output_path = os.path.join(folder_path, "Merged File", "With Page Numbers.pdf")

  with open(output_path, 'wb') as output_file:
    writer.write(output_file)
