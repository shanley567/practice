from PyPDF2 import PdfReader

def detect_paper_size(pdf_file):
  
  with open(pdf_file, "rb") as f:
    reader = PdfReader(f)

    page_sizes = []
    for i, page in enumerate(reader.pages):
      # Get the page size information
      media_box = page.mediabox

      # Convert points to mm (1 point = 1/72 inch, 25.4 mm/inch)
      width_mm = float(media_box[2]) / 72 * 25.4
      height_mm = float(media_box[3]) / 72 * 25.4

      # Define paper sizes in a dictionary with width and height in millimeters
      paper_sizes = {
          "A4": (210, 297),
          "A3": (297, 420),
          "A2": (420, 594),
          "A1": (594, 841),
          "A0": (841, 1189),
      }

      # Check for matching size with tolerance
      paper_size = None
      for size, (size_width, size_height) in paper_sizes.items():
        if abs(width_mm - size_width) <= 5 and abs(height_mm - size_height) <= 5:
          paper_size = size
          break  # Exit loop after finding a match

      page_sizes.append({
        "page_number": i + 1,
        "width": width_mm,
        "height": height_mm,
        "paper_size": paper_size,
      })

  return page_sizes

# # Example usage
# pdf_file = r"C:\Users\js105\Documents\Work\Dad's Work\Merged File\Merged PDF.pdf"  # Replace with your PDF file path
# page_sizes = detect_paper_size(pdf_file)
# # print(type(page_sizes))
# print(*page_sizes, sep="\n")