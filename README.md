# PDF File Splitter

This Python script allows users to split PDF files into smaller parts based on a size limit. It's particularly useful for handling large PDF files that need to be divided into smaller, more manageable files.

## Features

- Split PDF files into parts smaller than a specified size limit.
- Automatically handles the creation of output directories if they don't exist.
- Provides clear output messages for tracking the split process.

## Requirements

To run this script, you need Python installed on your system along with the following Python packages:
- [PyPDF2](https://pypi.org/project/PyPDF2/)

You can install the required package using pip:

```bash
pip install PyPDF2
```

## Ussage

To use the script, you need to provide the input folder containing the PDF files you want to split and the output folder where the split files will be saved.

```bash
python run.py <input_folder> <output_folder>
```

## Arguments

* input_folder: The folder containing PDF files to split.
* output_folder: The folder to save the split PDF files.

## Example

Assuming you have a folder named PDFs with PDF files and you want to save the split files into a folder named output, you would run:

```bash
python run.py input output
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or have identified bugs.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

