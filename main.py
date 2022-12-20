import os
import sys
from pdf2image import convert_from_path

# file_name = sys.argv[1]
file_name = 'sample.pdf'

current_wk_dir = os.getcwd()
target_file = current_wk_dir + file_name

pdf_images = convert_from_path(file_name)
for i in range(len(pdf_images)):
    pdf_images[i].save('page'+ str(i) +'.jpg', 'JPEG')
