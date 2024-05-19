# Function to convert all JPEGs in a folder to PDFs
def convert_image_to_pdfs(folder_path):
  from img2pdf import convert
  import os
  """
  Converts all JPEG images in a folder to PDF files with the same names and .pdf extension.

  Args:
      folder_path: Path to the folder containing JPEG images.
  """
  for filename in os.listdir(folder_path):
    # Check if it's a JPEG image
    if filename.lower().endswith(".jpg"):
      image_path = os.path.join(folder_path, filename)
      # Get filename without extension
      filename, _ = os.path.splitext(os.path.basename(image_path))
      # Create output PDF filename with .pdf extension
      output_filename = os.path.join(folder_path, f"{filename}.pdf")

      # Open image and convert to PDF
      with open(image_path, "rb") as image_file:
        pdf_bytes = convert(image_file)

      # Write PDF bytes to output file
      with open(output_filename, "wb") as pdf_file:
        pdf_file.write(pdf_bytes)

      print(f"Converted {filename}")

  print("Finished converting all JPEGs to PDFs!")
