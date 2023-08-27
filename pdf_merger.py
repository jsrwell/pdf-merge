"""
PDF Merger - jsrwell

This script allows the user to select multiple PDF files and merge them into
a single PDF file. The user can also specify the order in which the PDFs
should be merged.

Dependencies:
- tkinter (for GUI)
- PyPDF2 (for PDF manipulation)
"""

import PyPDF2
import inflect
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog


def merge_pdfs(output_filename, pdf_files):
    """
    Merge multiple PDF files into a single PDF.

    Args:
        output_filename (str): The name of the output merged PDF file.
        pdf_files (list): List of paths to the input PDF files.
    """
    merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        if pdf_file:
            merger.append(pdf_file)

    with open(output_filename, "wb") as output_file:
        merger.write(output_file)


def position(number):
    """
    Return the position of the number.

    Args:
        number (int): The number for which the position is required.

    Returns:
        str: The ordinal position of the number (e.g., "first", "second").
    """
    p = inflect.engine()
    position = p.ordinal(number)
    return position


def select_files():
    """
    Select and merge PDF files according to user-defined order.
    """
    file_paths = filedialog.askopenfilenames(
        filetypes=[("PDF Files", "*.pdf")])

    if file_paths:
        output_filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if output_filename:
            sorted_files = []
            file_position = 0
            positioned_files = ""

            for pdf_path in file_paths:
                number_of_files = len(file_paths)
                file_position += 1
                file_name = pdf_path.split("/")[-1]

                prompt = (
                    f"This is the {position(file_position)} pdf "
                    "archive, type the position of the number order of"
                    " merge.\n\n "
                    f"Actual archive name:\n {file_name}\n\n"
                    "Number of files positioned/total: "
                    f"{len(sorted_files)}/{number_of_files}\n"
                    f"Actual positions:\n{positioned_files}\n"
                )

                order = simpledialog.askinteger(
                    "Order", prompt, minvalue=1, maxvalue=number_of_files)
                sorted_files.append((order, pdf_path))
                positioned_files += f"Position {order} - {file_name}\n"

            sorted_files.sort(key=lambda x: x[0])

            sorted_pdf_paths = [pdf_path for _, pdf_path in sorted_files]

            merge_pdfs(output_filename, sorted_pdf_paths)
            print("PDFs merged successfully.")


app = tk.Tk()
app.withdraw()

select_files()
