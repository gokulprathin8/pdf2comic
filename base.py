import os
import sys
import uuid
import shutil
from copy import deepcopy
from pdf2image import convert_from_path

cmd_args = sys.argv

file_lst = deepcopy(cmd_args)
file_lst = file_lst[1:]

current_wk_dir = os.getcwd()
rand_hex = str(uuid.uuid4().hex)

for file in file_lst:
    if not os.path.exists('tmp'):
        os.makedirs('tmp')

    pdf_images = convert_from_path(file)
    for page_order in range(len(pdf_images)):
        pdf_images[page_order].save('tmp/' + 'page' + str(page_order) + rand_hex + '.jpg', 'JPEG')
    file_no_ext = file[:-4]
    shutil.make_archive(f'{file_no_ext}', 'zip', 'tmp')

    os.rename(f'{file_no_ext}.zip', f'{file_no_ext}.cbz')
    shutil.rmtree('tmp')

