'''
1. To get this to work you need 3 files called "word_to_pdf", "merge_pdfs" and "add_page_numbers"
   in the same folder as this file
2. Change the "folder_path" variable to the file path where your files are
3. Ensure that the requirements file has been downloaded using:

'''
from word_to_pdf import word_to_pdf
from jpeg_to_pdf import convert_image_to_pdfs
from merge_pdfs import merge_pdfs
from add_page_numbers_to_pdf import add_page_numbers

# change this line to the required folder path
folder_path = r"C:\Users\js105\Documents\Work\Dad's Work"   

word_to_pdf(folder_path)
convert_image_to_pdfs(folder_path)
merge_pdfs(folder_path)
add_page_numbers(folder_path)