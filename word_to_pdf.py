def word_to_pdf(folder_path):
  import os
  from docx2pdf import convert 

  # Loop through all files in the folder
  for filename in os.listdir(folder_path):
    
      # Check if the file is a Word document (.docx or .doc)
      if filename.endswith(".docx") or filename.endswith(".doc"):
          
          # Get the full path of the Word document
          file_path = os.path.join(folder_path, filename)

          # Generate the new PDF filename (replace .docx or .doc with .pdf)
          pdf_filename = os.path.splitext(filename)[0] + ".pdf"

          # Convert the Word document to PDF using docx2pdf
          try:
              convert(file_path, os.path.join(folder_path, pdf_filename))
              print(f"Converted '{filename}' to '{pdf_filename}' successfully!")
          except Exception as e:
              print(f"Error converting '{filename}': {e}")

  print("All word to PDF conversions completed.")
