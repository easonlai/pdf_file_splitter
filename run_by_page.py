import os
from PyPDF2 import PdfReader, PdfWriter

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfReader(path)
    for page in range(len(pdf.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page])
        output_filename = os.path.join('output', '{}_page_{}.pdf'.format(fname, page+1))
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_splitter(os.path.join(folder_path, filename))

if __name__ == '__main__':
    input_folder = 'input'
    process_folder(input_folder)