import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

# Define a function to write the PDF writer object to a file
def write_pdf_writer_to_file(pdf_writer, output_folder, base_filename, counter):
    output_filename = os.path.join(output_folder, f'{base_filename}_part_{counter}.pdf')
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
    print('Created:', output_filename)
    return output_filename

# Define the PDF splitter function
# The function takes the path to the PDF file, the output folder, and an optional size limit in MB
def pdf_splitter(path, output_folder, size_limit_mb=2.5):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfReader(path)
    counter = 1
    pages_to_add = []

    for page in pdf.pages:
        pages_to_add.append(page)
        pdf_writer = PdfWriter()
        for page_to_add in pages_to_add:
            pdf_writer.add_page(page_to_add)
        temp_filename = write_pdf_writer_to_file(pdf_writer, output_folder, fname, counter)
        
        if os.path.getsize(temp_filename) > size_limit_mb * 1024 * 1024:
            # If the file size exceeds the limit, remove the last page from the list and save the file
            pages_to_add.pop() # Remove the last page from the list
            if pages_to_add: # If there are still pages left
                # Write the current list of pages to a file, excluding the last one that caused overflow
                pdf_writer = PdfWriter()
                for page_to_add in pages_to_add:
                    pdf_writer.add_page(page_to_add)
                write_pdf_writer_to_file(pdf_writer, output_folder, fname, counter)
                counter += 1
            # Reset the list of pages to add with only the last page
            pages_to_add = [page]

    # Save any remaining pages in the last PDF part
    if pages_to_add:
        pdf_writer = PdfWriter()
        for page_to_add in pages_to_add:
            pdf_writer.add_page(page_to_add)
        write_pdf_writer_to_file(pdf_writer, output_folder, fname, counter)

# Define a function to process all PDF files in a folder
def process_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_splitter(os.path.join(input_folder, filename), output_folder)

# Define the main function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split PDF files into smaller parts.')
    parser.add_argument('input_folder', type=str, help='The folder containing PDF files to split.')
    parser.add_argument('output_folder', type=str, help='The folder to save the split PDF files.')
    args = parser.parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    process_folder(args.input_folder, args.output_folder)