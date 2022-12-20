import os
import uuid
import shutil
from rich.progress import Progress, SpinnerColumn, TextColumn
from pdf2image import convert_from_path


def convert_to_cbz(file_lst):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        rand_hex = str(uuid.uuid4().hex)

        for file in file_lst:
            if not os.path.exists('tmp'):
                os.makedirs('tmp')

            pdf_images = convert_from_path(file)
            for page_order in range(len(pdf_images)):
                pdf_images[page_order].save('tmp/' + 'page' + str(page_order) + rand_hex + '.jpg', 'JPEG')
            file_no_ext = str(file)[:-4]
            shutil.make_archive(f'{file_no_ext}', 'zip', 'tmp')

            os.rename(f'{file_no_ext}.zip', f'{file_no_ext}.cbz')
            shutil.rmtree('tmp')

