def merge_pdfs(folder_path):
    print("merge pdfs function")
    import os
    from PyPDF2 import PdfMerger

    merger = PdfMerger()
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            filepath = os.path.join(folder_path, filename)
            merger.append(filepath)

    # Define the desired output file path
    output_file_path = os.path.join(folder_path, "Merged File", "Merged File PDF.pdf")

    # Create the output directory if it doesn't exist
    output_dir = os.path.dirname(output_file_path)  # Get the directory path
    try:
        os.makedirs(output_dir, exist_ok=True)  # Create directories if needed
    except OSError as e:
        raise OSError(f"Error creating output directory: {e}") from e

    merger.write(output_file_path)
    merger.close()
    print("PDFs all merged")