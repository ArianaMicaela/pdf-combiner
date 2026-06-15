PDF Combiner

Simple Python utility that merges multiple PDF files into a single document.
The script automatically detects PDF files in the same folder, sorts them according to the numbers found in their filenames, and generates a combined PDF.

Features.
* Automatically detects PDF files in the current directory.
* Sorts files by the first number found in their names.
* Merges all pages into a single PDF.
* Works as both a Python script and a compiled executable.
* Generates PDF_FINAL.pdf automatically.

Requirements
* Python 3.8+
* pypdf

Install dependencies:
pip install pypdf

Usage
Place your PDF files in the same folder as the script.

Example:
Chapter_1.pdf
Chapter_2.pdf
Chapter_3.pdf

Run:
python pdf_combiner.py

The script will create:
PDF_FINAL.pdf

## Example Output
Se encontraron 3 PDFs. Uniendo...
Agregando Chapter_1.pdf
Agregando Chapter_2.pdf
Agregando Chapter_3.pdf
PDF unido correctamente

How Sorting Works
The script extracts the first number found in each filename and uses it to determine the merge order.

Example:
Part_1.pdf
Part_2.pdf
Part_10.pdf
will be merged in the correct numerical order.