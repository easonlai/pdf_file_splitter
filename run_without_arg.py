import os
from PyPDF2 import PdfReader, PdfWriter

def write_pdf_writer_to_file(pdf_writer, base_filename, counter):
    output_filename = os.path.join('output', f'{base_filename}_part_{counter}.pdf')
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
    print('Created:', output_filename)
    return output_filename

def pdf_splitter(path, size_limit_mb=2.5):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfReader(path)
    counter = 1
    pages_to_add = []

    for page in pdf.pages:
        pages_to_add.append(page)
        pdf_writer = PdfWriter()
        for page_to_add in pages_to_add:
            pdf_writer.add_page(page_to_add)
        temp_filename = write_pdf_writer_to_file(pdf_writer, fname, counter)
        
        if os.path.getsize(temp_filename) > size_limit_mb * 1024 * 1024:
            # If the file size exceeds the limit, remove the last page from the list and save the file
            pages_to_add.pop() # Remove the last page from the list
            if pages_to_add: # If there are still pages left
                # Write the current list of pages to a file, excluding the last one that caused overflow
                pdf_writer = PdfWriter()
                for page_to_add in pages_to_add:
                    pdf_writer.add_page(page_to_add)
                write_pdf_writer_to_file(pdf_writer, fname, counter)
                counter += 1
            # Reset the list of pages to add with only the last page
            pages_to_add = [page]

    # Save any remaining pages in the last PDF part
    if pages_to_add:
        pdf_writer = PdfWriter()
        for page_to_add in pages_to_add:
            pdf_writer.add_page(page_to_add)
        write_pdf_writer_to_file(pdf_writer, fname, counter)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_splitter(os.path.join(folder_path, filename))

if __name__ == '__main__':
    input_folder = 'input'
    process_folder(input_folder)