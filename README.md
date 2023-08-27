# PDF Merger
[![GitHub Release](https://img.shields.io/github/release/jsrwell/pdf-merger.svg)](https://github.com/jsrwell/pdf-merger/releases)
[![GitHub Commits](https://img.shields.io/github/commits-since/jsrwell/pdf-merger/latest.svg)](https://github.com/jsrwell/pdf-merger/commits)
[![GitHub Contributors](https://img.shields.io/github/contributors/jsrwell/pdf-merger.svg)](https://github.com/jsrwell/pdf-merger/graphs/contributors)

PDF Merger is a Python script that allows you to merge multiple PDF files into a single PDF. You can also specify the order in which the PDFs should be merged. This script utilizes the Tkinter library for GUI and PyPDF2 library for PDF manipulation.

## Features
- Merge multiple PDF files into a single PDF.
- Specify the order of PDF files for merging.
- User-friendly graphical interface.

## Dependencies
- Python 3.x
- Tkinter
- PyPDF2
- Inflect (for ordinal number conversion)

## Installation
1. Clone the repository or download the ZIP file.
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    ```
   - Windows:
    ```powershell
    . venv\Scripts\Activate
    ```
   - Linux:
    ```bash
    source venv/bin/activate
    ```
3. Install the required dependencies using the following command:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the script using Python:
    ```bash
    python pdf_merger.py
    ```
2. A GUI window will appear. Click the "Select PDF Files" button to choose multiple PDF files for merging.
3. Specify the output file name and location where the merged PDF will be saved.
4. Choose the order in which the PDFs should be merged. The script will prompt you to input the position of each PDF file.
5. Use it!

## License
This project is licensed under the [MIT License](LICENSE).

## Author
jsrwell - Wellington Jackson

## Contact
For questions or suggestions, please feel free to contact [jsrwell.dev@gmail.com](mailto:jsrwell.dev@gmail.com).
