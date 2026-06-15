PDF Combiner



Simple Python utility that merges multiple PDF files into a single document.
The script automatically detects PDF files in the same folder, sorts them according to the numbers found in their filenames, and generates a combined PDF.



Features.

* Automatically detects PDF files in the current directory.
* Sorts files by the first number found in their names.
* Merges all pages into a single PDF.
* Works as both a Python script and a compiled executable.
* Generates PDF\_FINAL.pdf automatically.
* 

Requirements

* Python 3.8+
* pypdf



Install dependencies:
pip install pypdf



Usage
Place your PDF files in the same folder as the script.



Example:
Chapter\_1.pdf
Chapter\_2.pdf
Chapter\_3.pdf



Run:
python pdf\_combiner.py



The script will create:
PDF\_FINAL.pdf



Example output:

Se encontraron 3 PDFs. Uniendo...
Agregando Chapter\_1.pdf
Agregando Chapter\_2.pdf
Agregando Chapter\_3.pdf
PDF unido correctamente



How Sorting Works
The script extracts the first number found in each filename and uses it to determine the merge order.



Example:
Part\_1.pdf
Part\_2.pdf
Part\_10.pdf
will be merged in the correct numerical order.

