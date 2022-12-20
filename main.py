import os
import sys
import shutil
from pdf2image import convert_from_path

# file_name = sys.argv[1]
file_name = 'sample.pdf'

current_wk_dir = os.getcwd()
target_file = current_wk_dir + file_name

if not os.path.exists('tmp'):
    os.makedirs('tmp')

pdf_images = convert_from_path(file_name)
for i in range(len(pdf_images)):
    pdf_images[i].save('tmp/' + 'page' + str(i) + '.jpg', 'JPEG')

shutil.make_archive('output', 'zip', 'tmp')

os.rename('output.zip', 'output.cbz')
